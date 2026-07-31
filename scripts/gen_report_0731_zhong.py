#!/usr/bin/env python3
"""Generate fund report HTML for 2026-07-31 盘中 (Multi-Agent · neodata + MD证据)."""
import json, html

WORKDIR = "/Users/yangjipeng/WorkBuddy/automation-2026-07-07-10-48-40"
scores = json.load(open(f"{WORKDIR}/deliverables/fund-analysis/merged-scores-0731-zhong.json", encoding="utf-8"))
funds = sorted(scores, key=lambda x: x["total"], reverse=True)

# 市场行情快照（2026-07-31 盘中 10:20 采集）
market = {
    "title": "2026-07-31 盘中 10:20",
    "a_share": [
        {"name": "上证指数", "value": "3,840.29", "chg": "+0.94%", "color": "#dc2626"},
        {"name": "深证成指", "value": "13,758.51", "chg": "+3.56%", "color": "#dc2626"},
        {"name": "创业板指", "value": "3,426.63", "chg": "+5.61%", "color": "#dc2626"},
    ],
    "hk": [
        {"name": "恒生指数", "value": "25,793.30", "chg": "-0.25%", "color": "#16a34a"},
        {"name": "恒生科技", "value": "4,833.62", "chg": "+0.62%", "color": "#dc2626"},
    ],
    "us": "英伟达创单日市值纪录（+4400亿美元）；苹果Q3营收1094.2亿美元(+16%)但指引不及预期盘后跌超8%；三星电子Q2营业利润89.5万亿韩元(+1814%)创新高，存储涨价周期延续",
    "news": "① 创指涨超6%、科创50涨超8%，半导体/存储/CPO/PCB集体反弹，两市超4300只个股上涨；② 银行、保险、油气板块逆势回调，五大行跌超4%，白酒板块回调；③ 商务部就美将电力逆变器、先进机器人列入『覆盖清单』回应：敦促撤销，必要时坚决反制；④ 三新经济增加值25.79万亿(+6.2%)，占GDP 18.39%；⑤ 二季度宏观杠杆率降至308.2%，2022年以来首次单季下降；⑥ 7/30 A股大跌(沪指-0.62%)后今日科技股强反弹，大金融/消费前期抗跌品种今日调整"
}

DIMS = ["估值水平", "行业前景", "经理能力", "持仓结构", "风险收益比", "流动性"]

# 综合评分（五维 → 技术/基本/新闻/情绪/风险 折算）
def dims_to_five(f):
    s = f["scores"]
    return {
        "基本面": min(10, round(s["估值水平"]*0.4 + s["行业前景"]*0.35 + s["持仓结构"]*0.25, 1)),
        "估值": s["估值水平"],
        "行业": s["行业前景"],
        "资金面": min(10, round(s["流动性"]*0.5 + s["风险收益比"]*0.5, 1)),
        "风险调整": min(10, round(s["风险收益比"], 1)),
    }

def esc(t):
    return html.escape(str(t))

# ============ 构建JS数据 ============
codes = [f["code"] for f in funds]
names = [f["name"] for f in funds]
totals = [f["total"] for f in funds]
bar_colors = ["#f59e0b","#94a3b8","#d97706","#3b82f6","#8b5cf6","#ec4899","#14b8a6","#f97316","#6366f1","#84cc16"]
radar_top3 = [[f["scores"].get(d,7) for d in DIMS] for f in funds[:3]]
radar_top3_labels = [f"{f['code']} {f['name']}" for f in funds[:3]]
scatter = [{"x": f["scores"]["估值水平"], "y": f["scores"]["风险收益比"], "code": f["code"]} for f in funds]

# ============ HTML 构建 ============
def make_rank_table():
    rows = ""
    for i, f in enumerate(funds):
        s = f["scores"]
        medal = ["🥇","🥈","🥉"][i] if i < 3 else f"{i+1}"
        ytd = str(f["ytd_return"]).replace("%","")
        ytd_color = "#16a34a" if ytd.startswith("+") else "#dc2626"
        badge = {"建议买入": "buy", "谨慎买入": "watch"}.get(f["verdict"], "hold")
        rows += f"""<tr>
        <td>{medal}</td><td><b>{esc(f['code'])}</b><br><small>{esc(f['name'])}</small></td>
        <td style="color:{ytd_color};font-weight:600">{esc(f['ytd_return'])}</td>
        <td>{esc(f['premium_rate'])}</td>
        <td>{s['估值水平']} / {s['行业前景']} / {s['经理能力']} / {s['持仓结构']} / {s['风险收益比']} / {s['流动性']}</td>
        <td style="font-weight:800">{f['total']:.2f}</td>
        <td><span class="badge {badge}">{esc(f['verdict'])}</span></td></tr>"""
    return rows

