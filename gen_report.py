import json

report_data = {
    "date": "2026-07-30",
    "session": "盘后",
    "market": {
        "a_shares": "上证 3804.69 (-0.62%) 深成指 13285.80 (-2.73%) 创业板 3244.62 (-3.97%)",
        "hong_kong": "恒生 25858.88 (+0.20%) 恒生科技 4803.77 (-1.25%)",
        "us": "道指 51594.14 (-2.19%) 标普 7316.15 (-1.52%) 纳指 24442.94 (-1.74%)",
        "events": "消费复苏政策预期升温；白酒银行板块走强；美联储年内第5次维持利率不变(3票反对加息)；中东地缘冲突推高油价；A股回购潮持续升温(7月超500亿)"
    },
    "funds": [
        {"code":"512880","name":"证券ETF国泰","ytd":"-8.68","premium":"-0.12","flow":"近20日净流入50.20亿","trap":"","scores":{"估值水平":7.5,"行业前景":8.0,"经理能力":6.0,"持仓结构":7.0,"风险收益比":7.0,"流动性":9.0},"total":7.38,"verdict":"谨慎买入","size":"630.39","pe":"15.2","pe_percentile":"3.52%分位"},
        {"code":"513050","name":"中概互联网ETF易方达","ytd":"-24.94","premium":"-0.23","flow":"近3日净流入9.05亿","trap":"","scores":{"估值水平":9.0,"行业前景":7.0,"经理能力":7.5,"持仓结构":7.7,"风险收益比":5.6,"流动性":10.0},"total":7.50,"verdict":"谨慎买入","size":"375.92","pe":"16.44","pe_percentile":"10.57%分位"},
        {"code":"513330","name":"恒生互联网ETF华夏","ytd":"-22.02","premium":"-0.42","flow":"近1周规模+9.55亿","trap":"","scores":{"估值水平":8.5,"行业前景":6.5,"经理能力":7.0,"持仓结构":6.5,"风险收益比":5.5,"流动性":9.0},"total":6.80,"verdict":"中性偏多","size":"282.43","pe":"21.73","pe_percentile":"16.67%分位"},
        {"code":"159928","name":"消费ETF汇添富","ytd":"-5.20","premium":"0.10","flow":"近5日净流入4699万","trap":"","scores":{"估值水平":8.0,"行业前景":7.5,"经理能力":7.0,"持仓结构":7.0,"风险收益比":6.0,"流动性":8.5},"total":7.20,"verdict":"谨慎买入","size":"155.12","pe":"20.58","pe_percentile":"12.62%分位"},
        {"code":"512800","name":"银行ETF华宝","ytd":"2.10","premium":"2.49","flow":"近5日主力净流入26.78亿","trap":"PE分位偏高,需注意","scores":{"估值水平":6.0,"行业前景":7.0,"经理能力":7.0,"持仓结构":6.5,"风险收益比":5.0,"流动性":8.0},"total":6.20,"verdict":"中性偏积极","size":"100.00","pe":"6.79","pe_percentile":"PB破净(0.67)"},
        {"code":"513060","name":"恒生医疗ETF博时","ytd":"-7.86","premium":"-2.86","flow":"7月主力博弈激烈","trap":"","scores":{"估值水平":8.5,"行业前景":8.0,"经理能力":7.0,"持仓结构":7.5,"风险收益比":6.8,"流动性":9.0},"total":7.80,"verdict":"买入持有","size":"58.51","pe":"29.52","pe_percentile":"16.48%分位"},
        {"code":"159766","name":"旅游ETF富国","ytd":"-29.73","premium":"0.10","flow":"近5日净流入1.37亿","trap":"盈利压缩型低PE(PE67.81/分位0.56%)","scores":{"估值水平":5.0,"行业前景":8.0,"经理能力":6.5,"持仓结构":6.0,"风险收益比":6.0,"流动性":6.0},"total":6.30,"verdict":"谨慎关注","size":"29.32","pe":"67.81","pe_percentile":"0.56%分位"},
        {"code":"515010","name":"证券ETF华夏","ytd":"-6.50","premium":"-0.05","flow":"近20日净流入5.93亿","trap":"","scores":{"估值水平":8.0,"行业前景":7.5,"经理能力":7.0,"持仓结构":7.0,"风险收益比":6.5,"流动性":8.0},"total":6.80,"verdict":"中性偏多","size":"27.44","pe":"14.83","pe_percentile":"5.28%分位"},
        {"code":"530280","name":"上证180ETF平安","ytd":"-1.73","premium":"-0.11","flow":"近期资金小幅流出","trap":"规模偏小仅3500万","scores":{"估值水平":9.0,"行业前景":6.0,"经理能力":7.0,"持仓结构":7.0,"风险收益比":6.0,"流动性":4.0},"total":6.80,"verdict":"谨慎关注","size":"5.00","pe":"11.77","pe_percentile":"10.57%分位"},
        {"code":"516850","name":"新能源ETF华夏","ytd":"-14.45","premium":"-0.90","flow":"近20日净申购111万","trap":"规模仅1.32亿偏小","scores":{"估值水平":7.5,"行业前景":7.5,"经理能力":7.5,"持仓结构":7.0,"风险收益比":6.0,"流动性":3.5},"total":6.50,"verdict":"谨慎关注","size":"1.32","pe":"34.68","pe_percentile":"0.83%分位"}
    ]
}

