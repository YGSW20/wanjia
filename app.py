from flask import Flask, render_template, request, jsonify, g
import sqlite3, os, urllib.parse
from seed_models import PRODUCTS, PRICE_SPECS

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'wanjia.db')

def platform_search_url(platform, product_name):
    """Generate platform-specific search URL for a product"""
    q = urllib.parse.quote(product_name)
    urls = {
        '闲鱼': f'https://www.goofish.com/search?q={q}',
        '京东': f'https://search.jd.com/Search?keyword={q}&enc=utf-8',
        '淘宝': f'https://s.taobao.com/search?q={q}',
        '拼多多': f'https://yangkeduo.com/search_result.html?search_key={q}',
        '得物': f'https://www.dewu.com/search?keyword={q}',
    }
    return urls.get(platform, '#')

app.jinja_env.globals['platform_search_url'] = platform_search_url

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db: db.close()

def init_db():
    db = sqlite3.connect(DATABASE)
    db.executescript('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            series TEXT,
            brand TEXT,
            release_date TEXT,
            msrp INTEGER,
            image_url TEXT,
            search_keywords TEXT
        );
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            platform TEXT,
            price_low INTEGER,
            price_high INTEGER,
            url TEXT,
            in_stock INTEGER DEFAULT 1,
            is_scalper INTEGER DEFAULT 0,
            source INTEGER DEFAULT 0,
            updated_at TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    ''')
    db.commit()
    # Migration: add source column if missing (safe retry)
    try:
        db.execute('ALTER TABLE prices ADD COLUMN source INTEGER DEFAULT 0')
        db.commit()
    except:
        pass
    db.executescript('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            platform TEXT,
            price INTEGER,
            recorded_at TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    ''')
    db.commit()

    # Seed data if empty
    if db.execute('SELECT COUNT(*) FROM products').fetchone()[0] == 0:
        seed_data(db)

def seed_data(db):
    products = PRODUCTS
    price_specs = PRICE_SPECS

    db.executemany('INSERT INTO products VALUES (?,?,?,?,?,?,?,?)', products)

    import datetime
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def gen_prices(pid, msrp, pop=0):
        """pop: -1=冷门折价, 0=正常, 1=热门溢价, 2=爆款倒挂"""
        platforms = ['闲鱼', '京东', '淘宝', '拼多多', '得物']
        if pop == -1:
            specs = [(0.55,0.75,0),(0.75,0.90,0),(0.70,0.88,0),(0.65,0.82,0),(0.78,0.95,0)]
        elif pop == 1:
            specs = [(0.90,1.15,0),(1.05,1.30,1),(1.00,1.25,1),(0.88,1.10,0),(1.10,1.40,1)]
        elif pop == 2:
            specs = [(1.10,1.50,1),(1.20,1.60,1),(1.15,1.55,1),(0.95,1.20,0),(1.30,1.80,1)]
        else:
            specs = [(0.70,0.95,0),(0.85,1.05,0),(0.82,1.00,0),(0.75,0.95,0),(0.90,1.15,0)]
        return [(pid, platforms[i], int(msrp*s[0]), int(msrp*s[1]), s[2]) for i, s in enumerate(specs)]

    price_id = 0
    prices = []
    for pid, (msrp, pop) in price_specs.items():
        for plat_data in gen_prices(pid, msrp, pop):
            price_id += 1
            # (price_id, pid, platform, low, high, in_stock=1, scalper, source=0, now)
            prices.append((price_id,) + plat_data[:4] + (1, plat_data[4], 0) + (now,))
    db.executemany('INSERT INTO prices (id, product_id, platform, price_low, price_high, in_stock, is_scalper, source, updated_at) VALUES (?,?,?,?,?,?,?,?,?)', prices)

    # Seed price_history with initial snapshot
    for pid, (_, _) in price_specs.items():
        low = db.execute('SELECT MIN(price_low) FROM prices WHERE product_id=?', (pid,)).fetchone()[0]
        if low:
            db.execute('INSERT INTO price_history (product_id, platform, price, recorded_at) VALUES (?,?,?,?)',
                       (pid, '全网最低', low, now))
    db.commit()


