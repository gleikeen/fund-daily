#!/usr/bin/env python3
"""Generate multi-agent fund report for 2026-07-28-07"""
import datetime

RUN_DT = datetime.datetime(2026, 7, 28, 7, 0)
RUN_TS = RUN_DT.strftime("%Y-%m-%d-%H")
RUN_TS_DISPLAY = RUN_DT.strftime("%Y-%m-%d %H:00")

# Multi-agent scores (agent calculated with standard weights)
AGENT_SCORES = {
    "512880": {"total": 7.86, "verdict": "建议买入", "scores": {"估值水平": 8.5, "行业前景": 7.0, "经理能力": 8.0, "持仓结构": 7.5, "风险收益比": 7.5, "流动性": 9.5},
        "dims": {"估值水平": "PE 15.27处于近十年9.06%分位的极端低位，PB 1.35仅26.72%分位，历史上券商在此估值区间运行时间不足1/10，向下空间窄、向上弹性大。",
                 "行业前景": "7/27 A股成交放量至2.08万亿、近5200只上涨，经纪和两融直接受益。首批主动ETF试点+中金三合一受理+券商发债超1.35万亿，行业创新与整合双线推进。7/28盘前东方证券251亿收购上海证券（1.25x PB、跻身行业前十）再添并购催化。",
                 "经理能力": "艾小军为国泰指数投资部负责人，该ETF为公司旗舰产品，跟踪误差控制成熟。被动型产品对主动管理依赖低，核心在于规模效应和运营稳健性。",
                 "持仓结构": "全面覆盖华泰、招商、广发等头部券商，集中度合理。龙头券商在行业整合期更具竞争优势，但单一行业属性的系统性风险无法通过持仓分散化对冲。",
                 "风险收益比": "向下有9% PE分位的极端估值底保护，向上有成交回暖+中报预增+并购整合三重催化。本周美联储议息和AI制裁扰动更多影响节奏而非趋势，赔率偏正向。",
                 "流动性": "规模516.3亿为全市场最大券商ETF，日均成交活跃，买卖价差极窄，承载大额资金进出无滑点压力。"},
        "verdict_text": "当前处于'估值极端低位+基本面边际改善+政策催化密集'的有利组合。建议左侧分批布局，仓位控制在可承受单行业系统性风险范围内，密切跟踪美联储议息和成交额能否持续维持1.5万亿以上。",
        "supports": ["PE 9.06%分位极端低估提供强安全边际，均值回归空间可观", "成交放量至2.08万亿+中报预增（中金+78~90%）构成基本面双击", "东方证券收购上海证券+首批主动ETF试点双线催化行业格局优化"],
        "risks": ["本周美联储议息若鹰派信号可能引发高Beta板块重估", "美国拟对华AI企业制裁的扩散风险可能抑制风险偏好", "单一行业集中度无法通过持仓分散化对冲系统性风险"]},
    "161725": {"total": 8.20, "verdict": "建议买入", "scores": {"估值水平": 8.8, "行业前景": 7.2, "经理能力": 7.8, "持仓结构": 8.2, "风险收益比": 8.3, "流动性": 9.2},
        "dims": {"估值水平": "PE 18.15处于近10年5.89%分位，PB 3.69仅0.28%分位，两者均触及历史极低区域，股息率高达4.65%，安全边际极为充足。",
                 "行业前景": "茅台年内二次提价（加权超10%）打开行业盈利空间，'十五五'消费规划+7/28税收改革发布提供政策支撑；WTI-7.5%原油暴跌利好生产成本端。人口结构变化与消费升级放缓对行业长期天花板构成约束。",
                 "经理能力": "侯昊长期管理200亿+级别LOF产品，指数投资经验丰富，跟踪误差控制稳定。作为被动指数基金，主动管理空间有限但运作成熟。",
                 "持仓结构": "茅台、五粮液、泸州老窖、山西汾酒等高端/次高端龙头，品牌护城河深厚、ROE高达20.87%；但行业高度集中，缺乏跨板块分散。",
                 "风险收益比": "估值底+提价催化剂+经济数据回暖（工业利润+18.7%），上行空间可观。参考7/20大涨后次日冲高回落，短期追高风险存在但中长期性价比突出。",
                 "流动性": "规模206.9亿，LOF场内+场外双通道，成交活跃、申赎便利，大资金进出无碍。"},
        "verdict_text": "估值分位极低+茅台提价+经济数据回暖构成三重共振，当前位置赔率突出。建议左侧分批布局，密切跟踪今日税收改革发布对消费税的潜在影响，勿追高单笔重仓。",
        "supports": ["PE/PB分位均处历史极低（PE5.89%/PB0.28%），股息率4.65%提供防御垫", "茅台年内两次提价加权超10%（历史首次），直接增厚高端白酒盈利预期", "WTI原油-7.5%至82.61，利好白酒生产成本端+工业利润+18.7%提振消费信心"],
        "risks": ["税收改革方案可能涉及消费税调整，若酒类消费税负提升将直接影响行业利润", "参考7/20集体大涨后7/21冲高回落（茅台-1.94%），短期情绪博弈激烈", "持仓高度集中于4-5只白酒龙头，行业集中度风险突出"]},
    "513050": {"total": 8.08, "verdict": "建议买入", "scores": {"估值水平": 9.0, "行业前景": 7.5, "经理能力": 7.0, "持仓结构": 8.0, "风险收益比": 8.0, "流动性": 9.0},
        "dims": {"估值水平": "PE 16.32/PB 2.12双双处于历史分位2%以下，估值比98%+的历史时间都便宜。ROE 12.95%为估值提供基本面支撑，极端低估状态提供极高安全边际。",
                 "行业前景": "AI大模型（MiniMax获高盛860港元目标价）、智能汽车（小米澎程新车7/30发布）等新增长极涌现，7/28盘前工业利润+18.7%印证宏观韧性。但反垄断、数据安全、跨境审计等监管不确定性仍是长期结构性风险。",
                 "经理能力": "余海燕/刘依姗团队长期稳定管理500亿+级QDII-ETF，运作成熟、跟踪误差可控。ETF被动管理属性强，主动管理加分空间有限。",
                 "持仓结构": "腾讯、阿里、美团、拼多多、京东、携程等均为各自赛道绝对龙头，护城河深厚。集中度高带来板块联动性强但也是弹性放大的来源。",
                 "风险收益比": "估值历史底部+港股7/27强势反弹恒科重返4700确认修复势头。油价暴跌缓解通胀压力利好成长股估值修复。美伊地缘博弈和南向短期流出构成短期扰动但不改中期趋势。",
                 "流动性": "364亿规模头部QDII-ETF，日均成交高度活跃，享有T+0交易机制，大资金出入自如。"},
        "verdict_text": "PE分位1.83%全市场最低水平之一，当前已充分反映悲观预期。中概金龙+2.51%逆势+油价暴跌缓解通胀构成宏观顺风。建议分批定投、严格控仓，勿单笔追高。",
        "supports": ["PE分位1.83%/PB分位1.56%处历史极端低位，安全性极高", "中概金龙+2.51%逆势+港股恒科+1.57%重返4700确认修复势头", "油价暴跌（WTI-7.5%）缓解通胀压力，利好成长股估值修复"],
        "risks": ["中美地缘政治与监管风险持续压制估值中枢", "南向7/27净卖出15.74亿短期逆流+港股反弹持续性待验证", "AI军备竞赛加剧板块内部竞争，利润端承压风险"]},
    "512800": {"total": 7.54, "verdict": "建议买入", "scores": {"估值水平": 8.5, "行业前景": 6.5, "经理能力": 7.0, "持仓结构": 7.5, "风险收益比": 7.5, "流动性": 8.5},
        "dims": {"估值水平": "PB仅0.63破净，PE 6.65处于历史绝对低位，PE/PB分位均不到28%，股息率5.13%构建坚实安全边际。破净+高股息双重验证，银行板块整体估值修复空间显著。",
                 "行业前景": "净息差持续收窄对盈利构成中周期压力，但上半年工业利润+18.7%与'十五五'税改预期提振经济信心，顺周期属性有望受益于复苏。利率下行趋势与资产质量分化是主要制约。",
                 "经理能力": "丰晨成隶属华宝指数团队，被动型ETF管理以跟踪精度为核心，跟踪误差约1.06%处于行业合理水平。非主动选股策略，经理差异化贡献有限。",
                 "持仓结构": "国有大行+股份行+城商行三层覆盖，招商、兴业、工行等核心标的兼具规模与质量。高股息特征鲜明（42家银行中15家股息率超5%），防御与分红双重属性突出。",
                 "风险收益比": "破净低估值+5.13%股息率提供下行保护，上行空间依赖经济复苏力度与利率环境改善。当前价位赔率占优但胜率需政策面进一步确认。",
                 "流动性": "规模106亿位列头部ETF梯队，日均成交活跃，申赎机制成熟。投资者进出成本低，大资金运作无明显冲击成本。"},
        "verdict_text": "破净+高股息+险资长期配置构成压舱石。工业利润+18.7%提振经济信心，但净息差收窄和证金减持需持续关注。建议长期配置、小额定投。",
        "supports": ["PB 0.63破净+PE 6.65历史低位，估值压缩已充分反映悲观预期", "股息率5.13%叠加六大行超4200亿分红，高股息在低利率环境下吸引力突出", "险资持有银行约总股本4.9%，资金结构由交易型转向长期配置"],
        "risks": ["净息差持续收窄拖累银行核心盈利", "证金减持信号+交易型资金分红兑现后获利了结", "经济复苏节奏不确定，若信贷需求恢复不及预期资产质量压力可能抬头"]},
    "008928": {"total": 7.64, "verdict": "建议买入", "scores": {"估值水平": 9.0, "行业前景": 7.0, "经理能力": 6.0, "持仓结构": 8.0, "风险收益比": 8.5, "流动性": 5.5},
        "dims": {"估值水平": "PE 17.49/分位11.45%，PB 3.24/分位0.20%，双双处于历史极低区间。股息率4.58%+ROE 18.95%的组合在被动指数产品中极具吸引力，估值安全边际充裕。",
                 "行业前景": "'十五五'消费规划奠定中长期政策底盘，7/28税收改革发布会提供短期催化，油价下行利好成本端。但上半年社零仅+1.3%、商品零售+1.1%，消费复苏力度偏弱。",
                 "经理能力": "李婷婷以指数化跟踪为主，管理规模较小。被动型产品对经理主动管理能力依赖度低，跟踪误差控制是核心。",
                 "持仓结构": "聚焦食品饮料、农牧等主要消费高股息龙头，防御属性突出。茅台年内二次提价直接利好白酒/食饮权重持仓，细分食品PE仅19.53（近10年3.92%分位）。",
                 "风险收益比": "估值双底+4.58%股息提供'下有底'保护，油价下跌+政策催化+茅台提价三重共振构成'上有催化'。当前点位赔率充分。",
                 "流动性": "⚠️ 规模仅6.54亿偏小，属于指数基金中的小微产品。大额申赎可能产生冲击成本，机构资金进出便利性受限。"},
        "verdict_text": "估值底部+高股息+政策催化三重共振，当前位置赔率突出；但消费复苏偏弱与规模偏小构成现实制约。适合中长线配置型资金分批介入，不宜重仓追涨。",
        "supports": ["PE分位11.45%/PB分位0.20%接近历史极值，股息率4.58%提供稳定现金回报", "茅台提价利好核心持仓+'十五五'消费规划+税收改革预期+油价下跌降成本四重催化", "细分食品指数PE 19.53近10年3.92%分位，持仓标的与基金估值形成双重底部验证"],
        "risks": ["上半年社零仅+1.3%，消费基本面复苏乏力制约反弹高度", "规模仅6.54亿偏小，大额申赎冲击成本不可忽视", "消费板块反弹持续性存疑，若政策预期落空或重回震荡磨底"]},
    "512170": {"total": 7.05, "verdict": "建议买入", "scores": {"估值水平": 8.0, "行业前景": 6.5, "经理能力": 5.0, "持仓结构": 6.5, "风险收益比": 7.0, "流动性": 9.5},
        "dims": {"估值水平": "PE 28.49（分位10.67%）/PB 3.13（分位2.40%）均处历史极低区间，PB分位已至历史极底，为中长期配置提供了充足的安全边际。绝对估值对应ROE 11.26%偏高，但分位角度性价比突出。",
                 "行业前景": "7部门《疾控'十五五'规划》政策催化明确，创新药出海81笔/1100亿美元彰显全球竞争力。7/27创新药（哈三联4天3板）/脑机接口（创新医疗3天2板）活跃。但集采、医保控费长期压制行业利润率。",
                 "经理能力": "⚠️ 张放2026年2月接任胡洁，任职仅5个月且期内收益-10.93%。管理能力与风格有待验证，新老交接期存在不确定性。",
                 "持仓结构": "药明康德11.15%/迈瑞医疗8.53%/联影医疗/爱尔眼科，覆盖CXO/器械/设备/医疗服务多赛道。但药明康德占比超11%，受中美地缘博弈影响大。",
                 "风险收益比": "估值分位极低提供下行缓冲，政策催化+资金流入提供向上弹性（6月以来64亿资金逆势入场）。张放管理期持续亏损和CXO地缘风险是主要衰减项。",
                 "流动性": "规模264.51亿元为大型ETF，日均成交额充裕，申赎机制成熟，流动性优异。"},
        "verdict_text": "左侧布局价值显现，PB分位2.40%已到历史极底。疾控规划+创新药活跃提供短期催化，但经理变更不确定性和CXO地缘风险需持续关注。建议控仓定投、严格勿追高。",
        "supports": ["PB分位2.40%已到历史极底，6月以来64亿资金逆势流入认可底部", "7部门《疾控十五五规划》+创新药出海81笔/1100亿美元政策与产业共振", "7/27创新药/脑机接口活跃，板块情绪边际回暖"],
        "risks": ["基金经理变更不确定性（张放任职仅5月/收益-10.93%）", "药明康德占比11.15%受中美生物技术博弈影响大", "集采常态化+医保控费长期压制行业利润率，低PB可能成为价值陷阱"]},
    "513180": {"total": 7.14, "verdict": "谨慎买入（定投·破线）", "scores": {"估值水平": 6.5, "行业前景": 7.5, "经理能力": 8.0, "持仓结构": 7.5, "风险收益比": 6.0, "流动性": 9.0},
        "dims": {"估值水平": "PE 23.06/分位35.34%已脱离深度低估区间（破20%筛选线），估值处于历史中位偏低区域，安全边际较前期显著收窄。严格按规则退出深度低估判定，仅作定投参与。",
                 "行业前景": "AI大模型（MiniMax+17.14%/高盛860目标价）、自动驾驶（小米澎程新车7/30发布）、云计算多线催化，中国科技龙头全球化布局提速；但中美科技博弈、政策监管路径仍存不确定性。",
                 "经理能力": "徐猛为华夏ETF核心基金经理，管理规模大运作稳健。被动指数产品核心竞争力在于跟踪误差控制，华夏作为头部公募经验成熟。",
                 "持仓结构": "阿里、腾讯、美团、小米、京东、网易、中芯国际等覆盖互联网+半导体+智能硬件核心赛道，标的质量优但集中度高。",
                 "风险收益比": "中概金龙+2.51%逆势是积极信号，恒科经历急跌后修复（7/27+1.57%重返4700）。但纳指四连跌+南向净卖出构成压制，估值下行风险约10-15%，反弹空间取决于政策与业绩兑现。",
                 "流动性": "规模498亿全市场最大恒生科技ETF之一，日均成交额充沛，折溢价控制良好，流动性极佳。"},
        "verdict_text": "PE分位35.34%明确突破20%深度低估线，按纪律退出'深度低估可大额配置'区间。中概金龙+2.51%逆势+恒科重返4700支撑修复，但仅适合定投式分批介入，不宜单笔重仓。",
        "supports": ["中概金龙+2.51%逆势+恒科+1.57%重返4700，外资对中国科技股情绪边际回暖", "科技产业催化密集（小米新车7/30发布/MiniMax获高盛860目标/腾讯持续反弹）", "恒科经历急跌后修复（7/22-3.04%→7/27+1.57%），短期恐慌已释放"],
        "risks": ["PE分位35.34%破20%筛选线，安全边际持续收窄，不具备极端低估的高赔率保护", "纳指四连跌+费半-2.23%（SK海力士-7.47%破发/英伟达-5%），若美股科技继续走弱将拖累", "南向7/27净卖出15.74亿，内资在反弹窗口选择减仓存在分歧"]},
    "168001": {"total": 7.17, "verdict": "建议买入（仅小资金）", "scores": {"估值水平": 9.0, "行业前景": 7.5, "经理能力": 6.5, "持仓结构": 7.0, "风险收益比": 7.5, "流动性": 3.0},
        "dims": {"估值水平": "PE 11.11处于0.86%全样本分位，PB 1.71仅1.40%分位，双双触及历史极值。ROE 15.58%搭配股息率2.82%，绝对估值与相对分位均提供罕见安全边际。",
                 "行业前景": "'十五五'规划单列养老消费+疾病防控规划利好医药端+个人养老金扩容至321只，政策红利密集。但养老产业本质偏防御，整体增速弹性不及科技成长赛道。",
                 "经理能力": "自2018年起长期任职、转型增强后未变更，任职稳定性可加分。但基金规模仅1.27亿，增强策略在小规模下腾挪空间极为有限。",
                 "持仓结构": "医药+消费+金融三大养老支柱均衡配置，行业分散度高，与当前政策催化方向高度契合。但规模过小导致个股权重受限。",
                 "风险收益比": "PE历史分位极低提供下行保护，叠加政策密集窗口与工业利润高增等宏观支撑。风险主要来自规模导致的非市场因素，而非指数本身基本面。",
                 "流动性": "⚠️ 规模仅1.27亿，处于清盘红线边缘区域（通常<5000万触发预警）。大额申赎对净值冲击显著，极端行情下面临流动性枯竭风险。"},
        "verdict_text": "估值全样本最低之一（PE分位0.86%），政策窗口密集（养老消费+疾控规划+税收改革）。但规模仅1.27亿面临清盘风险，仅适合极小额配置、不宜重仓。",
        "supports": ["PE/PB分位双双低于2%，处于全市场最极端低估区间之一", "十五五多部委政策密集落地（养老消费/疾控规划/税收改革），政策催化与低估值共振", "ROE 15.58%+股息率2.82%，在低利率环境下具备类债资产配置吸引力"],
        "risks": ["规模仅1.27亿，远低于行业常规标准，存在清盘风险", "小规模导致增强策略几乎无法有效执行，实质上接近高费率被动指数", "流动性极端脆弱，大资金进出困难、折溢价波动大，仅适合极小资金"]},
}