# Sort by total score descending
report_data["funds"].sort(key=lambda x: x["total"], reverse=True)

# Pre-compute Python variables for the JS section
radar_labels = list(report_data["funds"][0]["scores"].keys())
fund_names = [f["name"] for f in report_data["funds"]]
fund_codes = [f["code"] for f in report_data["funds"]]
top3_radar = []
for i in range(3):
    top3_radar.append([report_data["funds"][i]["scores"][k] for k in radar_labels])
bar_scores = [f["total"] for f in report_data["funds"]]
bar_colors = []
for f in report_data["funds"]:
    if f["total"] >= 7.0:
        bar_colors.append("#059669")
    elif f["total"] >= 6.5:
        bar_colors.append("#d97706")
    else:
        bar_colors.append("#6b7280")

# Generate HTML
html_parts = []
html_parts.append('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>基金低估筛选报告 - ''' + report_data["date"] + ''' 盘后</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; max-width: 1200px; margin: 0 auto; padding: 24px; background: #f0f2f5; color: #1f2937; }
.header { background: linear-gradient(135deg, #1a365d, #2563eb); color: white; padding: 32px 40px; border-radius: 16px; margin-bottom: 24px; }
.header h1 { font-size: 32px; margin: 0; }
.header .subtitle { font-size: 14px; opacity: 0.8; margin-top: 8px; }
.header .badge { display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 12px; font-size: 13px; margin-top: 12px; }
.market-card { background: linear-gradient(135deg, #1e3a5f, #2d4a7a); color: white; padding: 24px; border-radius: 12px; margin-bottom: 24px; }
.market-card h2 { font-size: 18px; margin-bottom: 12px; }
.market-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
.market-item { background: rgba(255,255,255,0.1); padding: 12px 16px; border-radius: 8px; }
.market-item .region { font-size: 12px; opacity: 0.7; }
.market-item .value { font-size: 20px; font-weight: 700; margin: 4px 0; }
.market-item .change { font-size: 13px; }
.positive { color: #4ade80 !important; }
.negative { color: #f87171 !important; }
.event-bar { background: rgba(255,255,255,0.08); padding: 12px 16px; border-radius: 8px; margin-top: 12px; font-size: 13px; line-height: 1.6; }
.chart-card { background: white; padding: 24px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
.chart-card h2 { font-size: 18px; margin-bottom: 16px; }
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th { background: #f8fafc; padding: 10px 12px; text-align: left; border-bottom: 2px solid #e2e8f0; white-space: nowrap; }
td { padding: 10px 12px; border-bottom: 1px solid #f1f5f9; }
tr:hover { background: #f8fafc; }
.rank-1 { background: #fef3c7; }
.score-bar { height: 6px; border-radius: 3px; background: #e2e8f0; overflow: hidden; }
.score-bar-inner { height: 100%; border-radius: 3px; transition: width 0.5s; }
.verdict-buy { color: #059669; font-weight: 600; }
.verdict-hold { color: #d97706; font-weight: 600; }
.verdict-watch { color: #6b7280; font-weight: 600; }
.trap-warn { color: #dc2626; font-size: 12px; }
.fund-card { background: white; border-radius: 12px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); overflow: hidden; }
.fund-card-header { padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; }
.fund-card-header .left h3 { font-size: 16px; }
.fund-card-header .left .code { font-size: 13px; color: #6b7280; }
.fund-card-header .score { font-size: 24px; font-weight: 700; }
.fund-card-body { padding: 0 20px 16px; }
.detail-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 12px 0; }
.detail-item { background: #f8fafc; padding: 10px 12px; border-radius: 8px; }
.detail-item label { font-size: 11px; color: #6b7280; }
.detail-item .val { font-size: 14px; font-weight: 600; }
canvas { max-width: 100%; }
.disclaimer { color: #6b7280; font-size: 13px; padding: 20px; border-top: 1px solid #e5e7eb; margin-top: 24px; text-align: center; }
</style>
</head>
<body>

<div class="header">
  <h1>📊 基金低估筛选报告</h1>
  <div class="subtitle">''' + report_data["date"] + ''' 盘后 17:00 · 东八区 · 数据来源: NeoData Financial Search</div>
  <div class="badge">Multi-Agent · 50+海选Top10 · 10只并行分析</div>
</div>

<div class="market-card">
  <h2>📈 市场行情快照</h2>
  <div class="market-grid">
    <div class="market-item">
      <div class="region">🇨🇳 A股（7/30收盘）</div>
      <div class="value">沪指 3,804.69</div>
      <div class="change negative">▼ -0.62%</div>
      <div style="margin-top:6px;font-size:13px;">深成指 13,285.80 <span class="negative">▼ -2.73%</span></div>
      <div style="font-size:13px;">创业板 3,244.62 <span class="negative">▼ -3.97%</span></div>
    </div>
    <div class="market-item">
      <div class="region">🇭🇰 港股（7/30收盘）</div>
      <div class="value">恒生 25,858.88</div>
      <div class="change positive">▲ +0.20%</div>
      <div style="margin-top:6px;font-size:13px;">恒生科技 4,803.77 <span class="negative">▼ -1.25%</span></div>
    </div>
    <div class="market-item">
      <div class="region">🇺🇸 美股（7/29收盘）</div>
      <div class="value">道指 51,594.14</div>
      <div class="change negative">▼ -2.19%</div>
      <div style="margin-top:6px;font-size:13px;">标普 7,316.15 <span class="negative">▼ -1.52%</span></div>
      <div style="font-size:13px;">纳指 24,442.94 <span class="negative">▼ -1.74%</span></div>
    </div>
  </div>
  <div class="event-bar">
    <strong>今日催化事件：</strong>''' + report_data["market"]["events"] + '''
  </div>
</div>

<div class="chart-card">
  <h2>🏆 综合评分排行榜</h2>
  <div class="table-wrap">
    <table>
      <thead>
        <tr><th>排名</th><th>基金</th><th>代码</th><th>PE</th><th>PE分位</th><th>规模(亿)</th><th>YTD</th><th>溢价率</th><th>总分</th><th>建议</th></tr>
      </thead>
      <tbody>''')