# ── Routes ──

@app.route('/')
def home():
    db = get_db()
    hot = db.execute('''
        SELECT p.*, MIN(pr.price_low) as min_price, COUNT(pr.id) as platform_count
        FROM products p JOIN prices pr ON p.id = pr.product_id
        WHERE pr.in_stock = 1
        GROUP BY p.id ORDER BY p.series, p.id
    ''').fetchall()
    return render_template('index.html', hot=hot)

@app.route('/search')
def search():
    q = request.args.get('q', '').strip()
    sort = request.args.get('sort', 'default')
    db = get_db()

    sort_map = {
        'price_asc': 'min_price ASC',
        'price_desc': 'min_price DESC',
        'name': 'p.name ASC',
        'series': 'p.series ASC, p.id ASC',
        'default': 'p.series, p.id',
    }
    order = sort_map.get(sort, 'p.series, p.id')

    if q:
        q_nospace = q.replace(' ', '').replace('　', '')
        products = db.execute(f'''
            SELECT p.*, MIN(pr.price_low) as min_price, COUNT(pr.id) as platform_count
            FROM products p JOIN prices pr ON p.id = pr.product_id
            WHERE (p.name LIKE ? OR p.search_keywords LIKE ?
                   OR REPLACE(p.name, ' ', '') LIKE ?
                   OR REPLACE(p.search_keywords, ' ', '') LIKE ?)
              AND pr.in_stock = 1
            GROUP BY p.id ORDER BY {order}
        ''', (f'%{q}%', f'%{q}%', f'%{q_nospace}%', f'%{q_nospace}%')).fetchall()
    else:
        products = db.execute(f'''
            SELECT p.*, MIN(pr.price_low) as min_price, COUNT(pr.id) as platform_count
            FROM products p JOIN prices pr ON p.id = pr.product_id
            WHERE pr.in_stock = 1
            GROUP BY p.id ORDER BY {order}
        ''').fetchall()
    return render_template('search.html', products=products, query=q, sort=sort)

@app.route('/product/<int:pid>')
def product(pid):
    db = get_db()
    p = db.execute('SELECT * FROM products WHERE id = ?', (pid,)).fetchone()
    if not p: return render_template('404.html', query=''), 404
    prices = db.execute('SELECT * FROM prices WHERE product_id = ? ORDER BY price_low ASC', (pid,)).fetchall()
    min_price = min(pr['price_low'] for pr in prices) if prices else 0
    history = db.execute('''
        SELECT platform, price, recorded_at FROM price_history
        WHERE product_id = ? ORDER BY recorded_at DESC LIMIT 20
    ''', (pid,)).fetchall()
    # Related products: same series
    series_base = p['series'].split(' ')[0].split('.')[0]
    related = db.execute('''
        SELECT p2.*, MIN(pr.price_low) as min_price
        FROM products p2 JOIN prices pr ON p2.id = pr.product_id
        WHERE (p2.series LIKE ? OR p2.series = ?) AND p2.id != ? AND pr.in_stock = 1
        GROUP BY p2.id ORDER BY p2.id LIMIT 8
    ''', (f'{series_base}%', series_base, pid)).fetchall()

    return render_template('product.html', product=p, prices=prices, min_price=min_price, history=history, related=related)

@app.route('/api/report', methods=['POST'])
def report():
    data = request.get_json(silent=True)
    if data is None:
        # Fallback: try form data or raw parse
        if request.form:
            data = request.form.to_dict()
        else:
            import json as _json
            try:
                data = _json.loads(request.get_data(as_text=True))
            except:
                data = None
    if not data or not data.get('product_id') or not data.get('price'):
        return jsonify({'ok': False, 'error': '缺少 product_id 或 price'}), 400
    db = get_db()
    import datetime
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    pid = int(data['product_id'])
    price = int(data['price'])
    plat = data.get('platform', '闲鱼')
    db.execute('INSERT INTO prices (product_id, platform, price_low, price_high, in_stock, is_scalper, source, updated_at) VALUES (?,?,?,?,1,0,1,?)',
               (pid, plat, price, price, now))
    db.execute('INSERT INTO price_history (product_id, platform, price, recorded_at) VALUES (?,?,?,?)',
               (pid, plat, price, now))
    db.commit()
    return jsonify({'ok': True})