# Engine scores
ENGINE_SCORES = {
    "512880": 8.51, "161725": 8.29, "513050": 8.24, "512800": 8.15,
    "008928": 7.71, "512170": 7.40, "168001": 7.28, "513180": 6.88,
}

# Agent 评分降序排列（不混引擎权重）
FUND_ORDER = sorted(AGENT_SCORES, key=lambda c: AGENT_SCORES[c]["total"], reverse=True)

FUND_INFO = {
    "512880": {"name": "国泰中证全指证券公司ETF", "index": "证券公司", "type": "股票型ETF", "scale": 516.3, "pe": 15.27, "pe_pct": 9.06, "pb": 1.35, "pb_pct": 26.72, "div": 1.89, "roe": 8.62, "manager": "艾小军", "vstat": "偏低"},
    "161725": {"name": "招商中证白酒指数A", "index": "中证白酒", "type": "指数(LOF)", "scale": 206.9, "pe": 18.15, "pe_pct": 5.89, "pb": 3.69, "pb_pct": 0.28, "div": 4.65, "roe": 20.87, "manager": "侯昊", "vstat": "极低"},
    "513050": {"name": "易方达中概互联网ETF", "index": "中概互联50", "type": "QDII-ETF", "scale": 364.49, "pe": 16.32, "pe_pct": 1.83, "pb": 2.12, "pb_pct": 1.56, "div": 1.06, "roe": 12.95, "manager": "余海燕/刘依姗", "vstat": "极低"},
    "512800": {"name": "华宝中证银行ETF", "index": "中证银行", "type": "股票型ETF", "scale": 106.0, "pe": 6.65, "pe_pct": 26.47, "pb": 0.63, "pb_pct": 27.24, "div": 5.13, "roe": 9.53, "manager": "丰晨成", "vstat": "绝对低估"},
    "008928": {"name": "宏利消费红利指数A", "index": "消费红利", "type": "指数型", "scale": 6.54, "pe": 17.49, "pe_pct": 11.45, "pb": 3.24, "pb_pct": 0.20, "div": 4.58, "roe": 18.95, "manager": "李婷婷", "vstat": "极低"},
    "512170": {"name": "华宝中证医疗ETF", "index": "中证医疗", "type": "股票型ETF", "scale": 264.51, "pe": 28.49, "pe_pct": 10.67, "pb": 3.13, "pb_pct": 2.40, "div": 1.46, "roe": 11.26, "manager": "张放", "vstat": "极低"},
    "513180": {"name": "华夏恒生科技ETF", "index": "恒生科技", "type": "QDII-ETF", "scale": 498.0, "pe": 23.06, "pe_pct": 35.34, "pb": 2.62, "pb_pct": 40.79, "div": 0.95, "roe": 11.20, "manager": "徐猛", "vstat": "偏低·破线"},
    "168001": {"name": "国寿安保中证养老产业指数增强", "index": "养老产业", "type": "指数增强型", "scale": 1.27, "pe": 11.11, "pe_pct": 0.86, "pb": 1.71, "pb_pct": 1.40, "div": 2.82, "roe": 15.58, "manager": "长期任职", "vstat": "极低"},
}

