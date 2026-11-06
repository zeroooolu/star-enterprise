"""Build sales reference PDFs that mirror the website's pricing hierarchy."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('NotoSansSC', str(ROOT / 'scripts/fonts/NotoSansSC-pricing-subset.ttf')))
pdfmetrics.registerFont(TTFont('NotoSansSC-Bold', str(ROOT / 'scripts/fonts/NotoSansSC-pricing-bold-subset.ttf')))
FONT = 'NotoSansSC'
BOLD = 'NotoSansSC-Bold'
NAVY = colors.HexColor('#152746')
BLUE = colors.HexColor('#0648F9')
PALE = colors.HexColor('#EEF3FF')
SOFT = colors.HexColor('#F5F8FC')
TEXT = colors.HexColor('#253653')
MUTED = colors.HexColor('#61718A')
LINE = colors.HexColor('#DCE5F0')
WHITE = colors.white
W = 170*mm

styles = {
 'eyebrow': ParagraphStyle('eyebrow', fontName=FONT, fontSize=8, leading=13, textColor=BLUE, spaceAfter=6),
 'title': ParagraphStyle('title', fontName=BOLD, fontSize=23, leading=32, textColor=NAVY, spaceAfter=6),
 'lead': ParagraphStyle('lead', fontName=FONT, fontSize=10, leading=17, textColor=MUTED, spaceAfter=14),
 'section': ParagraphStyle('section', fontName=BOLD, fontSize=14, leading=21, textColor=NAVY, spaceBefore=12, spaceAfter=8),
 'subsection': ParagraphStyle('subsection', fontName=BOLD, fontSize=10, leading=16, textColor=NAVY, spaceBefore=7, spaceAfter=4),
 'body': ParagraphStyle('body', fontName=FONT, fontSize=9, leading=16, textColor=TEXT, spaceAfter=7),
 'note': ParagraphStyle('note', fontName=FONT, fontSize=8.2, leading=14, textColor=MUTED, spaceAfter=5),
 'cardlabel': ParagraphStyle('cardlabel', fontName=FONT, fontSize=8.2, leading=12, textColor=MUTED, spaceAfter=6),
 'cardtitle': ParagraphStyle('cardtitle', fontName=BOLD, fontSize=15, leading=21, textColor=NAVY, spaceAfter=8),
 'price': ParagraphStyle('price', fontName=BOLD, fontSize=21, leading=27, textColor=BLUE, spaceAfter=5),
 'priceunit': ParagraphStyle('priceunit', fontName=FONT, fontSize=9, leading=14, textColor=MUTED, spaceAfter=8),
 'cardbody': ParagraphStyle('cardbody', fontName=FONT, fontSize=8.4, leading=14, textColor=TEXT, spaceAfter=3),
 'head': ParagraphStyle('head', fontName=BOLD, fontSize=8.4, leading=13, textColor=WHITE),
 'cell': ParagraphStyle('cell', fontName=FONT, fontSize=8.3, leading=13.3, textColor=TEXT),
}

def P(value, style='body'):
    return Paragraph(str(value), styles[style])

def T(rows, widths, first_col=False):
    data = [[P(v, 'head' if i == 0 else 'cell') for v in row] for i,row in enumerate(rows)]
    result = Table(data, colWidths=widths, hAlign='LEFT', repeatRows=1)
    commands = [
        ('BACKGROUND',(0,0),(-1,0),NAVY),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,SOFT]),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),6.5),('BOTTOMPADDING',(0,0),(-1,-1),6.5),
        ('LINEBELOW',(0,-1),(-1,-1),0.5,LINE),
    ]
    if first_col: commands.append(('TEXTCOLOR',(0,1),(0,-1),NAVY))
    result.setStyle(TableStyle(commands))
    return result

def card(label,title,price,unit,lines,featured=False):
    content=[P(label,'cardlabel'),P(title,'cardtitle'),P(price,'price'),P(unit,'priceunit')]
    content.extend(P('• '+line,'cardbody') for line in lines)
    shell=Table([[content]],colWidths=[53*mm],hAlign='LEFT')
    shell.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),WHITE if not featured else PALE),
        ('BOX',(0,0),(-1,-1),1.2,BLUE if featured else LINE),
        ('ROUNDEDCORNERS',[12,12,12,12]),
        ('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),10),
        ('TOPPADDING',(0,0),(-1,-1),13),('BOTTOMPADDING',(0,0),(-1,-1),12),
        ('VALIGN',(0,0),(-1,-1),'TOP')]))
    return shell

def three_cards(cards):
    row=Table([[cards[0],cards[1],cards[2]]],colWidths=[56.5*mm,56.5*mm,56.5*mm],hAlign='LEFT')
    row.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),1.5),('RIGHTPADDING',(0,0),(-1,-1),1.5),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
    ]))
    return row

def footer(canvas,doc):
    canvas.setStrokeColor(LINE)
    canvas.line(20*mm,18*mm,190*mm,18*mm)
    canvas.setFont(FONT,8)
    canvas.setFillColor(MUTED)
    canvas.drawString(20*mm,12.5*mm,'看见音乐 · 企业发行服务  |  标准参考方案 · 2026-11-06')
    canvas.drawRightString(190*mm,12.5*mm,str(doc.page))

def build(filename,story):
    doc=SimpleDocTemplate(str(OUT/filename),pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,
                          topMargin=19*mm,bottomMargin=23*mm,title=filename,author='看见音乐')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)

platform=[
    P('KANJIAN MUSIC  /  ENTERPRISE PLATFORM','eyebrow'),
    P('自有品牌发行平台 · 参考报价','title'),
    P('面向发行商、唱片公司、版权机构与音乐平台。像网页一样先看版本与核心权益，再按实际业务范围确认最终报价。','lead'),
    three_cards([
        card('BASIC  /  小规模发行运营','基础版','¥999','/ 月  ·  年付 ¥9,999',[
            '每月包含 1,250 次发行','1,000 首曲库 · 50 个合作客户','品牌门户与完整发行流程','标准客户与技术支持']),
        card('PROFESSIONAL  /  规模化运营','专业版','¥9,999','/ 月  ·  年付 ¥99,999',[
            '每月包含 15,000 次发行','5 万首曲库 · 1,000 个合作客户','独立域名与合作方分账','优先支持与首次实施培训'],True),
        card('ENTERPRISE  /  平台级业务','企业版','¥29,999','/ 月  ·  年付 ¥299,999',[
            '每月包含 50,000 次发行','30 万首曲库起','包含发行 API 与 DDEX 接入','专属客户经理与 SLA']),
    ]),
    P('核心权益','section'),
    T([
        ['业务容量与服务','基础版','专业版','企业版'],
        ['曲库规模','1,000 首','50,000 首','300,000 首起'],
        ['视频使用量','100 个','1,000 个','10,000 个'],
        ['合作客户','50 个','1,000 个','按项目配置'],
        ['赠送 ISRC','1,000 个','50,000 个','至少 300,000 个'],
        ['每月免费更新 / 重传','按次计费','10 次','50 次'],
        ['客户支持','标准支持','优先支持','专属客户经理'],
    ],[50*mm,39*mm,40*mm,41*mm],True),
    Spacer(1,5*mm),
    P('共同包含：客户发行门户、企业管理后台、曲库与作品管理、发行提交及状态跟踪、数据和收入报表、UPC、页面与 Excel 内容导入。','note'),
    PageBreak(),
    P('PLAN COMPARISON','eyebrow'),
    P('关键权益与实施服务','title'),
    P('根据业务容量、合作客户经营、批量处理与系统集成深度选择版本。','lead'),
    T([
        ['关键权益','基础版','专业版','企业版'],
        ['独立域名','—','支持','支持'],
        ['合作方分账','—','支持','支持'],
        ['批量发行','—','支持','支持'],
        ['SFTP / XML 数据交换','—','支持','支持'],
        ['DDEX 接入','—','支持','支持'],
        ['发行 API','—','—','包含'],
        ['Webhook / API 日志','—','—','支持'],
        ['历史曲库迁移','可选服务','可选服务','按项目范围'],
        ['上线与培训','标准上线指引','首次实施培训','项目实施 / 定制培训'],
        ['技术支持','标准支持','优先支持','专属支持 / SLA'],
    ],[54*mm,37*mm,39*mm,40*mm],True),
    P('订阅及使用规则','section'),
    T([
        ['项目','现行参考口径'],
        ['订阅周期','月付首期 3 个月，之后可按月续费；年付一次购买 12 个月，较连续月付约省 17%。'],
        ['标准部署费','月付另收 ¥9,800 一次性标准部署费；年付免标准部署费。'],
        ['发行使用量','每月额度重置、不结转。1 首歌曲 × 1 个目标渠道 = 1 次。'],
        ['额外发行次数','套餐额度用完后 ¥1 / 次，不另收增购实施费。'],
        ['特殊任务','更新 / 重传超出免费次数后按发行传输计费；下架、失败任务等以协议为准。'],
    ],[40*mm,130*mm],True),
    P('曲库扩容及专项服务','section'),
    P('基础版每增 100 首：¥49 / 月或 ¥490 / 年；专业版每增 1,000 首：¥199 / 月或 ¥1,990 / 年；企业版每增 10,000 首：¥499 / 月或 ¥4,990 / 年。扩容随订阅续费，不增加发行次数或赠送 ISRC。'),
    P('历史曲库迁移、复杂字段映射、专项联调、其他容量扩容及大型项目实施按工作范围单独评估。','note'),
    P('本资料为标准参考方案，不构成正式合同报价。最终价格、税务口径与交付范围以双方确认的合作文件为准。','note'),
]

api=[
    P('KANJIAN MUSIC  /  DISTRIBUTION API','eyebrow'),
    P('发行 API · 参考报价','title'),
    P('适合已有网站、App、SaaS 或内部系统的企业，通过 API 接入发行能力。独立 API 方案不默认包含完整客户发行门户和企业发行平台。','lead'),
    three_cards([
        card('STARTER  /  起步额度','起步额度','¥999','/ 月  ·  6 个月 ¥5,994',[
            '半年包含 7,500 次发行','适合验证接入与初期业务','套餐次数可跨月使用']),
        card('GROWTH  /  成长额度','成长额度','¥9,999','/ 月  ·  6 个月 ¥59,994',[
            '半年包含 90,000 次发行','适合持续批量发行','套餐次数可跨月使用'],True),
        card('SCALE  /  规模额度','规模额度','¥29,999','/ 月  ·  6 个月 ¥179,994',[
            '半年包含 300,000 次发行','适合高频规模化发行','套餐次数可跨月使用']),
    ]),
    P('费用结构','section'),
    T([
        ['费用项目','现行参考口径','说明'],
        ['基础接入实施费','¥9,800 / 一次性','开通基础发行 API 权限'],
        ['发行次数套餐','按上方档位','首期至少购买 6 个月'],
        ['超额发行','¥1 / 首 / 渠道','套餐次数用完后计费'],
        ['扩展 API 模块','¥2,000 / 模块','一次性参考费用，按需选配'],
    ],[45*mm,46*mm,79*mm],True),
    P('基础发行 API 能力','section'),
    P('通过标准 API 完成音乐内容提交、发行任务、更新与下架，并查询渠道处理状态。1 首歌曲发行到 1 个目标渠道计 1 次。套餐包含次数在半年周期内可跨月使用；套餐并非现金充值余额。'),
    P('首期费用示例（基础实施费 + 6 个月套餐费，未计扩展模块和超额使用）：起步 ¥15,794；成长 ¥69,794；规模 ¥189,794。','note'),
    PageBreak(),
    P('MODULAR API  /  DELIVERY','eyebrow'),
    P('扩展能力与服务范围','title'),
    P('在基础发行之外，根据现有系统选配业务 API。模块价格是一次性参考费用，实际接口权限与交付范围按项目确认。','lead'),
    T([
        ['扩展模块','主要能力','费用'],
        ['资产管理 API','专辑、歌曲、音视频文件及关联元数据','¥2,000'],
        ['艺人与厂牌 API','艺人、厂牌与作品关联','¥2,000'],
        ['发行数据 API','发行配置、渠道记录与操作历史','¥2,000'],
        ['版税报表 API','账期、平台、专辑和歌曲收益查询','¥2,000'],
        ['分账管理 API','歌曲分账明细与贡献者收益','¥2,000'],
        ['客户管理 API','客户档案、联系人、标签和认证信息','¥2,000'],
    ],[44*mm,100*mm,26*mm],True),
    P('关键规则与交付边界','section'),
    T([
        ['主题','说明'],
        ['额度与结算','首期至少 6 个月；额度可在周期内跨月使用。额外充值或结算方式以合作方案为准。'],
        ['接口权限','正式开放的模块、字段、环境及技术服务范围由双方确认。'],
        ['特殊任务','更新、下架、重传、重复提交、失败任务的计费以正式协议为准。'],
        ['专项集成','Excel、SFTP、XML、DDEX 等方式单独评估，不默认包含在标准 API 实施服务中。'],
    ],[39*mm,131*mm],True),
    P('申请与报价流程','section'),
    P('提供现有系统、预计半年发行歌曲数、平均目标渠道数及所需扩展模块。商务确认接口与交付范围后提供正式报价和合作方案。'),
    P('本资料为标准参考方案，不构成正式合同报价。最终价格、税务口径与交付范围以双方确认的合作文件为准。','note'),
]

build('enterprise-platform-quote-2026-11-06.pdf',platform)
build('distribution-api-quote-2026-11-06.pdf',api)