@app.route('/api/deals')
def api_deals():
    db = get_db()
    deals = db.execute('''
        SELECT pr.id, pr.platform, pr.price_low, pr.updated_at, p.id as pid, p.name, p.series
        FROM prices pr JOIN products p ON pr.product_id = p.id
        WHERE pr.source = 1
        ORDER BY pr.updated_at DESC LIMIT 20
    ''').fetchall()
    return jsonify([{
        'id': d['id'], 'platform': d['platform'], 'price': d['price_low'],
        'time': d['updated_at'], 'pid': d['pid'], 'name': d['name'], 'series': d['series']
    } for d in deals])

@app.route('/api/suggest')
def suggest():
    q = request.args.get('q', '').strip()
    if len(q) < 1: return jsonify([])
    db = get_db()
    q_nospace = q.replace(' ', '').replace('　', '')
    rows = db.execute('''
        SELECT id, name, series FROM products
        WHERE name LIKE ? OR search_keywords LIKE ?
           OR REPLACE(name, ' ', '') LIKE ?
           OR REPLACE(search_keywords, ' ', '') LIKE ?
        LIMIT 6
    ''', (f'%{q}%', f'%{q}%', f'%{q_nospace}%', f'%{q_nospace}%')).fetchall()
    return jsonify([{'id': r['id'], 'name': r['name'], 'series': r['series']} for r in rows])

# Initialize database on startup (idempotent — runs both via gunicorn and directly)
init_db()

# ── Admin ──
ADMIN_PASSWORD = 'wanjia2026'

def check_admin():
    # Try Basic Auth header
    auth = request.authorization
    if auth and auth.username == 'admin' and auth.password == ADMIN_PASSWORD:
        return True
    # Fallback: cookie/token for proxy environments that strip auth header
    token = request.args.get('token', '') or request.cookies.get('admin_token', '')
    if token == ADMIN_PASSWORD:
        return True
    return False

@app.route('/admin')
def admin_dashboard():
    if not check_admin():
        return ('请登录', 401, {'WWW-Authenticate': 'Basic realm="玩价管理后台"'})
    db = get_db()
    # Combine stats into one query for speed
    row = db.execute('''
        SELECT
            (SELECT COUNT(*) FROM products) as products,
            (SELECT COUNT(*) FROM prices) as prices,
            (SELECT COUNT(*) FROM price_history) as history,
            (SELECT COUNT(DISTINCT series) FROM products) as categories,
            (SELECT COUNT(DISTINCT platform) FROM prices) as platforms
    ''').fetchone()
    stats = dict(row)
    products = db.execute('''
        SELECT p.*, MIN(pr.price_low) as min_price, COUNT(pr.id) as pc
        FROM products p LEFT JOIN prices pr ON p.id = pr.product_id
        GROUP BY p.id ORDER BY p.id DESC LIMIT 30
    ''').fetchall()
    return render_template('admin.html', stats=stats, products=products)