def make_fund_cards():
    cards = ""
    for i, f in enumerate(funds):
        s = f["scores"]
        dims_html = ""
        for d in DIMS:
            v = s[d]
            pct = v / 10 * 100
            dims_html += f"""<div class="dim-row"><span class="dim-name">{d}</span><div class="dim-bar"><div class="dim-fill" style="width:{pct}%"></div></div><span class="dim-val">{v}</span></div>"""
        supports = "".join(f"<li>✅ {esc(x)}</li>" for x in f["supports"])
        risks = "".join(f"<li>⚠️ {esc(x)}</li>" for x in f["risks"])
        ytd_color = "#16a34a" if str(f["ytd_return"]).startswith("+") else "#dc2626"
        badge = {"建议买入": "buy", "谨慎买入": "watch"}.get(f["verdict"], "hold")
        trap = f"<div class='trap-note'><b>估值陷阱核查：</b>{esc(f['value_trap_note'])}</div>" if f.get("value_trap_note") else ""
        cards += f"""<div class="fund-card" id="card-{esc(f['code'])}">
        <div class="fund-head">
            <div><span class="rank-badge">#{i+1}</span><b style="font-size:17px">{esc(f['name'])}</b> <span class="code-chip">{esc(f['code'])}</span></div>
            <div class="fund-total">总分 <span style="font-size:28px;color:#1d4ed8">{f['total']:.2f}</span><br><span class="badge {badge}">{esc(f['verdict'])}</span></div>
        </div>
        <div class="fund-meta">
            <span>YTD：<b style="color:{ytd_color}">{esc(f['ytd_return'])}</b></span>
            <span>溢价率：{esc(f['premium_rate'])}</span>
            <span>资金：{esc(f['fund_flow'][:40])}{'…' if len(f['fund_flow'])>40 else ''}</span>
        </div>
        {trap}
        <div class="dims">{dims_html}</div>
        <div class="fund-grid">
            <div class="support-col"><h4>支撑因素</h4><ul>{supports}</ul></div>
            <div class="risk-col"><h4>风险因素</h4><ul>{risks}</ul></div>
        </div>
        <details><summary>查看详细结论</summary><p class="verdict-text">{esc(f['verdict_text'])}</p></details>
        </div>"""
    return cards

def make_market_snapshot():
    a = "".join(f"<div class='idx'><div class='idx-name'>{m['name']}</div><div class='idx-val'>{m['value']}</div><div class='idx-chg' style='color:{m['color']}'>{m['chg']}</div></div>" for m in market["a_share"])
    h = "".join(f"<div class='idx'><div class='idx-name'>{m['name']}</div><div class='idx-val'>{m['value']}</div><div class='idx-chg' style='color:{m['color']}'>{m['chg']}</div></div>" for m in market["hk"])
    return f"""
    <div class="chart-card">
        <h2>📊 市场行情快照 <span class="time-tag">{market['title']}</span></h2>
        <h3 style="margin:6px 0 4px">🇨🇳 A股（盘中）</h3>
        <div class="idx-grid">{a}</div>
        <h3 style="margin:10px 0 4px">🇭🇰 港股（盘中）</h3>
        <div class="idx-grid">{h}</div>
        <h3 style="margin:10px 0 4px">🇺🇸 隔夜美股 / 重要事件</h3>
        <p style="margin:4px 0;font-size:13.5px;color:#374151">{market['us']}</p>
        <p style="margin:6px 0 0;font-size:13px;color:#6b7280">{market['news']}</p>
    </div>"""

