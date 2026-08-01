# 万代高达全型号数据库
# 格式: (id, name, series, brand, release_date, msrp, image_url, search_keywords)
# price_specs: {id: (msrp, popularity)}  popularity: -1冷门 0正常 1热门 2爆款

PRODUCTS = []
PRICE_SPECS = {}
PID = [0]

def add(name, series, msrp, year, pop=0, kw=''):
    PID[0] += 1
    pid = PID[0]
    full_kw = f'{name} {series} {kw}'.strip()
    PRODUCTS.append((pid, name, series, '万代', year, msrp, None, full_kw))
    PRICE_SPECS[pid] = (msrp, pop)

# ═══════════════════════════════════════════
# PG (Perfect Grade) — 全系列 15 款
# ═══════════════════════════════════════════
add('PG RX-78-2 元祖高达', 'PG', 800, '1998-11', pop=-1, kw='元祖 78 PG')
add('PG 扎古 II 夏亚专用', 'PG', 800, '1999-07', pop=-1, kw='扎古 夏亚 zaku')
add('PG Z高达', 'PG', 900, '2000-03', pop=-1, kw='Z zeta PG')
add('PG 飞翼零式 EW', 'PG', 900, '2000-11', pop=-1, kw='飞翼零式 掉毛 wing zero')
add('PG 强袭高达', 'PG', 900, '2004-11', pop=-1, kw='强袭 strike PG')
add('PG 空中霸王', 'PG', 350, '2005-06', pop=-1, kw='空中霸王 striker')
add('PG 红色异端高达', 'PG', 1000, '2009-03', pop=0, kw='红异端 astray red frame')
add('PG 00 Raiser', 'PG', 1200, '2009-11', pop=0, kw='00 raiser 蛋蛋')
add('PG 强袭自由高达', 'PG', 1500, '2010-12', pop=0, kw='强袭自由 strike freedom')
add('PG 独角兽高达', 'PG', 1300, '2014-12', pop=1, kw='独角兽 unicorn 骗钱兽')
add('PG 独角兽二号机 报丧女妖', 'PG', 1300, '2015-09', pop=0, kw='报丧 banshee 二号机')
add('PG 能天使高达', 'PG', 1200, '2017-12', pop=0, kw='能天使 exia PG')
add('PG 完美强袭高达', 'PG', 1500, '2020-02', pop=0, kw='完美强袭 perfect strike')
add('PG Unleashed RX-78-2', 'PGU', 1400, '2020-12', pop=2, kw='PGU 元祖 78 unleashed')
add('PG 独角兽高达 最终决战Ver', 'PG', 1500, '2021-11', pop=1, kw='独角兽 final battle')

# ═══════════════════════════════════════════
# MGEX — 3 款
# ═══════════════════════════════════════════
add('MGEX 独角兽高达 Ver.Ka', 'MGEX', 1200, '2020-09', pop=1, kw='独角兽 unicorn verka')
add('MGEX 强袭自由高达', 'MGEX', 850, '2022-11', pop=2, kw='强袭自由 strike freedom mgex')
add('MGEX 强袭自由 暮光版', 'MGEX', 1800, '2024-06', pop=2, kw='暮光 twilight 基地限定')

# ═══════════════════════════════════════════
# MGSD — 5 款
# ═══════════════════════════════════════════
add('MGSD 自由高达', 'MGSD', 280, '2024-01', pop=1, kw='freedom 自由')
add('MGSD 巴巴托斯', 'MGSD', 280, '2024-10', pop=1, kw='barbatos 巴巴托斯')
add('MGSD 飞翼零式 EW', 'MGSD', 300, '2025-06', pop=1, kw='wing zero 飞翼 掉毛')
add('MGSD 独角兽高达', 'MGSD', 300, '2025-11', pop=1, kw='unicorn 独角兽')
add('MGSD 牛高达', 'MGSD', 320, '2026-04', pop=1, kw='nu gundam 牛')

# ═══════════════════════════════════════════
# MG Ver.Ka — 全系列 ~25 款
# ═══════════════════════════════════════════
add('MG 元祖高达 Ver.Ka', 'MG Ver.Ka', 350, '2002-12', pop=0, kw='RX-78-2 78 verka')
add('MG 飞翼高达 Ver.Ka', 'MG Ver.Ka', 300, '2004-03', pop=-1, kw='wing verka')
add('MG 飞翼零式 EW Ver.Ka', 'MG Ver.Ka', 380, '2020-12', pop=1, kw='掉毛 天使 wing zero verka')
add('MG 十字骷髅高达 X1 Ver.Ka', 'MG Ver.Ka', 320, '2006-09', pop=0, kw='海盗 crossbone verka')
add('MG 独角兽高达 Ver.Ka', 'MG Ver.Ka', 400, '2007-12', pop=0, kw='独角兽 unicorn verka')
add('MG 新安洲 Ver.Ka', 'MG Ver.Ka', 500, '2008-12', pop=1, kw='sinanju 新安洲 verka')
add('MG V高达 Ver.Ka', 'MG Ver.Ka', 300, '2009-12', pop=-1, kw='victory verka')
add('MG 飞翼零式 EW Ver.Ka 钛电镀', 'MG Ver.Ka', 650, '2010-06', pop=1, kw='titanium 钛')
add('MG 全武装独角兽 Ver.Ka', 'MG Ver.Ka', 550, '2011-12', pop=0, kw='FA unicorn verka')
add('MG 牛高达 Ver.Ka', 'MG Ver.Ka', 500, '2012-12', pop=1, kw='卡牛 nu gundam verka')
add('MG 沙扎比 Ver.Ka', 'MG Ver.Ka', 650, '2013-12', pop=1, kw='卡沙 sazabi verka')
add('MG 海牛高达 Ver.Ka', 'MG Ver.Ka', 500, '2014-08', pop=1, kw='卡海牛 hi-nu verka')
add('MG V2高达 Ver.Ka', 'MG Ver.Ka', 350, '2015-12', pop=-1, kw='victory V2 verka')
add('MG ZZ高达 Ver.Ka', 'MG Ver.Ka', 450, '2017-10', pop=0, kw='卡ZZ double zeta verka')
add('MG 百式 Ver.Ka', 'MG Ver.Ka', 450, '2025-09', pop=0, kw='百式 hyaku shiki verka')
add('MG NT-1 Alex Ver.Ka', 'MG Ver.Ka', 380, '2019-06', pop=0, kw='alex NT1 亚历克斯 verka')
add('MG 全装甲ZZ高达 Ver.Ka', 'MG Ver.Ka', 580, '2023-06', pop=0, kw='FAZZ verka')
add('MG 多鲁基斯 Fluegel Ver.Ka', 'MG Ver.Ka', 420, '2024-03', pop=0, kw='多鲁基斯 tallgeese fluegel')