DIM_ORDER = ["估值水平", "行业前景", "经理能力", "持仓结构", "风险收益比", "流动性"]
WEIGHTS = {"估值水平": 0.20, "行业前景": 0.20, "经理能力": 0.12, "持仓结构": 0.13, "风险收益比": 0.25, "流动性": 0.10}

CSS = """
  :root{--bg:#0f1419;--card:#1a2027;--ink:#e6edf3;--sub:#9aa7b4;--line:#2a333d;--brand:#ff4d5e;--brand2:#4aa3ff;--good:#3fb950;--warn:#d29922;--bad:#f85149;--low:#0d2818;--high:#2d1416}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;font-size:15px}
  .wrap{max-width:1100px;margin:0 auto;padding:28px 20px 60px}
  header{background:linear-gradient(135deg,#1a237e,#0d47a1);color:#fff;border-radius:16px;padding:30px 32px;margin-bottom:24px;box-shadow:0 8px 24px rgba(26,35,126,.3)}
  header h1{font-size:25px;margin-bottom:8px}
  header .meta{font-size:13px;opacity:.92}
  h2{font-size:19px;margin:30px 0 14px;padding-left:11px;border-left:4px solid var(--brand);color:var(--ink)}
  h3{font-size:16px;margin:18px 0 8px;color:var(--brand2)}
  .lead{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin-bottom:8px}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:14px 0}
  .kpi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
  .kpi .n{font-size:22px;font-weight:700;color:var(--brand)}
  .kpi .l{font-size:12px;color:var(--sub);margin-top:2px}
  table{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.3);font-size:13px;margin:10px 0}
  th,td{padding:10px 9px;text-align:center;border-bottom:1px solid var(--line)}
  th{background:#29333d;color:#e6edf3;font-weight:600;font-size:12.5px}
  tbody tr:nth-child(even){background:#161b21}
  td.l,th.l{text-align:left}
  .pill{padding:2px 8px;border-radius:20px;font-size:12px;font-weight:600}
  .p-low{background:var(--low);color:var(--good)}
  .p-mid{background:#3a2e10;color:var(--warn)}
  .p-abs{background:#10263d;color:var(--brand2)}
  .card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin:16px 0;box-shadow:0 2px 12px rgba(0,0,0,.25)}
  .card .hd{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px;border-bottom:1px dashed var(--line);padding-bottom:10px;margin-bottom:12px}
  .card .hd .code{font-size:13px;color:var(--brand);font-weight:700;background:var(--low);padding:2px 9px;border-radius:6px}
  .card .hd .nm{font-size:18px;font-weight:700}
  .row{display:grid;grid-template-columns:130px 1fr;gap:8px 14px;margin:7px 0;font-size:14px}
  .row .k{color:var(--sub);font-weight:600}
  .verdict{margin-top:12px;padding:12px 14px;border-radius:10px;font-size:14px}
  .v-buy{background:var(--low);border:1px solid #1f6b3f}
  .v-mid{background:#3a2e10;border:1px solid #6b5410}
  .v-watch{background:#10263d;border:1px solid #1f4a6b}
  .verdict b{color:var(--brand)}
  .risk{background:var(--high);border:1px solid #6b2420;border-radius:10px;padding:12px 14px;margin-top:10px;font-size:13.5px;color:#f0a8a2}
  .scores{margin-top:12px;background:#161b21;border:1px solid var(--line);border-radius:10px;padding:10px 14px}
  .scores table{box-shadow:none;margin:0;background:transparent;font-size:12.5px}
  .scores td,.scores th{padding:5px 8px;border-bottom:1px solid var(--line)}
  .tot{color:var(--brand);font-weight:700}
  ul{margin:6px 0 6px 20px;color:var(--sub);font-size:13.5px}
  ul li{margin:4px 0}
  .note{font-size:12px;color:#6b7884;margin-top:6px}
  footer{margin-top:36px;padding-top:16px;border-top:1px solid var(--line);font-size:12px;color:#6b7884}
  .src{background:#161b21;border:1px solid var(--line);border-radius:10px;padding:12px 16px;font-size:12.5px;color:var(--sub);margin-top:10px}
  .snap{background:#10263d;border:1px solid #1f4a6b;border-radius:10px;padding:11px 14px;margin:12px 0;font-size:13px;color:#a9d3f5}
  .flash{background:#0d2818;border:1px solid #1f6b3f;border-radius:12px;padding:14px 18px;margin:14px 0;font-size:14px}
  .flash b{color:var(--good)}
  .perf{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:12px 0}
  .perf .it{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:13px}
  .perf .it .nm{color:var(--sub);font-size:12px}
  .perf .it .ch{font-size:18px;font-weight:700;margin-top:2px}
  .up{color:var(--good)} .down{color:var(--bad)}
"""