for i, f in enumerate(report_data["funds"]):
    row_class = "rank-1" if i == 0 else ""
    score_color = "#059669" if f["total"] >= 7.0 else ("#d97706" if f["total"] >= 6.0 else "#dc2626")
    ytd_class = "positive" if float(f["ytd"]) > 0 else "negative"
    prem_class = "negative" if float(f["premium"]) > 2 else ""
    verdict_map = {"谨慎买入":"verdict-buy","买入持有":"verdict-buy","中性偏多":"verdict-hold","中性偏积极":"verdict-hold","谨慎关注":"verdict-watch"}
    verdict_class = verdict_map.get(f["verdict"],"verdict-watch")
    trap_note = '<div class="trap-warn">⚠️ ' + f["trap"] + '</div>' if f["trap"] else ""
    html_parts.append('''<tr class="''' + row_class + '''">
        <td>''' + str(i+1) + '''</td>
        <td><strong>''' + f["name"] + '''</strong>''' + trap_note + '''</td>
        <td style="font-family:monospace">''' + f["code"] + '''</td>
        <td>''' + str(f["pe"]) + '''</td>
        <td>''' + f["pe_percentile"] + '''</td>
        <td>''' + str(f["size"]) + '''</td>
        <td class="''' + ytd_class + '''">''' + f["ytd"] + '''%</td>
        <td class="''' + prem_class + '''">''' + f["premium"] + '''%</td>
        <td style="font-weight:700;color:''' + score_color + '''">''' + str(f["total"]) + '''</td>
        <td class="''' + verdict_class + '''">''' + f["verdict"] + '''</td>
      </tr>''')

html_parts.append('''</tbody>
    </table>
  </div>
  <div style="margin-top:12px;font-size:13px;color:#6b7280;">
    🔴 六维评分：估值水平/行业前景/经理能力/持仓结构/风险收益比/流动性 | 数据来源标注：neodata
  </div>
</div>

<div class="chart-card">
  <h2>📊 六维评分雷达对比图</h2>
  <div style="max-width:500px;margin:0 auto;">
    <canvas id="radarChart"></canvas>
  </div>
</div>

<div class="chart-card">
  <h2>📊 总分柱状图</h2>
  <div style="max-width:800px;margin:0 auto;">
    <canvas id="barChart"></canvas>
  </div>
</div>''')