# ═══════════════════════════════════════════
# MG — 通贩 + 限定 主力 ~120 款
# ═══════════════════════════════════════════
# 0079 / Origin
add('MG 元祖高达 1.0', 'MG', 200, '1995-07', pop=-1, kw='RX-78-2 初代')
add('MG 元祖高达 1.5', 'MG', 200, '2000-06', pop=-1, kw='RX-78-2')
add('MG 元祖高达 2.0', 'MG', 280, '2008-07', pop=0, kw='RX-78-2 2.0')
add('MG 元祖高达 3.0', 'MG', 300, '2013-08', pop=0, kw='RX-78-2 3.0')
add('MG 元祖高达 Origin', 'MG Origin', 320, '2015-11', pop=0, kw='RX-78-2 GTO origin')
add('MG 元祖高达 Origin 特殊镀膜', 'MG Origin', 550, '2016-03', pop=0, kw='GTO origin special coating')
add('MG 扎古 II 夏亚专用 2.0', 'MG', 250, '2007-05', pop=0, kw='扎古 zaku 夏亚 char')
add('MG 扎古 II 量产型 2.0', 'MG', 250, '2007-03', pop=-1, kw='扎古 zaku 量产')
add('MG 老虎 2.0', 'MG', 280, '2009-09', pop=-1, kw='gouf 老虎')
add('MG 大魔', 'MG', 300, '1999-06', pop=-1, kw='dom 大魔')
add('MG 魔蟹', 'MG', 200, '1999-08', pop=-1, kw='魔蟹 zgok')
add('MG 强人', 'MG', 280, '2004-04', pop=-1, kw='强人 gyan')
add('MG 龟霸', 'MG', 280, '2005-09', pop=-1, kw='龟霸 acguy')
add('MG 吉姆 2.0', 'MG', 250, '2009-02', pop=-1, kw='GM 吉姆')
add('MG 吉姆 sniper II', 'MG', 280, '2017-01', pop=0, kw='吉姆狙击 sniper')
add('MG 高达 NT-1 Alex 2.0', 'MG', 300, '2019-06', pop=0, kw='alex NT1 0080')
add('MG 肯普法', 'MG', 300, '2012-10', pop=0, kw='kampfer 京宝梵')

# Z / ZZ
add('MG 百式 2.0', 'MG', 320, '2015-05', pop=0, kw='百式 hyaku shiki')
add('MG Z高达 2.0', 'MG', 350, '2005-12', pop=0, kw='Z zeta')
add('MG 高达 Mk-II 2.0 AEUG', 'MG', 280, '2005-10', pop=-1, kw='mk2 马克兔')
add('MG 高达 Mk-II 2.0 Titans', 'MG', 280, '2006-03', pop=-1, kw='mk2 titans 提坦斯')
add('MG 力奇戴亚斯', 'MG', 300, '2013-02', pop=-1, kw='力奇戴亚斯 rick dias')
add('MG 卡碧尼', 'MG', 300, '2001-09', pop=-1, kw='卡碧尼 qubeley')

# CCA 逆袭的夏亚
add('MG 牛高达 1.0', 'MG', 320, '2000-12', pop=-1, kw='nu gundam')
add('MG 沙扎比 1.0', 'MG', 500, '2000-06', pop=-1, kw='sazabi')
add('MG 灵格斯', 'MG', 320, '2008-01', pop=-1, kw='灵格斯 re-gz')
add('MG 基拉德卡', 'MG', 320, '2018-07', pop=-1, kw='基拉德卡 geara doga')
add('MG 乍得多卡', 'MG', 300, '2014-06', pop=-1, kw='乍得多卡 jegan')
add('MG 海牛高达 1.0', 'MG', 500, '2007-02', pop=0, kw='hi-nu 海牛')

# Unicorn
add('MG 新安洲 OVA', 'MG', 450, '2010-02', pop=0, kw='sinanju 新安洲')
add('MG 独角兽 OVA', 'MG', 350, '2010-03', pop=0, kw='unicorn ova')
add('MG 报丧女妖 OVA', 'MG', 380, '2012-06', pop=0, kw='banshee 报丧 二号机')
add('MG 全武装独角兽 红', 'MG', 500, '2012-07', pop=0, kw='FA unicorn 全武装')
add('MG 独角兽 二号机 命运女神', 'MG', 400, '2014-02', pop=0, kw='命运女神 norn banshee')
add('MG 独角兽 三号机 菲尼克斯', 'MG', 800, '2014-06', pop=0, kw='菲尼克斯 phenex 三号机')
add('MG 杰斯塔', 'MG', 280, '2013-07', pop=0, kw='jesta 杰斯塔')
add('MG 里歇尔', 'MG', 320, '2010-10', pop=-1, kw='里歇尔 rezel')