def generate_html():
    # Build compare table
    compare_rows = []
    for code in FUND_ORDER:
        a = AGENT_SCORES[code]
        f = FUND_INFO[code]
        vcls = "p-low" if f["vstat"] in ("极低",) else ("p-abs" if "绝对" in f["vstat"] else "p-mid")
        okcls = "ok" if "建议买入" in a["verdict"] and "谨慎" not in a["verdict"] else "wt"
        compare_rows.append(
            f"<tr><td class='l'>{f['index']}</td><td>{code}</td><td class='l'>{f['name']}</td>"
            f"<td>{f['manager']}</td><td>{f['scale']}</td><td>{f['pe']}</td>"
            f"<td>{f['pe_pct']:.2f}%</td><td>{f['pb']}</td><td>{f['pb_pct']:.2f}%</td>"
            f"<td>{f['div']:.2f}%</td><td>{f['roe']:.2f}%</td>"
            f"<td><span class='pill {vcls}'>{f['vstat']}</span></td>"
            f"<td class='tot'>{a['total']:.2f}</td>"
            f"<td><span class='{okcls}'>{a['verdict']}</span></td></tr>"
        )

    # Build fund cards
    cards = []
    for code in FUND_ORDER:
        a = AGENT_SCORES[code]
        f = FUND_INFO[code]
        e = ENGINE_SCORES[code]
        dim_rows = "".join(
            f"<div class='row'><span class='k'>{d}</span><span class='v'>{a['dims'][d]}</span></div>"
            for d in DIM_ORDER
        )
        score_rows = "".join(
            f"<tr><td class='l'>{d}</td><td>{a['scores'][d]:.1f}</td><td>{WEIGHTS[d]*100:.0f}%</td></tr>"
            for d in DIM_ORDER
        )
        support_items = "".join(f"<li>✅ {s}</li>" for s in a["supports"])
        risk_items = "".join(f"<li>⚠️ {r}</li>" for r in a["risks"])
        vcls = "v-buy" if "建议买入" in a["verdict"] and "谨慎" not in a["verdict"] else "v-mid"
        pe_pass = f["pe_pct"] < 20 or (code == "512800" and f["pb"] < 1.0)
        screen_badge = "✅ 通过低估筛选" if pe_pass else "⚠️ 破线（PE分位≥20%）"
        
        cards.append(f"""
<div class="card">
  <div class="hd"><span class="code">{code}</span><span class="nm">{f['name']}</span>
    <span class="tag" style="color:var(--sub);font-size:12px">跟踪{f['index']}｜{f['type']}｜规模{f['scale']}亿｜经理{f['manager']}｜PE{f['pe']}分位{f['pe_pct']:.2f}%</span></div>
{dim_rows}
  <div class="scores">
    <div style="font-size:13px;color:var(--sub);margin-bottom:6px"><b>Multi-Agent 六维评分（权重→加权总分）</b>　{screen_badge} ｜ 引擎分：{e:.2f} → Agent 综合分：<b class="tot">{a['total']:.2f}</b></div>
    <table><thead><tr><th class="l">维度</th><th>得分(0-10)</th><th>权重</th></tr></thead><tbody>
{score_rows}
      <tr><td class="l"><b>加权总分</b></td><td class="tot">{a['total']:.2f}</td><td>100%</td></tr>
    </tbody></table>
  </div>
  <div class="verdict {vcls}"><b>Multi-Agent 评估结论：{a['verdict']}</b><br>{a['verdict_text']}</div>
  <div style="margin-top:10px;font-size:13px"><b>支撑因素：</b></div><ul>{support_items}</ul>
  <div class="risk" style="margin-top:10px"><b>风险因素：</b></div><ul>{risk_items}</ul>
</div>""")

    # Summary table
    summ_rows = []
    for code in FUND_ORDER:
        a = AGENT_SCORES[code]
        f = FUND_INFO[code]
        e = ENGINE_SCORES[code]
        okcls = "ok" if "建议买入" in a["verdict"] and "谨慎" not in a["verdict"] else "wt"
        summ_rows.append(
            f"<tr><td class='l'>{f['name']}</td><td>{code}</td><td>{f['pe_pct']:.2f}%</td>"
            f"<td>引擎 {e:.2f} / Agent {a['total']:.2f}</td>"
            f"<td class='l'>{a['verdict']}</td>"
            f"<td><span class='{okcls}'>{a['verdict']}</span></td></tr>"
        )

    # 7/28 sort order
    # 纯 Agent 评分降序
    sort_order = [("161725", "8.20", "茅台二次提价+油价续跌成本利好+PE/PB双底极低分位"),
                  ("513050", "8.08", "中概金龙+2.51%逆势+恒科重返4700+PE分位1.83%历史极底"),
                  ("512880", "7.86", "长鑫上市改写半导体估值+东方证券收购上海证券+近20家回购"),
                  ("008928", "7.64", "消费政策底盘+茅台提价+高股息4.58%防御"),
                  ("512800", "7.54", "破净PB0.63+高股息5.13%+工业利润提振信心"),
                  ("168001", "7.17", "PE分位0.86%全样本最低·仅小资金·规模1.27亿"),
                  ("513180", "7.14", "破线·定投·恒科重返4700+中概金龙支撑·PE分位35.34%"),
                  ("512170", "7.05", "疾控规划+创新药活跃+PB分位2.40%极底·经理变更风险")]

    sort_lines = []
    for i, (code, score, desc) in enumerate(sort_order):
        a = AGENT_SCORES[code]
        emoji = "🟢" if "建议买入" in a["verdict"] and "谨慎" not in a["verdict"] else "🟡"
        sort_lines.append(f"{emoji} {FUND_INFO[code]['name']}({code}) {desc}（Agent {score}）→ {a['verdict']}")

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>低估基金筛选与综合评估报告 · 2026-07-28 · 多Agent独立分析 · 周二盘前</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

