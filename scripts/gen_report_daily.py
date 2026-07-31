# -*- coding: utf-8 -*-
"""生成 fund-report-YYYY-MM-DD-盘中.html 的自包含HTML报告"""
import json, datetime

merged = json.load(open('deliverables/fund-analysis/merged-scores.json', encoding='utf-8'))

# 市场行情快照
market = {
    "a_share": [
        {"name": "上证指数", "value": "3,834.66", "chg": "+0.79%", "note": "昨收3804.69，昨日-0.62%后反弹"},
        {"name": "深证成指", "value": "13,718.31", "chg": "+3.26%", "note": "科技股V型反弹"},
        {"name": "创业板指", "value": "3,411.17", "chg": "+5.13%", "note": "昨日-3.97%后大幅反弹"},
    ],
    "hk": [
        {"name": "恒生指数", "value": "25,747.70", "chg": "-0.43%", "note": "昨收25858.88"},
        {"name": "恒生科技", "value": "4,808.85", "chg": "+0.11%", "note": "昨收4803.77，翻红"},
    ],
    "us": [
        {"name": "道琼斯", "value": "—", "chg": "+1.01%", "note": "隔夜反弹，微软财报超预期+8%"},
        {"name": "纳斯达克", "value": "—", "chg": "+1.67%", "note": "苹果盘后跌超8%（指引不及预期）"},
    ],
    "events": [
        "政治局会议配套细则落地：科创企业研发补贴加码、内需消费扶持细化（从'远期画饼'变'近期落地'）",
        "社保、保险长线资金入市提速，新增入市额度按计划投放",
        "美联储维持利率3.5%-3.75%不变，3名官员主张加息，鲍威尔偏鹰",
        "宇树科技科创板IPO：人形机器人第一股，拟发行4044.6万股（占10%），8/5询价",
        "三星电子Q2营收+130%、营业利润+1814%创新高，存储芯片供应紧张延续",
        "商务部回应美将电力逆变器和先进机器人列入'覆盖清单'：坚决反制",
    ],
}

# 基金展示顺序（按总分降序）
order = ['512170','513050','513690','513060','159549','515010','159841','159605','512800','515290']

funds_meta = {
    '512170': {'name':'医疗ETF华宝','track':'中证医疗指数','manager':'张放','size':'257.61亿','nav':'0.3241元','price':'—','pe':'PE-TTM 29.84','pb':'—','perc':'医疗服务板块分位20.86%','premium':'溢价0.03%~1.2%','flow':'近20日份额-33.65亿份，当日净流入1.98亿','ytd':'-4.51%'},
    '513050': {'name':'中概互联网ETF易方达','track':'中证海外中国互联网50','manager':'余海燕、刘依姗','size':'384.77亿','nav':'1.1416元','price':'1.138元','pe':'PE-TTM约16倍','pb':'—','perc':'成立以来2.53%分位','premium':'折价0.32%（无溢价）','flow':'近1年净流入129.67亿、近6月93.94亿','ytd':'-22.58%'},
    '513690': {'name':'港股红利ETF博时','track':'恒生港股通高股息率指数','manager':'万琼、王萌','size':'43.65亿','nav':'1.1738元','price':'1.170元','pe':'PE-TTM 7.16倍','pb':'—','perc':'近1年5.04%分位','premium':'折价约0.3%（无溢价）','flow':'份额12.1亿→37.18亿持续净申购','ytd':'+8.84%'},
    '513060': {'name':'恒生医疗ETF博时','track':'恒生医疗保健指数','manager':'万琼','size':'份额108.05亿份','nav':'0.5295元','price':'0.528元','pe':'PE-TTM约30倍','pb':'—','perc':'近5年16.48%~19.53%分位','premium':'折价0.28%（无溢价）','flow':'近15-16日净流入约1.84亿，7月小幅净赎回','ytd':'-9.90%'},
    '159549': {'name':'红利低波ETF天弘','track':'中证红利低波100指数','manager':'沙川','size':'62.58亿','nav':'1.2344元','price':'1.214元','pe':'PE-TTM 8.94倍','pb':'PB 0.86~0.90（破净）','perc':'PE近1年30.71%、PB近1年18.6%~38.84%','premium':'折价1.65%（无溢价）','flow':'近30日净流入约4.00亿','ytd':'+3.07%'},
    '515010': {'name':'证券ETF华夏','track':'中证全指证券公司指数','manager':'—','size':'26.92亿','nav':'1.2740元','price':'1.274元','pe':'PE-TTM约14倍','pb':'PB约1.19倍','perc':'PE 3/5年0%分位、PB近10年6%分位','premium':'溢价0.00%（无溢价）','flow':'4月以来ETF持续净流入，7/1板块主力净流入80亿+','ytd':'-8.21%'},
    '159841': {'name':'证券ETF天弘','track':'证券公司指数','manager':'—','size':'120.26亿','nav':'1.0040元','price':'1.004元','pe':'PE 10年分位25.73%','pb':'PB分位47.30%','perc':'PE分位25.73%（中低分位）','premium':'溢价≈0%（无溢价）','flow':'—','ytd':'-8.61%'},
    '159605': {'name':'中概互联ETF广发','track':'中证海外中国互联网30','manager':'—','size':'35.05亿','nav':'0.8562元','price':'0.856元','pe':'PE-TTM约15-16.6倍','pb':'—','perc':'近1年1.5%~11.7%分位','premium':'溢价约-0.02%（无溢价）','flow':'近1周净赎回1.83亿（约5.2%），资金流出信号','ytd':'-21.09%'},
    '512800': {'name':'银行ETF华宝','track':'中证银行指数','manager':'—','size':'110.74亿','nav':'0.8405元','price':'0.819元','pe':'PE分位84.82%（偏高）','pb':'PB 0.68倍','perc':'PB 37.54%分位','premium':'溢价约-0.06%（基本平价）','flow':'份额自2023年7月62.8亿份持续增长','ytd':'+2.00%'},
    '515290': {'name':'银行ETF天弘','track':'中证银行指数','manager':'陈瑶','size':'41.55亿','nav':'—','price':'—','pe':'PE分位90.49%（高）','pb':'PB分位43.31%','perc':'估值分位显著偏高','premium':'溢价率0.17%（低溢价）','flow':'7/30风格策略ETF净流出17.78亿','ytd':'+50.93%'},
}