# F91 / Crossbone
add('MG F91 高达', 'MG', 250, '2006-07', pop=0, kw='F91')
add('MG 十字骷髅高达 X1', 'MG', 280, '2010-01', pop=0, kw='海盗 crossbone x1')
add('MG 十字骷髅高达 X2', 'MG', 300, '2013-12', pop=0, kw='海盗 crossbone x2')
add('MG 十字骷髅高达 X3', 'MG', 320, '2017-03', pop=0, kw='海盗 crossbone x3')

# G Gundam
add('MG 神高达', 'MG', 280, '2001-07', pop=0, kw='god gundam 神')
add('MG 尊者高达', 'MG', 320, '2003-02', pop=-1, kw='master gundam 尊者')
add('MG 闪光高达', 'MG', 280, '2002-11', pop=-1, kw='shining 闪光')

# Wing
add('MG 飞翼高达 EW', 'MG', 280, '2010-03', pop=0, kw='wing ew')
add('MG 死神高达 EW', 'MG', 280, '2011-02', pop=0, kw='死神 deathscythe ew')
add('MG 神龙高达 EW', 'MG', 280, '2011-10', pop=-1, kw='神龙 shenlong ew')
add('MG 沙漠高达 EW', 'MG', 280, '2012-03', pop=-1, kw='沙漠 sandrock ew')
add('MG 重武装高达 EW', 'MG', 300, '2012-09', pop=0, kw='重武装 heavyarms ew')
add('MG 托鲁基斯 EW', 'MG', 280, '2013-01', pop=0, kw='托鲁基斯 tallgeese')
add('MG 艾比安高达 EW', 'MG', 300, '2016-07', pop=0, kw='艾比安 epyon ew')

# SEED
add('MG 强袭高达 RM', 'MG', 280, '2013-05', pop=0, kw='strike RM 强袭')
add('MG 自由高达 2.0', 'MG', 300, '2016-04', pop=0, kw='freedom 2.0 自由')
add('MG 正义高达', 'MG', 320, '2017-06', pop=0, kw='justice 正义')
add('MG 神意高达', 'MG', 350, '2017-04', pop=0, kw='神意 providence')
add('MG 强袭自由高达', 'MG', 350, '2006-12', pop=0, kw='strike freedom 强袭自由')
add('MG 命运高达', 'MG', 320, '2007-10', pop=0, kw='destiny 命运')
add('MG 无限正义高达', 'MG', 320, '2008-08', pop=0, kw='infinite justice 无正')
add('MG 决斗高达', 'MG', 280, '2012-02', pop=-1, kw='duel 决斗')
add('MG 暴风高达', 'MG', 280, '2012-09', pop=-1, kw='buster 暴风')
add('MG 迅雷高达', 'MG', 280, '2012-06', pop=-1, kw='blitz 迅雷')
add('MG 圣盾高达', 'MG', 320, '2012-10', pop=0, kw='aegis 圣盾')
add('MG 红异端改', 'MG', 320, '2010-02', pop=0, kw='红异端 astray red frame')
add('MG 蓝异端 D', 'MG', 320, '2014-08', pop=-1, kw='蓝异端 astray blue')
add('MG 强袭 Rouge + IWSP', 'MG', 350, '2014-04', pop=-1, kw='rouge IWSP')

# 00
add('MG 能天使高达', 'MG', 300, '2009-07', pop=0, kw='exia 能天使')
add('MG 00 Qan[T]', 'MG', 350, '2010-11', pop=0, kw='00q 量子型 蛋蛋Q')
add('MG 00 Raiser', 'MG', 380, '2011-05', pop=0, kw='00r oo raiser 蛋蛋')
add('MG 力天使高达', 'MG', 300, '2019-03', pop=0, kw='dynames 力天使')
add('MG 主天使高达', 'MG', 320, '2020-05', pop=0, kw='kyrios 主天使')
add('MG 德天使高达', 'MG', 480, '2021-11', pop=1, kw='virtue 德天使')
add('MG 座天使一号', 'MG', 320, '2023-03', pop=0, kw='座天使 thrones')

# AGE
add('MG AGE-1 普通型', 'MG', 250, '2012-02', pop=-1, kw='age1')
add('MG AGE-2 普通型', 'MG', 280, '2012-08', pop=-1, kw='age2')

# IBO 铁血
add('MG 巴巴托斯 第四形态', 'MG', 320, '2019-12', pop=0, kw='巴巴托斯 barbatos')
add('MG 巴巴托斯 第六形态', 'MG', 350, '2021-05', pop=0, kw='barbatos 6th')
add('MG 高达·维达尔', 'MG', 350, '2023-06', pop=0, kw='维达尔 vidar')

# Turn A / Turn X
add('MG Turn A高达', 'MG', 300, '2007-08', pop=-1, kw='turn A TA')
add('MG Turn X高达', 'MG', 420, '2014-06', pop=-1, kw='turn X TX')