<header>
  <h1>💰 低估基金筛选与综合评估报告</h1>
  <div class="meta">
    生成日期：<b>2026-07-28 07:00（周二盘前快照·自动化执行）</b><br>
    估值快照：<b>2026-07-15 收盘（平安证券指数信号灯口径，近十年分位）</b><br>
    分析方法：<b>引擎评分 + 8 Agent 并行独立分析（每只基金独立上下文·六维评分+支撑/风险因素）</b><br>
    数据来源：<b>天天基金网 · 雪球/蛋卷 · 平安证券指数信号灯 · 东方财富 · 同花顺iFinD · 腾讯/新浪/网易 · 证券时报/每日经济新闻</b>
  </div>
</header>

<div class="snap">
<b>⚠️ 估值口径与快照时点说明：</b>盘前自动化执行（周二 7/28 生成）——基准 7/15 收盘估值快照（日内稳定）+ 7/27 全天收盘行情（A股/港股/美股）+ 7/28 盘前催化。
<br><br>
<b>① A股 7/27 收盘（周一·强势反弹·长鑫科技上市引爆市场）：</b>上证 <b>+1.15%</b>（3858.25）、深成指 +2.72%（14148.73）、创业板 <b>+3.16%</b>（3590.79）、科创50 +1.16%（1807.95）、中证1000 +3.33%；全天成交 <b>2.08 万亿</b>（放量 1455 亿 vs 7/24 的 1.94 万亿）、<b>近 5200 只上涨、逾百股涨停</b>。建筑材料领涨超 5%，MLCC（三环集团 +10.64%/风华高科涨停）、PCB（景旺电子涨停）、创新药（哈三联 4 天 3 板）、脑机接口（创新医疗 3 天 2 板）、电力（立新能源 8 天 7 板）多点开花。<b>长鑫科技科创板上市首日 +465.82%</b>，单日成交 1412 亿刷新 A 股历史纪录、总市值 3.28 万亿超越工商银行登顶 A 股。石油石化（中曼石油跌停·油价续跌）、煤炭偏弱。
<br><br>
<b>② 港股 7/27 收盘（强势反弹）：</b>恒指 <b>+0.98%</b>（25207.18）、<b>恒科 +1.57%</b>（4702.05），小米 +7.34%（澎程新车 7/30 发布）、MiniMax +17.14%（高盛维持 860 港元目标）、腾讯 +1.93%（443 港元）；大市成交 2105 亿港元、南向净卖出约 15.74 亿。
<br><br>
<b>③ 美股 7/27 收盘（北京 7/28 晨 · 纳指四连跌·中概金龙逆势）：</b>道指 +0.51%（52210.08）、标普 +0.02%（7413.18）、<b>纳指 -0.18%</b>（24932.08，连续四日下跌）；<b>费半 -2.23%</b>（SK海力士-7.47%破发/英伟达-5%/阿斯麦-5%）；苹果 +1% 市值 4.95 万亿再登全球第一；<b>中概金龙 +2.51%</b>（禾赛+5%/腾讯音乐+5%/理想+4%/哔哩哔哩+4%）。
<br><br>
<b>④ 大宗商品：</b><b>国际油价继续暴跌——WTI -7.5% 报 82.61、布油 -8.7% 报 88.36</b>（美伊停火谈判信号混乱——特朗普称"给和平空间"若谈不拢"重新大打"、伊朗否认磋商、沙特阿美关键石油设施疑遭袭起火，但供应端担忧被需求端悲观对冲）。
<br><br>
<b>⑤ 7/28 盘前催化（政策密集+回购潮+美联储议息周）：</b>上半年工业企业利润 <b>+18.7%</b>（电子 +96.9%/集成电路制造利润增近 26 倍/计算机整机制造增近 7 倍）；国新办今日发布"十五五"税收改革方案；7 部门《疾病预防控制"十五五"规划》；东方证券拟 251.2 亿收购上海证券 100% 股权（1.25x PB/跻身行业前十）；工业富联拟 10–20 亿回购 + <b>近 20 家公司密集公告回购</b>（世运电路/宏工科技获银行回购专项贷）；美拟对华 AI 企业制裁+美加征 12.5% 301 关税；本周美联储议息（市场预期按兵不动、但格林斯潘难题再现或借加息压低长端利率）。
</div>