@app.route('/admin/product/add', methods=['GET','POST'])
def admin_add_product():
    if not check_admin():
        return ('请登录', 401, {'WWW-Authenticate': 'Basic realm="玩价管理后台"'})
    db = get_db()
    msg = ''
    if request.method == 'POST':
        name = request.form['name'].strip()
        series = request.form['series'].strip()
        msrp = int(request.form['msrp'])
        brand = request.form.get('brand','万代').strip()
        year = request.form.get('year','2024').strip()
        kw = request.form.get('keywords','').strip()
        pid = db.execute('SELECT COALESCE(MAX(id),0)+1 FROM products').fetchone()[0]
        db.execute('INSERT INTO products VALUES (?,?,?,?,?,?,?,?)',
                   (pid, name, series, brand, year, msrp, None, f'{name} {series} {kw}'))
        # Generate prices
        import datetime
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        for plat, (lm, hm) in [('闲鱼',(0.7,0.95)),('京东',(0.85,1.05)),('淘宝',(0.82,1.0)),('拼多多',(0.75,0.95)),('得物',(0.9,1.15))]:
            pid2 = db.execute('SELECT COALESCE(MAX(id),0)+1 FROM prices').fetchone()[0]
            db.execute('INSERT INTO prices VALUES (?,?,?,?,?,?,?,?,?)',
                       (pid2, pid, plat, int(msrp*lm), int(msrp*hm), '', 1, 0, now))
        db.execute('INSERT INTO price_history (product_id, platform, price, recorded_at) VALUES (?,?,?,?)',
                   (pid, '全网最低', int(msrp*0.7), now))
        db.commit()
        msg = f'✅ {name} 已添加！<a href="/product/{pid}">查看</a>'
    return render_template('admin_form.html', msg=msg, product=None)

@app.route('/admin/product/<int:pid>/edit', methods=['GET','POST'])
def admin_edit_product(pid):
    if not check_admin():
        return ('请登录', 401, {'WWW-Authenticate': 'Basic realm="玩价管理后台"'})
    db = get_db()
    p = db.execute('SELECT * FROM products WHERE id=?',(pid,)).fetchone()
    if not p: return 'Not found', 404
    msg = ''
    if request.method == 'POST':
        name = request.form['name'].strip()
        series = request.form['series'].strip()
        msrp = int(request.form['msrp'])
        kw = request.form.get('keywords','').strip()
        db.execute('UPDATE products SET name=?,series=?,msrp=?,search_keywords=? WHERE id=?',
                   (name, series, msrp, f'{name} {series} {kw}', pid))
        db.commit()
        msg = f'✅ {name} 已更新！<a href="/product/{pid}">查看</a>'
        p = db.execute('SELECT * FROM products WHERE id=?',(pid,)).fetchone()
    prices = db.execute('SELECT * FROM prices WHERE product_id=? ORDER BY platform',(pid,)).fetchall()
    return render_template('admin_form.html', msg=msg, product=p, prices=prices)

@app.route('/admin/product/<int:pid>/price', methods=['POST'])
def admin_update_price():
    if not check_admin():
        return ('请登录', 401, {'WWW-Authenticate': 'Basic realm="玩价管理后台"'})
    db = get_db()
    pid = request.form.get('pid')
    import datetime
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for key in request.form:
        if key.startswith('price_low_'):
            price_id = int(key.replace('price_low_',''))
            low = int(request.form[key])
            high = int(request.form.get(f'price_high_{price_id}', low))
            db.execute('UPDATE prices SET price_low=?, price_high=?, updated_at=? WHERE id=?',
                       (low, high, now, price_id))
            plat = db.execute('SELECT platform, product_id FROM prices WHERE id=?',(price_id,)).fetchone()
            if plat:
                db.execute('INSERT INTO price_history (product_id, platform, price, recorded_at) VALUES (?,?,?,?)',
                           (plat['product_id'], plat['platform'], low, now))
    db.commit()
    return jsonify({'ok': True})

@app.route('/admin/product/<int:pid>/delete', methods=['POST'])
def admin_delete_product(pid):
    if not check_admin():
        return ('请登录', 401, {'WWW-Authenticate': 'Basic realm="玩价管理后台"'})
    db = get_db()
    db.execute('DELETE FROM prices WHERE product_id=?',(pid,))
    db.execute('DELETE FROM price_history WHERE product_id=?',(pid,))
    db.execute('DELETE FROM products WHERE id=?',(pid,))
    db.commit()
    return jsonify({'ok': True})

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', query=''), 404

if __name__ == '__main__':
    import os as _os
    port = int(_os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