# Other notable MG
add('MG 全装甲高达 TB', 'MG', 380, '2017-07', pop=0, kw='FA 全装甲 thunderbolt')
add('MG 精神力扎古 TB', 'MG', 550, '2017-12', pop=0, kw='精神病扎古 psycho zaku TB')
add('MG 狙击型吉姆 II WD', 'MG', 280, '2018-02', pop=0, kw='gm sniper white dingo')
add('MG 深度强袭高达', 'MG', 1200, '2018-03', pop=0, kw='deep striker 深度强袭')
add('MG 飞翼零式 EW 白雪姬', 'MG', 600, '2023-01', pop=1, kw='白雪姬 snow white 掉毛')
add('MG Narrative 高达 C装备', 'MG', 450, '2024-02', pop=0, kw='narrative NT')

# ═══════════════════════════════════════════
# RG — 全系列 ~45 款
# ═══════════════════════════════════════════
add('RG 元祖高达 1.0', 'RG', 200, '2010-07', pop=-1, kw='RX-78-2 1.0')
add('RG 夏亚专用扎古 II', 'RG', 200, '2010-11', pop=-1, kw='扎古 zaku 夏亚 char')
add('RG 强袭高达', 'RG', 200, '2011-04', pop=-1, kw='strike 强袭')
add('RG 自由高达', 'RG', 220, '2011-11', pop=-1, kw='freedom 自由')
add('RG 空战强袭高达', 'RG', 200, '2012-02', pop=-1, kw='aile strike')
add('RG 正义高达', 'RG', 220, '2012-07', pop=-1, kw='justice 正义')
add('RG 命运高达', 'RG', 200, '2013-04', pop=0, kw='destiny 命运')
add('RG Z高达', 'RG', 250, '2012-11', pop=-1, kw='Z zeta')
add('RG GP01 零式', 'RG', 200, '2013-07', pop=-1, kw='gp01')
add('RG GP01Fb 全装甲', 'RG', 220, '2013-08', pop=-1, kw='gp01fb')
add('RG 强袭自由高达', 'RG', 220, '2013-11', pop=0, kw='strike freedom 强袭自由')
add('RG 能天使高达', 'RG', 200, '2014-04', pop=0, kw='exia 能天使')
add('RG 飞翼零式 EW', 'RG', 200, '2014-12', pop=0, kw='wing zero 飞翼 掉毛')
add('RG 00 Raiser', 'RG', 250, '2015-04', pop=0, kw='00 raiser 蛋蛋')
add('RG 红色异端高达', 'RG', 200, '2015-08', pop=0, kw='红异端 astray red')
add('RG 00 Qan[T]', 'RG', 220, '2016-05', pop=0, kw='00q 量子型')
add('RG 脉冲高达', 'RG', 220, '2020-04', pop=0, kw='impulse 脉冲')
add('RG 新安洲', 'RG', 280, '2016-08', pop=1, kw='sinanju 新安洲')
add('RG 独角兽高达', 'RG', 280, '2017-08', pop=0, kw='unicorn 骗钱兽 RG独角兽')
add('RG 独角兽二号机 报丧女妖', 'RG', 300, '2018-04', pop=0, kw='banshee 报丧 二号机')
add('RG 独角兽三号机 菲尼克斯', 'RG', 800, '2019-02', pop=0, kw='phenex 菲尼克斯 三号机')
add('RG 托鲁基斯 EW', 'RG', 200, '2018-04', pop=0, kw='tallgeese 托鲁基斯')
add('RG 沙扎比', 'RG', 350, '2018-08', pop=0, kw='sazabi RG沙')
add('RG 全装甲独角兽', 'RG', 380, '2019-08', pop=0, kw='FA unicorn 全武装')
add('RG 牛高达', 'RG', 250, '2019-08', pop=1, kw='nu gundam RG牛 牛高达')
add('RG 十字骷髅高达 X1', 'RG', 220, '2019-10', pop=0, kw='海盗 crossbone x1')
add('RG 海牛高达', 'RG', 300, '2021-09', pop=1, kw='hi-nu RG海牛 海牛')
add('RG 吉翁号', 'RG', 380, '2021-01', pop=0, kw='zeong 吉翁号 鸡瘟号')
add('RG 飞翼高达 TV版', 'RG', 220, '2021-06', pop=0, kw='wing tv')
add('RG 神高达', 'RG', 250, '2022-08', pop=1, kw='god gundam RG神')
add('RG 艾比安高达', 'RG', 270, '2023-09', pop=0, kw='epyon 艾比安')
add('RG 命运脉冲高达', 'RG', 280, '2023-04', pop=0, kw='命运脉冲 destiny impulse')
add('RG ν高达 FF 福冈', 'RG', 300, '2023-04', pop=1, kw='nu ff 福冈 牛FF')
add('RG 元祖高达 2.0', 'RG', 220, '2024-08', pop=1, kw='RX-78-2 2.0 RG元祖')
add('RG 拂晓高达', 'RG', 350, '2024-12', pop=1, kw='akatsuki 拂晓')
add('RG 飞翼零式 EW 白雪姬', 'RG', 450, '2024-06', pop=1, kw='白雪姬 snow white')
add('RG 强袭自由 二式', 'RG', 280, '2025-09', pop=1, kw='strike freedom spec2')
add('RG 无限正义 二式', 'RG', 280, '2025-06', pop=0, kw='infinite justice spec2')
add('RG 决斗高达 尸装', 'RG', 280, '2025-12', pop=0, kw='duel 尸装')

# ═══════════════════════════════════════════
# HG — 热门/长青机型 ~80 款
# ═══════════════════════════════════════════
# The Origin
add('HG RX-78-02 元祖高达 Origin', 'HG Origin', 120, '2015-05', pop=0, kw='GTO RX78 origin')
add('HG 夏亚专用扎古 II Origin', 'HG Origin', 120, '2015-05', pop=0, kw='char zaku origin')