<div class="grid">
  <div class="kpi"><div class="n">8</div><div class="l">入选低估基金（7通过+1破线）</div></div>
  <div class="kpi"><div class="n">+465.82%</div><div class="l">长鑫科技首日（成交1412亿A股纪录）</div></div>
  <div class="kpi"><div class="n">-7.5%</div><div class="l">WTI暴跌至82.61（美伊谈判混乱）</div></div>
  <div class="kpi"><div class="n">+18.7%</div><div class="l">工业利润（电子+96.9%集成+26倍）</div></div>
  <div class="kpi"><div class="n">+2.51%</div><div class="l">中概金龙逆势（禾赛/腾讯音乐+5%）</div></div>
  <div class="kpi"><div class="n">251亿</div><div class="l">东方证券收购上海证券（行业前十）</div></div>
  <div class="kpi"><div class="n">20家</div><div class="l">密集公告回购（工业富联10-20亿）</div></div>
  <div class="kpi"><div class="n">8 Agent</div><div class="l">并行独立分析（独立上下文）</div></div>
</div>

<h2>一、核心指标对比表（Multi-Agent 综合评分）</h2>
<p>估值分位取自<b>平安证券指数信号灯（基准日 7/15 收盘，近十年历史分位）</b>。恒生科技 PE 分位 35.34% 破筛线，按规则退出深度低估、仅作定投；中证银行 PE 分位 26.47% 偏高（盈利周期低位），但 PB 0.63+股息率 5.13% 处绝对历史底部，按"绝对低估"豁免纳入。每只基金均由 <b>独立 Agent</b> 进行六维评分（估值20%/行业前景20%/经理12%/持仓13%/风险收益比25%/流动性10%），综合分 = Agent 加权评分。</p>
<table>
  <thead><tr><th class="l">跟踪指数</th><th>代码</th><th class="l">基金简称</th><th>经理</th><th>规模(亿)</th><th>PE</th><th>PE分位</th><th>PB</th><th>PB分位</th><th>股息率</th><th>ROE</th><th>估值</th><th>综合分</th><th>建议</th></tr></thead>
  <tbody>{' '.join(compare_rows)}</tbody>