# ============ 最终HTML ============
html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>基金低估筛选报告 · 2026-07-31 盘中</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  body {{ font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; max-width: 1100px; margin: 0 auto; padding: 24px; background: #f7f8fa; color: #1f2937; }}
  h1 {{ font-size: 24px; margin: 0 0 4px; }}
  .subtitle {{ color: #6b7280; font-size: 14px; margin-bottom: 20px; }}
  .chart-card {{ background: #fff; padding: 20px 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,.06); }}
  .chart-card h2 {{ margin: 0 0 12px; font-size: 18px; }}
  .time-tag {{ background: #1d4ed8; color: #fff; font-size: 12px; padding: 2px 8px; border-radius: 10px; vertical-align: middle; }}
  .idx-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; }}
  .idx {{ background: #f3f4f6; border-radius: 8px; padding: 10px 12px; text-align: center; }}
  .idx-name {{ font-size: 12.5px; color: #6b7280; }}
  .idx-val {{ font-size: 17px; font-weight: 700; }}
  .idx-chg {{ font-size: 13.5px; font-weight: 600; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th {{ background: #f3f4f6; text-align: left; padding: 8px; border-bottom: 2px solid #e5e7eb; }}
  td {{ padding: 8px; border-bottom: 1px solid #f3f4f6; vertical-align: middle; }}
  .badge {{ display: inline-block; padding: 2px 10px; border-radius: 10px; font-size: 12px; font-weight: 700; color: #fff; }}
  .badge.buy {{ background: #16a34a; }}
  .badge.watch {{ background: #f59e0b; }}
  .badge.hold {{ background: #6b7280; }}
  .fund-card {{ background: #fff; border-radius: 12px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,.06); border-left: 4px solid #1d4ed8; }}
  .fund-head {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
  .rank-badge {{ background: #1d4ed8; color: #fff; border-radius: 6px; padding: 2px 8px; font-size: 13px; margin-right: 6px; }}
  .code-chip {{ background: #e0e7ff; color: #3730a3; border-radius: 6px; padding: 2px 8px; font-size: 12.5px; }}
  .fund-total {{ text-align: right; line-height: 1.3; }}
  .fund-meta {{ display: flex; gap: 18px; flex-wrap: wrap; font-size: 13px; color: #374151; margin-bottom: 10px; }}
  .trap-note {{ background: #fef3c7; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #92400e; margin-bottom: 10px; }}
  .dims {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 6px 14px; margin-bottom: 12px; }}
  .dim-row {{ display: flex; align-items: center; gap: 6px; font-size: 12px; }}
  .dim-name {{ width: 58px; color: #6b7280; }}
  .dim-bar {{ flex: 1; background: #f3f4f6; border-radius: 4px; height: 8px; }}
  .dim-fill {{ background: linear-gradient(90deg,#3b82f6,#1d4ed8); height: 8px; border-radius: 4px; }}
  .dim-val {{ width: 18px; font-weight: 700; text-align: right; }}
  .fund-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }}
  @media (max-width: 700px) {{ .fund-grid {{ grid-template-columns: 1fr; }} }}
  .support-col h4 {{ color: #16a34a; margin: 6px 0; font-size: 13.5px; }}
  .risk-col h4 {{ color: #dc2626; margin: 6px 0; font-size: 13.5px; }}
  ul {{ margin: 0; padding-left: 16px; }}
  li {{ font-size: 12.5px; margin-bottom: 3px; color: #374151; }}
  .verdict-text {{ font-size: 13px; color: #374151; line-height: 1.6; }}
  details {{ margin-top: 8px; }}
  summary {{ cursor: pointer; color: #1d4ed8; font-size: 13px; font-weight: 600; }}
  .disclaimer {{ color: #6b7280; font-size: 12.5px; padding: 16px 0; border-top: 1px solid #e5e7eb; margin-top: 24px; }}
  .src-note {{ font-size: 12px; color: #6b7280; margin-top: 8px; }}
  .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
  @media (max-width: 800px) {{ .grid-2 {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<h1>📈 低估基金筛选报告 <span class="time-tag">2026-07-31 盘中 10:00</span></h1>
<div class="subtitle">Multi-Agent 并行分析 · 50+只海选 → Top10 · 数据源：neodata-financial-search + MD证据校验 · 生成时间：2026-07-31 10:30 (CST)</div>

{make_market_snapshot()}

<div class="chart-card">
    <h2>🛰️ 海选说明</h2>
    <p style="font-size:13px;color:#374151;margin:0">
    专用海选Agent通过 <b>6个渠道方向、13+组关键词</b>（天天基金/雪球/平安证券/新时空/每经/界面 + neodata交叉验证）实时搜索 <b>50+只候选基金</b>，
    覆盖中概互联、恒生科技、白酒/食品饮料、医药/医疗、消费、红利、证券/银行等主流赛道，按资金规模取 Top 10。<br>
    🔴 <b>反指标检查（2026-07-28热修复）</b>：全部基金 YTD &lt; 30%（无"盈利暴增型低PE"），溢价率均 &lt; 5%（多为折价/平价），资金多为净流入；
    513180 恒生科技因 PE 贴近 15 倍临界已标注⚠️观察并经 neodata 独立核实（PE-TTM 约23倍，风险未坐实）。
    </p>
</div>

<div class="chart-card">
    <h2>📋 基金筛选对比表 <span style="font-size:12px;color:#6b7280">（数据来源：neodata）</span></h2>
    <table>
        <tr><th>排名</th><th>基金</th><th>YTD</th><th>溢价率</th><th>六维评分(估/行/经/持/风/流)</th><th>总分</th><th>结论</th></tr>
        {make_rank_table()}
    </table>
    <div class="src-note">六维评分：估值水平 / 行业前景 / 经理能力 / 持仓结构 / 风险收益比 / 流动性（各10分制）</div>
</div>

<div class="chart-card">
    <h2>📊 Multi-Agent 评分总览</h2>
    <div class="grid-2">
        <div><canvas id="barChart" height="280"></canvas></div>
        <div><canvas id="radarChart" height="280"></canvas></div>
    </div>
    <div class="src-note">左：Top10 综合总分柱状图（满分10）｜右：Top3 六维雷达对比</div>
</div>

<div class="chart-card">
    <h2>🎯 结论汇总</h2>
    <div style="font-size:13.5px;line-height:1.7;color:#374151">
    <p>🥇 <b>证券ETF国泰(512880) 8.68分 — 建议买入</b>：真低估（PE近3年10%分位/近十年4.69%）+ 行业高景气（42家券商H1净利预增50%）+ 政策资金共振（国家队增持600亿+、中金"三合一"并购获受理），溢价率≈0%，为当前评分最高标的。</p>
    <p>🥈 <b>红利ETF华泰柏瑞(510880) 8.01分 — 建议买入</b>：PB 0.73深度破净 + 股息率4.8-5% + 股债息差3.6pct历史极值，低利率时代类固收底仓，险资持续增配。</p>
    <p>🥉 <b>医疗ETF华宝(512170) 7.92分 — 谨慎买入</b>：PE近10年约10%分位真低估，创新药获批38个+BD出海约1100亿美元+CXO业绩兑现，行业拐点初期，建议左侧分批。</p>
    <p>📌 港股互联网/科技类（513180/159792/513050/513330）普遍处于近5-10年极低分位 + YTD深跌20-27%，AI商业化+南向资金回流构成修复主线，但波动极大、底部反转未确认，均建议<b>谨慎买入、分批逢低</b>，以8月中报为验证节点。</p>
    <p>📌 消费/酒类（159928/512690）处于十年估值大底（PE分位约9%），茅台两次提价+消费"十五五"规划催化，但白酒价格指数连续6个月下行、基本面反转待中报验证，建议分批左侧布局。</p>
    </div>
</div>

<h2 style="font-size:19px;margin:20px 0 12px">🔍 单基金详细分析（10只）</h2>
{make_fund_cards()}

<div class="disclaimer">
    ⚠️ <b>免责声明</b>：本报告由 AI 基于公开信息（neodata金融数据服务 + 网络搜索）自动生成，所有评分与结论仅供参考，<b>不构成任何投资建议或基金推荐</b>。基金有风险，投资需谨慎。市场有风险，过往业绩不代表未来表现。数据截至 2026-07-31 盘中，可能存在延迟或误差。
</div>

<script>
const DIMS = {json.dumps(DIMS, ensure_ascii=False)};
// 1. 总分柱状图
new Chart(document.getElementById('barChart'), {{
  type: 'bar',
  data: {{
    labels: {json.dumps([f"{c}\\n{n}" for c,n in zip(codes,names)], ensure_ascii=False)},
    datasets: [{{ label: '综合总分', data: {json.dumps(totals)}, backgroundColor: {json.dumps(bar_colors)}, borderRadius: 6 }}]
  }},
  options: {{ responsive: true, plugins: {{ legend: {{ display: false }}, tooltip: {{ callbacks: {{ title: (i)=>i[0].label.replace('\\n',' ') }} }} }}, scales: {{ y: {{ min: 6, max: 10, title: {{ display: true, text: '总分' }} }} }} }}
}});
// 2. Top3 六维雷达图
new Chart(document.getElementById('radarChart'), {{
  type: 'radar',
  data: {{
    labels: DIMS,
    datasets: {json.dumps([{"label": radar_top3_labels[i], "data": radar_top3[i], "borderColor": c, "backgroundColor": c+"22", "pointRadius": 3} for i,c in enumerate(["#1d4ed8","#16a34a","#f59e0b"])], ensure_ascii=False)}
  }},
  options: {{ responsive: true, scales: {{ r: {{ min: 0, max: 10, ticks: {{ stepSize: 2 }} }} }}, plugins: {{ legend: {{ position: 'bottom' }} }} }}
}});
</script>
</body>
</html>"""

out = f"{WORKDIR}/fund-report-2026-07-31-盘中.html"
open(out, "w", encoding="utf-8").write(html_doc)
print(f"✅ 报告已生成: {out} ({len(html_doc)//1024} KB)")