# UC
add('HG 独角兽高达 毁灭模式', 'HGUC', 120, '2010-03', pop=0, kw='unicorn destroy')
add('HG 独角兽高达 独角兽模式', 'HGUC', 100, '2010-03', pop=0, kw='unicorn mode')
add('HG 报丧女妖 毁灭模式', 'HGUC', 130, '2012-03', pop=0, kw='banshee destroy')
add('HG 新安洲', 'HGUC', 150, '2010-10', pop=0, kw='sinanju')
add('HG 刹帝利', 'HGUC', 200, '2010-09', pop=0, kw='刹帝利 kshatriya')
add('HG 牛高达', 'HGUC', 150, '2008-04', pop=0, kw='nu gundam')
add('HG 沙扎比', 'HGUC', 180, '2008-06', pop=0, kw='sazabi')
add('HG 海牛高达', 'HGUC', 180, '2014-05', pop=0, kw='hi-nu')
add('HG 月高达', 'HGUC', 200, '2019-09', pop=1, kw='moon gundam 月')
add('HG V2高达 Assault Buster', 'HGUC', 180, '2015-10', pop=-1, kw='V2 AB')
add('HG 吉翁号', 'HGUC', 200, '2021-05', pop=0, kw='zeong 吉翁号')
add('HG 夜莺', 'HGUC', 480, '2019-07', pop=1, kw='nightingale 夜莺')
add('HG 柯西高达', 'HGUC', 350, '2019-05', pop=0, kw='柯西 xi hathaway')
add('HG 佩涅罗佩', 'HGUC', 500, '2019-10', pop=0, kw='佩涅罗佩 penelope 白鹅')

# SEED
add('HG 强袭自由高达', 'HGCE', 130, '2016-08', pop=0, kw='strike freedom')
add('HG 无限正义高达', 'HGCE', 150, '2020-05', pop=0, kw='infinite justice 无正')
add('HG 命运高达', 'HGCE', 150, '2019-05', pop=0, kw='destiny')
add('HG 强袭高达', 'HGCE', 100, '2014-01', pop=0, kw='strike')

# 00
add('HG 能天使高达', 'HG00', 100, '2008-10', pop=0, kw='exia')
add('HG 00 Raiser', 'HG00', 150, '2009-02', pop=0, kw='00 raiser 蛋蛋')

# IBO
add('HG 巴巴托斯 第四形态', 'HG IBO', 80, '2015-12', pop=0, kw='barbatos')
add('HG 巴巴托斯 天狼座', 'HG IBO', 100, '2016-10', pop=0, kw='barbatos lupus')
add('HG 巴巴托斯 天狼座帝王', 'HG IBO', 120, '2017-04', pop=0, kw='barbatos lupus rex')
add('HG 流星号', 'HG IBO', 100, '2016-04', pop=0, kw='流星 gusion')

# WFM 水星魔女
add('HG 风灵高达', 'HG WFM', 100, '2022-10', pop=0, kw='aerial 风灵')
add('HG 风灵高达改', 'HG WFM', 120, '2023-03', pop=0, kw='aerial rebuild 风灵改')
add('HG 异灵高达', 'HG WFM', 130, '2023-07', pop=0, kw='calibarn 异灵')
add('HG 迪兰扎', 'HG WFM', 100, '2023-01', pop=-1, kw='dilanza')
add('HG 达里尔巴尔德', 'HG WFM', 120, '2023-05', pop=0, kw='darilbalde')

# Gundam SEED Freedom (剧场版)
add('HG 强袭自由 极', 'HGCE', 150, '2024-01', pop=0, kw='strike freedom 极')
add('HG 无限正义 极', 'HGCE', 150, '2024-02', pop=0, kw='infinite justice 极')
add('HG 命运 极', 'HGCE', 150, '2024-03', pop=0, kw='destiny 极')
add('HG 黑骑士小队 湿婆', 'HGCE', 140, '2024-04', pop=0, kw='shiva 黑骑士')

# GQuuuuuuX
add('HG GQuuuuuuX', 'HG', 120, '2025-01', pop=1, kw='GQuuuuuuX gqx')
add('HG 红色高达 GQuuuuuuX ver', 'HG', 120, '2025-02', pop=1, kw='红色高达 red gundam gqx')
add('HG 夏亚专用扎古 GQuuuuuuX ver', 'HG', 120, '2025-05', pop=1, kw='char zaku gqx')

# Other popular HG
add('HG RX-78-2 超越全球', 'HG', 120, '2020-06', pop=0, kw='元祖 beyond global')
add('HG 无限正义高达 新生', 'HGCE', 140, '2020-05', pop=0, kw='IJ revive')
add('HG 命运高达 新生', 'HGCE', 140, '2019-05', pop=0, kw='destiny revive')
add('HG 自由高达 新生', 'HGCE', 130, '2015-08', pop=0, kw='freedom revive')
add('HG 元祖高达 新生', 'HGUC', 80, '2015-07', pop=0, kw='RX-78-2 revive')
add('HG 老虎 新生', 'HGUC', 100, '2018-04', pop=0, kw='gouf revive')