# 六维评分用于雷达图
dims_order = ['估值水平','行业前景','经理能力','持仓结构','风险收益比','流动性']
weights = {'估值水平':0.20,'行业前景':0.20,'经理能力':0.12,'持仓结构':0.13,'风险收益比':0.25,'流动性':0.10}

def radar_points(code):
    s = merged[code]['scores']
    return [s.get(d,0) for d in dims_order]

# 生成每基金卡片
def fund_card(code):
    m = merged[code]
    meta = funds_meta[code]
    scores = m['scores']
    dims = m['dims']
    supports = m.get('supports',[])
    risks = m.get('risks',[])
    verdict = m['verdict']
    vcolor = {'建议买入':'#e74c3c','谨慎买入':'#f39c12','不建议买入':'#95a5a6'}.get(verdict,'#f39c12')
    vtrap = m.get('value_trap_note','')
    html = f'''
    <div class="fund-card" id="fund-{code}">
      <div class="fund-head">
        <span class="fund-code">{code}</span>
        <h3>{meta['name']}</h3>
        <span class="fund-verdict" style="background:{vcolor}">{verdict}</span>
        <span class="fund-total">总分 <b>{m['total']:.2f}</b>/10</span>
      </div>
      <div class="fund-meta">
        <table class="meta-table">
          <tr><td>跟踪指数</td><td>{meta['track']}</td><td>YTD涨幅</td><td class="{ 'warn' if m.get('ytd_return','').replace('%','').replace('+','').split('（')[0]!='' and is_over30(m) else ''}"><b>{m['ytd_return']}</b></td></tr>
          <tr><td>基金规模</td><td>{meta['size']}</td><td>溢价率</td><td>{meta['premium']}</td></tr>
          <tr><td>PE/PB</td><td>{meta['pe']} / {meta['pb']}</td><td>估值分位</td><td>{meta['perc']}</td></tr>
          <tr><td>资金流向</td><td colspan="3">{meta['flow']}</td></tr>
        </table>
      </div>
      <div class="score-grid">
        {''.join(f'<div class="score-item"><span class="score-label">{d}</span><div class="score-bar"><div class="score-fill" style="width:{scores[d]*10}%"></div></div><span class="score-num">{scores[d]}</span></div>' for d in dims_order)}
      </div>
      <div class="dim-text">
        {''.join(f'<p><b>{d}（{int(weights[d]*100)}%）</b>：{dims.get(d,"—")}</p>' for d in dims_order)}
      </div>
      <div class="support-risk">
        <div class="supports"><b>✅ 支撑因素</b><ul>{''.join(f'<li>{s}</li>' for s in supports)}</ul></div>
        <div class="risks"><b>⚠️ 风险因素</b><ul>{''.join(f'<li>{r}</li>' for r in risks)}</ul></div>
      </div>
      <div class="vtrap"><b>🔍 估值陷阱核查</b>：{vtrap if vtrap else '未标记'}</div>
      <p class="verdict-text"><b>结论</b>：{m['verdict_text']}</p>
    </div>'''
    return html