</table>
<p class="note">注：① 中证银行以 PB/股息率"绝对低估"豁免；② 恒科 PE 分位 35.34% 破线仅作定投；③ 综合分 = 8 个独立 Agent 六维加权评分（权重量化透明）；④ 引擎分（fund_system.py 硬编码引擎）供参考对比。⑤ <b>Multi-Agent 排序（7/28 盘前）：</b></p>
<p class="note">{' | '.join(f'{code} {name[:8]}' for code, name in [(c, FUND_INFO[c]['name']) for c in FUND_ORDER])}</p>

<h2>二、Multi-Agent 逐只深度分析（独立 Agent + 独立上下文）</h2>
{''.join(cards)}

<h2>三、Multi-Agent 评估结论汇总</h2>
<table>
  <thead><tr><th class="l">基金</th><th>代码</th><th>PE分位</th><th class="l">评分（引擎/Agent）</th><th class="l">Agent 建议</th><th>结论</th></tr></thead>
  <tbody>{' '.join(summ_rows)}</tbody>
</table>

<h3>Multi-Agent 排序（7/28 盘前）：</h3>
<ol style="margin:10px 0 10px 24px;color:var(--sub);font-size:14px">
{''.join(f'<li style="margin:6px 0">{line}</li>' for line in sort_lines)}
</ol>