# Fund detail cards
html_parts.append('<h2 style="font-size:20px;margin:24px 0 16px;">🔍 基金详细分析</h2>')
for i, f in enumerate(report_data["funds"]):
    verdict_emoji = {"谨慎买入":"🟢","买入持有":"🟢","中性偏多":"🟡","中性偏积极":"🟡","谨慎关注":"🟡"}.get(f["verdict"],"⚪")
    trap_note = '<div style="color:#dc2626;font-size:13px;margin-top:6px;">⚠️ ' + f["trap"] + '</div>' if f["trap"] else ""
    score_color = "#059669" if f["total"] >= 7.0 else "#d97706"
    ytd_emoji = "🟢" if float(f["ytd"]) > 0 else "🔴"
    prem_color = "" if float(f["premium"]) <= 2 else "color:#dc2626;"
    
    card = '''<div class="fund-card">
    <div class="fund-card-header" onclick="var b=this.nextElementSibling;b.style.display=b.style.display=='none'?'':'none'">
      <div class="left">
        <h3>#''' + str(i+1) + ' ' + f["name"] + ''' <span style="font-weight:400;font-size:13px;color:#6b7280;">''' + f["code"] + '''</span></h3>
        <div style="font-size:13px;color:#6b7280;">PE ''' + str(f["pe"]) + ''' · ''' + f["pe_percentile"] + ''' · 规模 ''' + str(f["size"]) + '''亿 · YTD ''' + f["ytd"] + '''%</div>
        ''' + trap_note + '''
      </div>
      <div class="score" style="color:''' + score_color + '''">''' + str(f["total"]) + '''</div>
    </div>
    <div class="fund-card-body">
      <div class="detail-grid">
        <div class="detail-item"><label>建议</label><div class="val">''' + verdict_emoji + ' ' + f["verdict"] + '''</div></div>
        <div class="detail-item"><label>YTD涨幅</label><div class="val">''' + ytd_emoji + ' ' + f["ytd"] + '''%</div></div>
        <div class="detail-item"><label>溢价率</label><div class="val" style="''' + prem_color + '''">''' + f["premium"] + '''%</div></div>
        <div class="detail-item"><label>资金流向</label><div class="val" style="font-size:13px;">''' + f["flow"] + '''</div></div>
        <div class="detail-item"><label>PE</label><div class="val">''' + str(f["pe"]) + '''</div></div>
        <div class="detail-item"><label>PE分位</label><div class="val">''' + f["pe_percentile"] + '''</div></div>
      </div>
      <div style="margin-top:12px;">
        <div style="font-size:13px;font-weight:600;margin-bottom:8px;">六维评分：</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">'''
    
    dims = [("估值水平",f["scores"]["估值水平"]),("行业前景",f["scores"]["行业前景"]),("经理能力",f["scores"]["经理能力"]),
            ("持仓结构",f["scores"]["持仓结构"]),("风险收益比",f["scores"]["风险收益比"]),("流动性",f["scores"]["流动性"])]
    for dim_name, dim_score in dims:
        pct = dim_score/10*100
        bar_clr = "#059669" if dim_score >= 7 else ("#d97706" if dim_score >= 5 else "#dc2626")
        card += '''<div><div style="display:flex;justify-content:space-between;font-size:12px;"><span>''' + dim_name + '''</span><span>''' + str(dim_score) + '''</span></div>
          <div class="score-bar"><div class="score-bar-inner" style="width:''' + str(pct) + '''%;background:''' + bar_clr + '''"></div></div></div>'''
    
    card += '</div></div></div></div>'
    html_parts.append(card)