# ═══════════════════════════════════════════
# RE/100 & Full Mechanics
# ═══════════════════════════════════════════
add('RE/100 夜莺', 'RE/100', 480, '2014-09', pop=0, kw='nightingale 夜莺')
add('RE/100 刹帝利', 'RE/100', 380, '2018-02', pop=0, kw='刹帝利 kshatriya')
add('RE/100 钢加农 探测者', 'RE/100', 280, '2019-08', pop=-1, kw='钢加农 guncannon')
add('RE/100 扎古 II 改', 'RE/100', 280, '2019-02', pop=-1, kw='zaku 扎古')
add('FM 灾厄高达', 'FM', 350, '2021-09', pop=0, kw='calamity 灾厄')
add('FM 侵略高达', 'FM', 350, '2021-11', pop=-1, kw='侵略 raider')
add('FM 禁断高达', 'FM', 350, '2022-03', pop=-1, kw='禁断 forbidden')
add('FM 风灵高达', 'FM', 280, '2023-04', pop=0, kw='aerial 风灵 FM')

# ═══════════════════════════════════════════
# Mega Size
# ═══════════════════════════════════════════
add('Mega Size 独角兽高达', 'Mega Size', 500, '2011-03', pop=0, kw='mega unicorn')
add('Mega Size RX-78-2', 'Mega Size', 480, '2010-03', pop=-1, kw='mega 元祖 78')

# ═══════════════════════════════════════════
# SHF 真骨雕 / S.H.Figuarts — ~30 款
# ═══════════════════════════════════════════
add('SHF 孙悟空 超赛 2.0', 'SHF', 350, '2020-07', pop=1, kw='龙珠 悟空 super saiyan 真骨雕')
add('SHF 贝吉塔 超赛 2.0', 'SHF', 350, '2021-03', pop=1, kw='龙珠 贝吉塔 vegeta')
add('SHF 特兰克斯 超赛', 'SHF', 380, '2022-06', pop=1, kw='龙珠 trunks 大特')
add('SHF 孙悟饭 少年期', 'SHF', 320, '2021-11', pop=1, kw='龙珠 悟饭 gohan')
add('SHF 弗利萨 第一形态', 'SHF', 400, '2023-02', pop=1, kw='龙珠 frieza 弗利萨')
add('SHF 人造人18号', 'SHF', 350, '2022-09', pop=1, kw='龙珠 android18')
add('SHF 布罗利 超赛 Full Power', 'SHF', 550, '2023-08', pop=2, kw='龙珠 broly 布罗利')
add('SHF 孙悟空 自在极意功', 'SHF', 380, '2024-01', pop=2, kw='龙珠 UI  ultra instinct')
add('SHF 短笛 潜力解放', 'SHF', 380, '2024-06', pop=1, kw='龙珠 piccolo 比克')
add('SHF 假面骑士 空我 全能形态', 'SHF', 350, '2021-04', pop=1, kw='kamen rider kuuga 真骨雕')
add('SHF 假面骑士 亚极陀 大地形态', 'SHF', 350, '2022-03', pop=1, kw='kamen rider agito 真骨雕')
add('SHF 假面骑士 龙骑', 'SHF', 380, '2022-11', pop=1, kw='kamen rider ryuki 真骨雕')
add('SHF 假面骑士 电王 圣剑形态', 'SHF', 380, '2023-05', pop=1, kw='kamen rider den-o 真骨雕')
add('SHF 假面骑士 W 疾风王牌', 'SHF', 380, '2024-03', pop=1, kw='kamen rider W double 真骨雕')
add('SHF 假面骑士 极狐 马格南推进', 'SHF', 320, '2023-09', pop=1, kw='kamen rider geats')
add('SHF 假面骑士 歌查德 蒸汽蝗虫', 'SHF', 320, '2024-09', pop=0, kw='kamen rider gotchard')
add('SHF 奥特曼 初代', 'SHF', 300, '2022-07', pop=0, kw='ultraman 初代 真骨雕')
add('SHF 奥特曼 迪迦 复合型', 'SHF', 350, '2023-04', pop=1, kw='ultraman tiga 迪迦')
add('SHF 蜘蛛侠 英雄无归', 'SHF', 400, '2022-02', pop=0, kw='spider-man 蜘蛛侠 marvel')
add('SHF 钢铁侠 MK3', 'SHF', 450, '2023-06', pop=0, kw='iron man 钢铁侠 marvel')
add('SHF 火影忍者 漩涡鸣人', 'SHF', 280, '2023-11', pop=0, kw='naruto 鸣人')
add('SHF 火影忍者 宇智波佐助', 'SHF', 280, '2024-02', pop=0, kw='sasuke 佐助 naruto')
add('SHF 海贼王 路飞 鬼岛决战', 'SHF', 300, '2024-04', pop=1, kw='one piece luffy 路飞')
add('SHF 海贼王 索隆 鬼岛决战', 'SHF', 320, '2024-07', pop=1, kw='one piece zoro 索隆')
add('SHF 咒术回战 五条悟', 'SHF', 280, '2024-01', pop=0, kw='jujutsu kaisen gojo')
add('SHF 鬼灭之刃 灶门炭治郎', 'SHF', 250, '2023-08', pop=0, kw='demon slayer tanjiro')