<div class="note" style="margin-top:20px">
<b>估值快照：</b>平安证券指数信号灯口径（基准 7/15 收盘，与 7/14~7/27 各版一致，日内稳定）。
<b>7/27 收盘：</b>A股强势反弹（沪+1.15%/深+2.72%/创+3.16%/近5200涨/成交2.08万亿放量1455亿/长鑫+465.82%成交1412亿纪录）；港股恒指+0.98%/恒科+1.57%（小米+7.34%/MiniMax+17.14%）；美股纳指-0.18%四连跌/费半-2.23%/中概金龙+2.51%。
<b>7/28 盘前催化：</b>工业利润+18.7%/税收改革/疾控规划/东方证券收购上海证券/近20家回购/美对华AI制裁/美联储议息。<b>Multi-Agent 独立分析：</b>8 只基金各由独立 Agent（独立上下文）进行六维评分，综合分 = Agent 加权评分。
</div>

<div class="src">
<b>数据来源：</b>天天基金网（fund.eastmoney.com）；雪球/蛋卷估值中心（djfunds.imedao.com）；平安证券指数信号灯（近十年分位，基准 7/15 收盘）；东方财富/同花顺 iFinD（行情/南向/规模）；7/27 收盘：证券时报（收评逾5100涨·长鑫+465.82%·MLCC异动）、央广网（收评创业板+3.16%·长鑫成交破1400亿）、新华社（港股恒指+0.98%恒科+1.57%）、中新经纬/每经（美股纳指四连跌·中概金龙+2.51%·油价暴跌 WTI-7.5%）；7/28 盘前：陆家嘴财经早餐（工业利润+18.7%·税收改革·疾控规划·东方证券收购·回购潮）、雪球盘前早参/同花顺财经早餐（美国AI制裁·20家回购·美伊谈判混乱·美联储议息）。
</div>

<footer>
  ⚠️ <b>风险提示：</b>本报告由 AI Multi-Agent 系统基于公开信息整理生成（天天基金、雪球、平安证券指数信号灯、东方财富、同花顺、腾讯、证券时报、每经等平台），仅供研究参考，<b>不构成任何投资建议或个股推荐</b>。基金有风险，投资需谨慎。估值分位会随行情变化，请以最新数据为准。过去的表现不代表未来的结果。请结合自身风险承受能力做出独立判断。<br>
  <b>报告生成：</b>2026-07-28 07:00 自动化执行 · 7/15 收盘估值快照 + 7/27 全天收盘数据 + 7/28 盘前催化 · 8 Agent 并行独立分析 · 引擎评分 + Multi-Agent 综合评分
</footer>

</div>
</body>
</html>"""
    return html

def main():
    report_file = f"fund-report-{RUN_TS}.html"
    html = generate_html()
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Multi-agent report: {report_file} ({len(html)} bytes)")
    
    # Update index.html
    import re
    import os
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update latest card
    m = re.search(r'<a class="latest" href="[^"]+">.*?</a>', content, re.S)
    if m:
        summary = f"A股7/27强势反弹近5200涨·长鑫+465.82%成交1412亿·恒科+1.57%重返4700·中概金龙+2.51%逆势·油价续跌WTI82.61 → 8 Agent并行独立分析（纯Agent分排序） → 白酒居首(8.20)·中概第二(8.08)·券商第三(7.86)·消费红利(7.64)·银行(7.54)·养老(7.17)·恒科破线定投(7.14)·医疗(7.05)；7只建议买入+恒科破线定投"
        new_block = (f'<a class="latest" href="{report_file}">\n'
                     f'      <span class="label">最新报告 · Multi-Agent 独立分析（盘前快照 · 8 Agent 并行）</span>\n'
                     f'      <strong>{RUN_TS_DISPLAY}</strong>\n'
                     f'      <span>{summary}</span>\n'
                     f'    </a>')
        content = content[:m.start()] + new_block + content[m.end():]
    
    # Add to archive
    new_li = f'        <li><a href="{report_file}"><time datetime="{RUN_TS[:10]}">{RUN_TS}</time><span class="arrow">查看报告 →</span></a></li>\n'
    content = re.sub(r'(      <ul>\n)', rf'\1{new_li}', content, count=1)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    
    # Update README
    readme = "README.md"
    if os.path.exists(readme):
        with open(readme, "r", encoding="utf-8") as f:
            rc = f.read()
        rc = re.sub(r'fund-report-\d{4}-\d{2}-\d{2}-\d{2}\.html', report_file, rc, count=1)
        with open(readme, "w", encoding="utf-8") as f:
            f.write(rc)
    
    print(f"[OK] index.html + README.md updated -> {report_file}")

if __name__ == "__main__":
    main()