# Conclusion
html_parts.append('''
<div class="chart-card">
  <h2>📋 结论汇总</h2>
  <div style="line-height:1.8;font-size:14px;">
    <p><strong>Top 3推荐：</strong></p>
    <ol style="margin-left:20px;">
      <li><strong>''' + report_data["funds"][0]["name"] + ''' (''' + report_data["funds"][0]["code"] + ''')</strong> — 总分 ''' + str(report_data["funds"][0]["total"]) + ''' — ''' + report_data["funds"][0]["verdict"] + '''。PE分位仅''' + report_data["funds"][0]["pe_percentile"] + '''，规模''' + str(report_data["funds"][0]["size"]) + '''亿流动性极佳，近20日净流入超50亿。</li>
      <li><strong>''' + report_data["funds"][1]["name"] + ''' (''' + report_data["funds"][1]["code"] + ''')</strong> — 总分 ''' + str(report_data["funds"][1]["total"]) + ''' — ''' + report_data["funds"][1]["verdict"] + '''。中概互联PE分位处于历史大底，规模近400亿，AI催化+外资回流。</li>
      <li><strong>''' + report_data["funds"][2]["name"] + ''' (''' + report_data["funds"][2]["code"] + ''')</strong> — 总分 ''' + str(report_data["funds"][2]["total"]) + ''' — ''' + report_data["funds"][2]["verdict"] + '''。消费龙头估值历史低位，十五五消费规划强力政策支撑。</li>
    </ol>
    <p style="margin-top:12px;"><strong>⚠️ 风险关注：</strong></p>
    <ul style="margin-left:20px;">
      <li>银行ETF华宝(512800)溢价率2.49%偏高，需注意溢价回落风险</li>
      <li>旅游ETF富国(159766)PE 67.81倍但分位0.56%，属盈利压缩型低PE</li>
      <li>新能源ETF华夏(516850)规模仅1.32亿偏小，流动性不足</li>
      <li>上证180ETF平安(530280)规模偏小，日均成交约80万</li>
      <li>美联储年内持续鹰派、中东地缘风险影响全球流动性</li>
    </ul>
  </div>
</div>

<div class="disclaimer">
  <p>⚠️ 数据来源：NeoData Financial Search（neodata-financial-search） | 基金海选通过天天基金、雪球、平安基金等5+渠道完成</p>
  <p>本报告基于公开信息整理生成，仅供参考，不构成任何投资建议或基金推荐。基金有风险，投资需谨慎。过往表现不代表未来收益。</p>
  <p style="margin-top:8px;">📁 分析证据文件：deliverables/fund-analysis/（10只基金独立MD分析文件，含neodata原始查询输出）</p>
</div>

<script>''')

# JavaScript section
radar_labels_json = json.dumps(radar_labels)
fund_names_json = json.dumps(fund_names)
fund_codes_json = json.dumps(fund_codes)
top3_data_json = json.dumps(top3_radar)
bar_scores_json = json.dumps(bar_scores)
bar_colors_json = json.dumps(bar_colors)

js = '''
const fundNames = ''' + fund_names_json + ''';
const fundCodes = ''' + fund_codes_json + ''';
const radarLabels = ''' + radar_labels_json + ''';

const ctx1 = document.getElementById('radarChart').getContext('2d');
new Chart(ctx1, {
  type: 'radar',
  data: {
    labels: radarLabels,
    datasets: [
      {label: fundNames[0], data: ''' + json.dumps(top3_radar[0]) + ''', borderColor: '#059669', backgroundColor: 'rgba(5,150,105,0.1)', pointBackgroundColor: '#059669'},
      {label: fundNames[1], data: ''' + json.dumps(top3_radar[1]) + ''', borderColor: '#2563eb', backgroundColor: 'rgba(37,99,235,0.1)', pointBackgroundColor: '#2563eb'},
      {label: fundNames[2], data: ''' + json.dumps(top3_radar[2]) + ''', borderColor: '#d97706', backgroundColor: 'rgba(217,119,6,0.1)', pointBackgroundColor: '#d97706'}
    ]
  },
  options: {scales: {r: {min: 0, max: 10, ticks: {stepSize: 2}}}, plugins: {legend: {position: 'bottom'}}}
});

const ctx2 = document.getElementById('barChart').getContext('2d');
new Chart(ctx2, {
  type: 'bar',
  data: {
    labels: fundCodes.map((c,i) => c + ' ' + fundNames[i].slice(0,6)),
    datasets: [{label: '综合评分', data: ''' + bar_scores_json + ''', backgroundColor: ''' + bar_colors_json + ''', borderRadius: 4}]
  },
  options: {
    indexAxis: 'y',
    scales: {x: {min: 0, max: 10}, y: {ticks: {fontSize: 11}}},
    plugins: {legend: {display: false}}
  }
});
</script>
</body>
</html>'''

html_parts.append(js)

output_html = ''.join(html_parts)
output_path = '/Users/yangjipeng/WorkBuddy/automation-2026-07-07-10-48-40/fund-report-2026-07-30-盘后.html'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output_html)

print(f"Report generated: fund-report-2026-07-30-盘后.html")
print(f"Size: {len(output_html)} bytes")
print(f"Funds: {len(report_data['funds'])}")
for i, f in enumerate(report_data['funds']):
    print(f"  #{i+1} {f['code']} {f['name']}: {f['total']} - {f['verdict']}")
