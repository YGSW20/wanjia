"""Batch update prices from real market data"""
import sqlite3, os, datetime

db_path = os.path.join(os.path.dirname(__file__), 'wanjia.db')
if not os.path.exists(db_path):
    print("DB not found. Run app first.")
    exit(1)

db = sqlite3.connect(db_path)
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

# Real price data: product_id -> {platform: (low, high)}
real_prices = {
    46: {'闲鱼': (1389, 1700), '京东': (1500, 1700), '淘宝': (1389, 1650), '拼多多': (1389, 1600), '得物': (1500, 1800)},   # PGU
    1:  {'闲鱼': (900, 1100), '京东': (1000, 1200), '淘宝': (950, 1100), '拼多多': (900, 1050), '得物': (1000, 1250)},    # MGEX强袭自由
    5:  {'闲鱼': (319, 453), '京东': (350, 450), '淘宝': (319, 453), '拼多多': (319, 420), '得物': (380, 480)},           # MG卡牛
    6:  {'闲鱼': (395, 441), '京东': (400, 450), '淘宝': (395, 441), '拼多多': (395, 430), '得物': (420, 480)},           # MG卡沙
    25: {'闲鱼': (199, 345), '京东': (220, 320), '淘宝': (199, 345), '拼多多': (199, 300), '得物': (240, 360)},           # RG牛
    27: {'闲鱼': (220, 315), '京东': (240, 310), '淘宝': (220, 315), '拼多多': (220, 300), '得物': (260, 340)},           # RG海牛
    26: {'闲鱼': (216, 219), '京东': (220, 250), '淘宝': (216, 219), '拼多多': (216, 230), '得物': (230, 260)},           # RG沙扎比
    22: {'闲鱼': (189, 269), '京东': (210, 270), '淘宝': (189, 269), '拼多多': (189, 250), '得物': (220, 290)},           # MGSD自由
    28: {'闲鱼': (147, 205), '京东': (160, 200), '淘宝': (147, 205), '拼多多': (147, 190), '得物': (180, 220)},           # RG元祖2.0
    2:  {'闲鱼': (199, 279), '京东': (220, 280), '淘宝': (199, 279), '拼多多': (199, 260), '得物': (230, 300)},           # MG巴巴托斯
    29: {'闲鱼': (188, 262), '京东': (200, 260), '淘宝': (188, 262), '拼多多': (188, 240), '得物': (210, 280)},           # RG独角兽
    40: {'闲鱼': (28, 120), '京东': (50, 120), '淘宝': (28, 120), '拼多多': (28, 100), '得物': (60, 140)},               # HG风灵
    3:  {'闲鱼': (210, 305), '京东': (230, 300), '淘宝': (210, 305), '拼多多': (210, 280), '得物': (240, 320)},           # MG自由2.0
    8:  {'闲鱼': (600, 700), '京东': (620, 700), '淘宝': (600, 700), '拼多多': (600, 680), '得物': (650, 750)},           # MG卡ZZ
    7:  {'闲鱼': (435, 445), '京东': (440, 460), '淘宝': (435, 445), '拼多多': (435, 450), '得物': (450, 480)},           # MG卡海牛
    35: {'闲鱼': (427, 481), '京东': (440, 480), '淘宝': (427, 481), '拼多多': (427, 470), '得物': (460, 520)},           # RG吉翁号
    47: {'闲鱼': (1320, 2980), '京东': (1400, 2800), '淘宝': (1320, 2980), '拼多多': (1320, 2700), '得物': (1500, 3200)}, # PG独角兽
}

# SHF孙悟空 = product ID around 220+ (need to find)
# 乐高42115 = product ID around 240+
# AirPods Pro 2 = product ID around 308+

updated = 0
for pid, platforms in real_prices.items():
    for plat, (low, high) in platforms.items():
        # Update existing price or insert new
        existing = db.execute('SELECT id FROM prices WHERE product_id=? AND platform=?', (pid, plat)).fetchone()
        if existing:
            db.execute('UPDATE prices SET price_low=?, price_high=?, source=1, updated_at=? WHERE id=?',
                       (low, high, now, existing[0]))
            updated += 1
        else:
            new_id = db.execute('SELECT COALESCE(MAX(id),0)+1 FROM prices').fetchone()[0]
            db.execute('INSERT INTO prices (id, product_id, platform, price_low, price_high, url, in_stock, is_scalper, source, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?)',
                       (new_id, pid, plat, low, high, '', 1, 0, 1, now))
            updated += 1
    # Add to price_history
    low = min(p[0] for p in platforms.values())
    db.execute('INSERT INTO price_history (product_id, platform, price, reporter, recorded_at) VALUES (?,?,?,?,?)',
               (pid, '全网最低', low, 'Felix', now))

db.commit()
print(f'Updated {updated} prices across {len(real_prices)} products.')
print('Reporter: Felix - check /api/leaderboard')

# Show what was updated
for pid in list(real_prices.keys())[:5]:
    name = db.execute('SELECT name FROM products WHERE id=?', (pid,)).fetchone()
    if name:
        prices = db.execute('SELECT platform, price_low, price_high FROM prices WHERE product_id=? AND source=1', (pid,)).fetchall()
        print(f'  {name[0][:20]}: {[(p[0],p[1],p[2]) for p in prices]}')

db.close()