# ═══════════════════════════════════════════
# 圣衣神话 — ~10 款
# ═══════════════════════════════════════════
add('圣衣神话 天马座星矢 EX', '圣衣神话', 500, '2021-06', pop=1, kw='圣斗士 星矢 seiya')
add('圣衣神话 天龙座紫龙 EX', '圣衣神话', 500, '2021-10', pop=1, kw='圣斗士 紫龙 shiryu')
add('圣衣神话 白鸟座冰河 EX', '圣衣神话', 480, '2022-03', pop=0, kw='圣斗士 冰河 hyoga')
add('圣衣神话 仙女座瞬 EX', '圣衣神话', 480, '2022-07', pop=0, kw='圣斗士 瞬 shun')
add('圣衣神话 凤凰座一辉 EX', '圣衣神话', 500, '2022-12', pop=0, kw='圣斗士 一辉 ikki')
add('圣衣神话 双子座撒加 EX', '圣衣神话', 650, '2023-05', pop=1, kw='圣斗士 撒加 saga 黄金')
add('圣衣神话 处女座沙加 EX', '圣衣神话', 680, '2023-09', pop=1, kw='圣斗士 沙加 shaka 黄金')
add('圣衣神话 狮子座艾奥里亚 EX', '圣衣神话', 600, '2024-02', pop=0, kw='圣斗士 艾奥里亚 aiolia 黄金')
add('圣衣神话 射手座艾俄洛斯 EX', '圣衣神话', 650, '2024-07', pop=1, kw='圣斗士 艾俄洛斯 aiolos 黄金')
add('圣衣神话 冥王哈迪斯 EX', '圣衣神话', 750, '2024-11', pop=2, kw='圣斗士 哈迪斯 hades 冥王')

# ═══════════════════════════════════════════
# 泡泡玛特 — ~15 款
# ═══════════════════════════════════════════
add('泡泡玛特 Molly 茉莉 星座系列 盲盒', '泡泡玛特', 69, '2023-06', pop=0, kw='molly 星座 盲盒 popmart')
add('泡泡玛特 Molly 茉莉 敦煌系列', '泡泡玛特', 69, '2023-12', pop=1, kw='molly 敦煌 飞天 popmart')
add('泡泡玛特 Dimoo 迪莫 梦境系列', '泡泡玛特', 69, '2023-08', pop=0, kw='dimoo 梦境 popmart')
add('泡泡玛特 Dimoo 迪莫 夜行系列', '泡泡玛特', 69, '2024-04', pop=1, kw='dimoo 夜行 popmart')
add('泡泡玛特 Skullpanda 骷髅熊猫 温度系列', '泡泡玛特', 69, '2023-09', pop=1, kw='skullpanda 温度 popmart')
add('泡泡玛特 Skullpanda 骷髅熊猫 山海经系列', '泡泡玛特', 79, '2024-06', pop=2, kw='skullpanda 山海经 popmart')
add('泡泡玛特 Crybaby 哭泣宝贝', '泡泡玛特', 69, '2024-08', pop=1, kw='crybaby popmart')
add('泡泡玛特 Labubu 拉布布 精灵系列', '泡泡玛特', 59, '2023-04', pop=2, kw='labubu 精灵 popmart')
add('泡泡玛特 Labubu 拉布布 坐坐系列 大娃', '泡泡玛特', 599, '2024-03', pop=2, kw='labubu 大娃 popmart')
add('泡泡玛特 Pucky 毕奇 精灵系列', '泡泡玛特', 59, '2023-03', pop=0, kw='pucky 毕奇 popmart')
add('泡泡玛特 Hirono 小野 重塑系列', '泡泡玛特', 69, '2024-05', pop=1, kw='hirono 小野 popmart')
add('泡泡玛特 Zsiga 系列', '泡泡玛特', 69, '2024-09', pop=0, kw='zsiga popmart')
add('泡泡玛特 Mega Molly 400% 宇航员', '泡泡玛特', 899, '2023-11', pop=2, kw='mega molly 400% 宇航员 popmart')
add('泡泡玛特 Mega Space Molly 1000%', '泡泡玛特', 3999, '2024-02', pop=2, kw='mega space molly 1000% popmart')

# ═══════════════════════════════════════════
# 乐高 — ~20 款
# ═══════════════════════════════════════════
add('乐高 兰博基尼 Sián FKP 37 42115', '乐高 Technic', 2699, '2020-06', pop=0, kw='lego 兰博基尼 lamborghini 42115')
add('乐高 布加迪 Chiron 42083', '乐高 Technic', 2499, '2018-06', pop=0, kw='lego 布加迪 bugatti 42083')
add('乐高 法拉利 Daytona SP3 42143', '乐高 Technic', 2999, '2022-06', pop=0, kw='lego 法拉利 ferrari 42143')
add('乐高 迈凯伦 P1 42172', '乐高 Technic', 2999, '2024-08', pop=1, kw='lego 迈凯伦 mclaren 42172')
add('乐高 千年隼 75192', '乐高 Star Wars', 5999, '2017-10', pop=1, kw='lego 千年隼 millennium falcon 75192')
add('乐高 AT-AT 全地形装甲 75313', '乐高 Star Wars', 5999, '2021-11', pop=0, kw='lego ATAT 75313')
add('乐高 霍格沃茨城堡 71043', '乐高 Harry Potter', 3199, '2018-09', pop=0, kw='lego 霍格沃茨 hogwarts 71043')
add('乐高 泰坦尼克号 10294', '乐高 Creator', 4999, '2021-11', pop=1, kw='lego 泰坦尼克 titanic 10294')
add('乐高 埃菲尔铁塔 10307', '乐高 Icons', 4999, '2022-11', pop=0, kw='lego 埃菲尔 eiffel 10307')
add('乐高 指环王 幽谷 10316', '乐高 Icons', 3499, '2023-03', pop=1, kw='lego 指环王 rivendell 10316')
add('乐高 蝙蝠侠 蝙蝠洞 76252', '乐高 DC', 2999, '2023-06', pop=0, kw='lego 蝙蝠侠 batcave 76252')
add('乐高 星战 共和国炮艇 75354', '乐高 Star Wars', 1099, '2023-09', pop=0, kw='lego 炮艇 gunship 75354')
add('乐高 兰花 10311', '乐高 Botanical', 399, '2022-05', pop=0, kw='lego 兰花 orchid 10311')
add('乐高 多肉植物 10309', '乐高 Botanical', 399, '2022-05', pop=0, kw='lego 多肉 succulent 10309')
add('乐高 樱花 40725', '乐高 Botanical', 199, '2024-01', pop=1, kw='lego 樱花 cherry blossom 40725')
add('乐高 超级马里奥 64问号块 71395', '乐高 Mario', 1299, '2021-10', pop=0, kw='lego 马里奥 mario 71395')
add('乐高 塞尔达传说 德库树 77092', '乐高 Zelda', 2299, '2024-09', pop=2, kw='lego 塞尔达 zelda 德库树 77092')