def is_over30(m):
    ytd = m.get('ytd_return','')
    try:
        num = float(ytd.replace('%','').replace('+','').split('（')[0])
        return num > 30
    except:
        return False

# 对比表行
def cmp_row(code):
    m = merged[code]
    meta = funds_meta[code]
    s = m['scores']
    return f'''<tr><td>{code}</td><td>{meta['name']}</td><td>{meta['track']}</td><td>{m['ytd_return']}</td><td>{meta['premium']}</td><td>{s['估值水平']}</td><td>{s['风险收益比']}</td><td>{m['total']:.2f}</td><td>{m['verdict']}</td><td>neodata</td></tr>'''

cards = ''.join(fund_card(c) for c in order)
rows = ''.join(cmp_row(c) for c in order)

# 图表数据
labels_js = json.dumps([funds_meta[c]['name'] for c in order])
totals_js = json.dumps([merged[c]['total'] for c in order])
radar_labels = json.dumps(dims_order)
radar_data = json.dumps({c: radar_points(c) for c in order})

today = '2026-07-31'
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>基金低估筛选报告 · {today} 盘中</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  :root {{ --primary:#2c3e50; --accent:#1a7f37; --warn:#d4a72c; --danger:#d64545; --bg:#f6f8fa; --card:#ffffff; --text:#1f2937; --muted:#6b7280; --border:#e5e7eb; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }}
  .container {{ max-width:1100px; margin:0 auto; padding:24px 20px 80px; }}
  header.hero {{ background:linear-gradient(135deg,#1a365d 0%,#2b6cb0 100%); color:#fff; padding:32px 36px; border-radius:16px; margin-bottom:28px; box-shadow:0 8px 24px rgba(26,54,93,.25); }}
  header.hero h1 {{ font-size:28px; margin-bottom:8px; }}
  header.hero .sub {{ opacity:.85; font-size:15px; }}
  .badges {{ display:flex; gap:10px; margin-top:14px; flex-wrap:wrap; }}
  .badge {{ background:rgba(255,255,255,.18); border:1px solid rgba(255,255,255,.3); padding:6px 14px; border-radius:20px; font-size:13px; }}
  .section {{ background:var(--card); border-radius:14px; padding:26px 30px; margin-bottom:26px; box-shadow:0 1px 4px rgba(0,0,0,.06); }}
  .section h2 {{ font-size:20px; margin-bottom:18px; color:var(--primary); border-left:4px solid var(--accent); padding-left:12px; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th,td {{ padding:10px 12px; border-bottom:1px solid var(--border); text-align:left; }}
  th {{ background:#f3f4f6; font-weight:600; white-space:nowrap; }}
  tr:hover td {{ background:#fafbfc; }}
  .market-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; }}
  .market-box {{ border:1px solid var(--border); border-radius:10px; padding:16px; background:#fafbfc; }}
  .market-box h4 {{ font-size:14px; color:var(--muted); margin-bottom:8px; }}
  .mkt-row {{ display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px dashed var(--border); font-size:14px; }}
  .mkt-row:last-child {{ border:none; }}
  .up {{ color:var(--danger); font-weight:600; }}
  .down {{ color:var(--accent); font-weight:600; }}
  .events {{ list-style:none; }}
  .events li {{ padding:8px 0 8px 24px; position:relative; font-size:14px; border-bottom:1px dashed var(--border); }}
  .events li::before {{ content:"▸"; position:absolute; left:4px; color:var(--accent); }}
  .events li:last-child {{ border:none; }}
  .chart-wrap {{ position:relative; height:380px; margin:10px 0; }}
  .two-col {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }}
  @media (max-width:800px) {{ .two-col {{ grid-template-columns:1fr; }} }}
  .fund-card {{ border:1px solid var(--border); border-radius:12px; padding:22px 26px; margin-bottom:22px; background:#fff; }}
  .fund-head {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:14px; }}
  .fund-code {{ background:#eef2f7; color:#4a5568; padding:4px 10px; border-radius:6px; font-weight:700; font-size:13px; }}
  .fund-head h3 {{ font-size:18px; }}
  .fund-verdict {{ color:#fff; padding:4px 12px; border-radius:16px; font-size:13px; font-weight:600; }}
  .fund-total {{ margin-left:auto; font-size:14px; color:var(--muted); }}
  .fund-total b {{ font-size:18px; color:var(--primary); }}
  .meta-table td {{ padding:6px 10px; font-size:13.5px; }}
  .meta-table td:first-child {{ color:var(--muted); white-space:nowrap; width:80px; }}
  .warn {{ color:var(--danger); font-weight:700; }}
  .score-grid {{ display:grid; grid-template-columns:repeat(6,1fr); gap:8px; margin:12px 0 16px; }}
  @media (max-width:700px) {{ .score-grid {{ grid-template-columns:repeat(3,1fr); }} }}
  .score-item {{ text-align:center; }}
  .score-label {{ font-size:12px; color:var(--muted); display:block; margin-bottom:4px; }}
  .score-bar {{ height:6px; background:#edf2f7; border-radius:3px; overflow:hidden; }}
  .score-fill {{ height:100%; background:linear-gradient(90deg,#38a169,#2f855a); border-radius:3px; }}
  .score-num {{ font-size:13px; font-weight:700; }}
  .dim-text p {{ font-size:13.5px; margin:6px 0; color:#374151; }}
  .support-risk {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:14px 0; }}
  @media (max-width:700px) {{ .support-risk {{ grid-template-columns:1fr; }} }}
  .supports,.risks {{ background:#f9fafb; border-radius:8px; padding:12px 16px; font-size:13.5px; }}
  .supports ul,.risks ul {{ margin:8px 0 0 18px; }}
  .supports li,.risks li {{ margin:4px 0; }}
  .vtrap {{ background:#fffbeb; border:1px solid #fde68a; border-radius:8px; padding:10px 14px; font-size:13px; color:#92400e; margin:12px 0; }}
  .verdict-text {{ font-size:14px; color:#374151; background:#f0fdf4; border-radius:8px; padding:12px 16px; }}
  .footer-note {{ color:var(--muted); font-size:13px; padding:20px 0; text-align:center; }}
  .disclaimer {{ background:#fef2f2; border:1px solid #fecaca; color:#991b1b; border-radius:10px; padding:16px 20px; font-size:13px; margin-top:20px; }}
  .data-source {{ font-size:12.5px; color:var(--muted); margin-top:8px; }}
  @media print {{ .fund-card {{ break-inside:avoid; }} }}
</style>
</head>
<body>
<div class="container">
  <header class="hero">
    <h1>📊 基金低估筛选 · Multi-Agent 深度分析报告</h1>
    <div class="sub">{today} 盘中（10:11 数据快照）· 50+只海选 → Top 10 · 每基金独立 Agent + neodata 实时数据</div>
    <div class="badges">
      <span class="badge">🕐 {today} 盘中</span>
      <span class="badge">🔍 海选 50+ 只低估基金</span>
      <span class="badge">🤖 10 只独立分析 Agent</span>
      <span class="badge">📡 数据源: neodata</span>
      <span class="badge">🛡️ 估值陷阱检查: YTD/溢价/资金流</span>
    </div>
  </header>

  <div class="section">
    <h2>🌍 市场行情快照</h2>
    <div class="market-grid">
      <div class="market-box">
        <h4>🇨🇳 A股（盘中 10:18）</h4>
        {"".join(f'<div class="mkt-row"><span>{r["name"]}</span><span class="up">{r["chg"]}</span></div><div class="data-source">{r["value"]} · {r["note"]}</div>' for r in market["a_share"])}
      </div>
      <div class="market-box">
        <h4>🇭🇰 港股（盘中 10:19）</h4>
        {"".join(f'<div class="mkt-row"><span>{r["name"]}</span><span class="{ "up" if "+" in r["chg"] else "down"}">{r["chg"]}</span></div><div class="data-source">{r["value"]} · {r["note"]}</div>' for r in market["hk"])}
      </div>
      <div class="market-box">
        <h4>🇺🇸 隔夜美股</h4>
        {"".join(f'<div class="mkt-row"><span>{r["name"]}</span><span class="up">{r["chg"]}</span></div><div class="data-source">{r["note"]}</div>' for r in market["us"])}
      </div>
    </div>
    <h3 style="margin-top:18px;font-size:15px;color:var(--muted);">📰 当日关键催化事件</h3>
    <ul class="events">
      {"".join(f'<li>{e}</li>' for e in market["events"])}
    </ul>
    <p class="data-source">行情来源：WebSearch 实时采集（2026-07-31 10:18 数据快照），仅供参考。</p>
  </div>

  <div class="section">
    <h2>🔎 基金海选说明</h2>
    <p style="font-size:14px;color:#374151;">专用海选 Agent（fund-screener）通过 <b>天天基金、雪球、平安基金/证券 + 行业全覆盖 + WeStock 补充</b> 等 5+ 渠道搜索 50+ 只 PE 历史分位 &lt;20%（或 PB 破净+高股息豁免）的低估基金，按规模取 Top 10。</p>
    <p style="font-size:14px;color:#374151;margin-top:8px;"><b>🔴 反指标检查（PE 分位低 ≠ 低估）</b>：每只候选检查 ①YTD 涨幅&gt;30%（盈利暴增型低PE）②溢价率&gt;5% ③近5日资金净流出&gt;5% ④PE&lt;15 且 ROE&gt;20%。海选标记 3 只候选（513690 溢价/ROE、159605 资金流出、券商类盈利暴增），均已在独立 Agent 分析中核实修正。</p>
  </div>

  <div class="section">
    <h2>📋 基金筛选对比表（数据来源：neodata）</h2>
    <div style="overflow-x:auto;">
    <table>
      <thead><tr><th>代码</th><th>名称</th><th>跟踪指数</th><th>YTD</th><th>溢价率</th><th>估值分</th><th>风险收益分</th><th>总分</th><th>评级</th><th>数据源</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    </div>
  </div>

  <div class="section">
    <h2>📊 Multi-Agent 评分总览</h2>
    <div class="chart-wrap"><canvas id="totalChart"></canvas></div>
    <div class="chart-wrap"><canvas id="radarChart"></canvas></div>
  </div>

  <div class="section">
    <h2>🔍 每只基金详细分析（独立 Agent + neodata 实时数据）</h2>
    {cards}
  </div>

  <div class="section">
    <h2>📌 结论汇总</h2>
    <table>
      <thead><tr><th>排名</th><th>基金</th><th>总分</th><th>评级</th><th>核心逻辑</th></tr></thead>
      <tbody>
        <tr><td>🥇 1</td><td>512170 医疗ETF华宝</td><td>7.92</td><td>谨慎买入</td><td>真低估（YTD -4.51% + 分位20.86%），基药目录纳入创新药、出海1100亿美元，龙头规模257亿</td></tr>
        <tr><td>🥈 2</td><td>513050 中概互联网ETF易方达</td><td>7.89</td><td>谨慎买入</td><td>PE-TTM 16倍/2.53%分位历史极低，折价0.32%，资金近1年净流入129.7亿，AI商业化驱动</td></tr>
        <tr><td>🥉 3</td><td>513690 港股红利ETF博时</td><td>7.79</td><td>谨慎买入</td><td>PE 7.16倍/5%分位+股息率5.26%，无溢价；航运周期股盈利下行含陷阱属性，分批建仓</td></tr>
        <tr><td>4</td><td>513060 恒生医疗ETF博时</td><td>7.74</td><td>谨慎买入</td><td>PE分位16.5%-19.5%真低估，创新药BD超1000亿美元，7月已反弹30%有回吐压力</td></tr>
        <tr><td>5</td><td>159549 红利低波ETF天弘</td><td>7.68</td><td>谨慎买入</td><td>PB 0.86-0.90破净+股息率4.31%，折价1.65%，近30日净流入4亿，防御型配置</td></tr>
        <tr><td>6</td><td>515010 证券ETF华夏</td><td>7.52</td><td>谨慎买入</td><td>PE 14倍/0%分位+PB 1.19倍/6%分位真低估，盈利暴增+股价下跌剪刀差，成交+58%</td></tr>
        <tr><td>7</td><td>159841 证券ETF天弘</td><td>7.36</td><td>谨慎买入</td><td>PE分位25.73%中低，印花税+97.3%行业景气，规模120亿流动性佳</td></tr>
        <tr><td>8</td><td>159605 中概互联ETF广发</td><td>7.12</td><td>谨慎买入</td><td>PE分位1.5%-11.7%真低估，但近1周净赎回5.2%资金流出信号，结构性分化</td></tr>
        <tr><td>9</td><td>512800 银行ETF华宝</td><td>6.80</td><td>谨慎买入</td><td>PB 0.68倍+股息率4.24%，但PE分位84.82%偏高，7月急涨14.8%后回调压力（五大行跌3%）</td></tr>
        <tr><td>10</td><td>515290 银行ETF天弘</td><td>5.63</td><td>谨慎买入</td><td>⚠️ YTD +50.93% 严重超涨（估值仅3分），PE分位90.49%透支，仅建议回调后定投</td></tr>
      </tbody>
    </table>
    <p style="margin-top:14px;font-size:14px;color:#374151;"><b>综合判断</b>：今日市场呈现<b>科技强反弹 + 资金轮动</b>格局（创业板+5.13%），低估榜以<b>医药、中概、红利、券商</b>为主。Top 5 均为"真低估"（YTD 温和或为负 + 历史低分位），可优先关注；<b>515290 银行ETF天弘 YTD+50.93% 属典型"超涨型"标的</b>，估值评分仅 3 分，追高风险大，报告已如实降级标注。全部评级以"谨慎买入/分批建仓"为主基调，防范短期波动。</p>
  </div>

  <div class="section">
    <h2>📡 数据来源与说明</h2>
    <p style="font-size:14px;">本次报告所有基金数据均由 <b>10 只独立 Agent 通过 neodata-financial-search 实时查询获取</b>（每只基金 6-12 条查询，全部含 <code>"code":"200"</code> 原始 JSON 输出），市场行情由 WebSearch 实时采集。原始证据文件保存在 <code>deliverables/fund-analysis/</code> 目录（每只基金一个 MD 文件），主助理已逐一读取校验。</p>
    <p style="font-size:13px;color:var(--muted);margin-top:6px;">估值陷阱核查：每只基金均检查 YTD 涨幅、溢价率、资金流向三项反指标，515290（YTD+50.93%）已降级至 5.63 分，159605（净赎回5.2%）已在风险中标注。</p>
  </div>

  <div class="disclaimer">⚠️ <b>免责声明</b>：本报告由 AI 基于公开数据自动生成，仅供研究参考，<b>不构成任何投资建议</b>。基金有风险，投资需谨慎。过往业绩不代表未来表现，请结合自身风险承受能力独立决策。</div>
  <div class="footer-note">Generated by WorkBuddy · 基金低估筛选 Multi-Agent 工作流 · {today} 盘中</div>
</div>

<script>
const labels = {labels_js};
const totals = {totals_js};
new Chart(document.getElementById('totalChart'), {{
  type: 'bar',
  data: {{
    labels: labels,
    datasets: [{{
      label: '综合评分 (总分10)',
      data: totals,
      backgroundColor: totals.map(t => t >= 7.5 ? 'rgba(47,133,90,.85)' : t >= 6.5 ? 'rgba(212,167,44,.85)' : 'rgba(214,69,69,.85)'),
      borderRadius: 6
    }}]
  }},
  options: {{
    indexAxis: 'y',
    responsive: true, maintainAspectRatio: false,
    scales: {{ x: {{ min: 0, max: 10, title: {{ display:true, text:'综合评分' }} }} }},
    plugins: {{ legend: {{ display:false }} }}
  }}
}});

const radarLabels = {radar_labels};
const radarData = {radar_data};
const colors = ['#2b6cb0','#38a169','#d69e2e','#e53e3e','#805ad5','#dd6b20','#3182ce','#b83280','#2c7a7b','#975a16'];
new Chart(document.getElementById('radarChart'), {{
  type: 'radar',
  data: {{
    labels: radarLabels,
    datasets: labels.map((name, i) => ({{
      label: name,
      data: radarData[Object.keys(radarData)[i]],
      borderColor: colors[i % colors.length],
      backgroundColor: colors[i % colors.length] + '22',
      borderWidth: 2,
      pointRadius: 3
    }}))
  }},
  options: {{
    responsive: true, maintainAspectRatio: false,
    scales: {{ r: {{ min: 0, max: 10, ticks: {{ stepSize: 2 }} }} }},
    plugins: {{ legend: {{ position: 'right', labels: {{ font: {{ size: 11 }} }} }} }}
  }}
}});
</script>
</body>
</html>'''

out = f'fund-report-{today}-盘中.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'已生成 {out} ({len(html)} bytes)')