# ═══════════════════════════════════════════
# Hot Toys — ~10 款
# ═══════════════════════════════════════════
add('Hot Toys 钢铁侠 MK85 战损版', 'Hot Toys', 2680, '2022-08', pop=1, kw='iron man mk85 battle damaged 复联4')
add('Hot Toys 蜘蛛侠 2099', 'Hot Toys', 1980, '2023-06', pop=1, kw='spider-man 2099 蜘蛛侠 纵横宇宙')
add('Hot Toys 蝙蝠侠 2022 帕丁森版', 'Hot Toys', 1980, '2023-02', pop=1, kw='batman pattinson 新蝙蝠侠')
add('Hot Toys 洛基 第二季', 'Hot Toys', 1780, '2024-03', pop=0, kw='loki 洛基 第二季')
add('Hot Toys 美国队长 终局之战', 'Hot Toys', 1980, '2022-05', pop=0, kw='captain america endgame 美队')
add('Hot Toys 曼达洛人 丁贾林+古古', 'Hot Toys', 2380, '2023-09', pop=1, kw='mandalorian grogu 曼达洛人 古古')
add('Hot Toys 黑神话悟空 天命人', 'Hot Toys', 2580, '2024-10', pop=2, kw='黑神话悟空 black myth wukong')
add('Hot Toys 死侍 3 金刚狼', 'Hot Toys', 2180, '2024-08', pop=2, kw='deadpool wolverine 死侍 金刚狼')

# ═══════════════════════════════════════════
# 一番赏 — ~5 款
# ═══════════════════════════════════════════
add('一番赏 龙珠 VS 布罗利', '一番赏', 58, '2024-03', pop=1, kw='ichiban kuji 龙珠 broly')
add('一番赏 海贼王 四皇传说', '一番赏', 58, '2024-06', pop=1, kw='ichiban kuji one piece 四皇')
add('一番赏 鬼灭之刃 无限城', '一番赏', 58, '2024-05', pop=1, kw='ichiban kuji demon slayer 无限城')
add('一番赏 高达 SEED FREEDOM', '一番赏', 58, '2024-04', pop=1, kw='ichiban kuji gundam seed freedom')
add('一番赏 宝可梦 朱紫', '一番赏', 58, '2024-07', pop=1, kw='ichiban kuji pokemon 宝可梦 朱紫')

# ═══════════════════════════════════════════
# 电子科技 — ~15 款
# ═══════════════════════════════════════════
add('Apple AirPods Pro 2', 'TWS耳机', 1899, '2022-09', pop=0, kw='airpods pro 2 苹果 耳机')
add('Apple AirPods 4', 'TWS耳机', 999, '2024-09', pop=0, kw='airpods 4 苹果 耳机')
add('Sony WH-1000XM5 头戴耳机', 'HiFi耳机', 2499, '2023-03', pop=0, kw='sony xm5 降噪 耳机')
add('Sony WF-1000XM5 降噪豆', 'TWS耳机', 1699, '2023-07', pop=0, kw='sony xm5 降噪豆 TWS')
add('Bose QC Ultra 头戴耳机', 'HiFi耳机', 2799, '2023-10', pop=0, kw='bose qc ultra 降噪')
add('Keychron Q1 Pro 机械键盘', '机械键盘', 898, '2023-08', pop=1, kw='keychron q1 pro 客制化 铝坨坨')
add('Wooting 60HE 磁轴键盘', '机械键盘', 1299, '2024-01', pop=2, kw='wooting 60he 磁轴 电竞 SOCD')
add('罗技 G Pro X Superlight 2', '游戏鼠标', 999, '2023-09', pop=0, kw='logitech gpw 狗屁王 superlight 鼠标')
add('Razer Viper V3 Pro', '游戏鼠标', 1199, '2024-04', pop=1, kw='razer 毒蝰 viper v3 鼠标')
add('ROG 龙鳞 ACE Extreme', '游戏鼠标', 1499, '2024-06', pop=1, kw='rog 龙鳞 harpe ace 鼠标')
add('漫步者 MR4 监听音箱', '桌面音响', 399, '2023-05', pop=0, kw='edifier mr4 音箱 监听')
add('Apple iPad Air M2', '平板', 4399, '2024-05', pop=0, kw='ipad air m2 苹果 平板')
add('大疆 Osmo Pocket 3', '相机', 3499, '2023-10', pop=2, kw='dji osmo pocket 3 大疆 vlog')
add('富士 X100VI', '相机', 8999, '2024-03', pop=2, kw='fujifilm x100vi 富士 旁轴 复古')
add('Kindle Scribe 电子书', '电子阅读', 2699, '2023-11', pop=0, kw='kindle scribe 电子书 手写')

print(f'Total models: {PID[0]}')

