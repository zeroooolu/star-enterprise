from pathlib import Path

path = Path('prototype-v4/index.html')
html = path.read_text(encoding='utf-8')

# API 页面中文化辅助标签与真实文档入口。
replacements = {
    '<span>api.star-distribution.com</span><b>LIVE EXAMPLE</b>': '<span>Open API V1</span><b>接口示例</b>',
    '<span>REQUEST</span>': '<span>请求</span>',
    '<span>RESPONSE</span>': '<span>响应</span>',
    '<span class="eyebrow">API CAPABILITIES</span>': '<span class="eyebrow">API 能力</span>',
    '<article><span>01 · BUSINESS</span><h3>客户与基础资料</h3>': '<article><span>01 · 基础资料</span><h3>客户与基础资料</h3>',
    '<article><span>02 · CATALOG</span><h3>内容与曲库</h3>': '<article><span>02 · 内容与曲库</span><h3>内容与曲库</h3>',
    '<article><span>03 · DISTRIBUTION</span><h3>发行管理</h3>': '<article><span>03 · 发行管理</span><h3>发行管理</h3>',
    '<article><span>04 · STATUS</span><h3>渠道状态</h3>': '<article><span>04 · 发行状态</span><h3>渠道状态</h3>',
    '<article><span>05 · REPORTING</span><h3>数据与报表</h3>': '<article><span>05 · 数据与报表</span><h3>数据与报表</h3>',
    '<article><span>06 · SETTLEMENT</span><h3>收入与结算</h3>': '<article><span>06 · 收入与结算</span><h3>收入与结算</h3>',
    '现有艺人、专辑、曲目等业务能力统一封装为 Public API；发行提交沿用已跑通的 K-JSON 发行链路，并对外抽象为更简洁的 Distribution 资源。': '现有艺人、厂牌、专辑、歌曲等业务能力统一封装为开放 API；发行提交沿用已跑通的 K-JSON 发行链路，并对外抽象为更简洁的发行资源。',
    'href="/enterprise/developers#webhook"': 'href="/enterprise/developers#webhooks"',
    '查看 Webhook 设计 →': '查看事件回调说明 →',
    '<small>REAL-TIME</small>': '<small>实时接口</small>',
    '<small>STANDARD RELEASE</small>': '<small>标准发行</small>',
    '<small>BATCH</small>': '<small>批量导入</small>',
    '<small>FILE EXCHANGE</small>': '<small>文件交换</small>',
    '<small>STRUCTURED DATA</small>': '<small>结构化数据</small>',
    '<small>INDUSTRY STANDARD</small>': '<small>行业标准</small>',
    'Public Resource API': '开放资源 API',
    'Changelog': '更新记录',
    'Request ID': '请求 ID',
}
for old, new in replacements.items():
    html = html.replace(old, new)

start = html.index('  <section class="section api-explorer-section">')
end = html.index('  <section class="section dark api-flow-section"', start)
new_explorer = r'''  <section class="section api-explorer-section"><div class="container"><div class="visual-section-head reveal"><div><span class="eyebrow">接口概览</span><h2>按照音乐发行对象组织接口</h2></div><p>开发者不需要理解内部系统结构，按“内容 → 文件 → 发行 → 状态 → 参考数据”的顺序即可完成标准发行接入。</p></div><div class="api-explorer reveal" data-api-explorer><div class="api-resource-nav"><button class="active" type="button" data-api-resource="catalog"><span>01</span><b>内容与曲库</b><small>艺人 · 厂牌 · 专辑 · 歌曲</small></button><button type="button" data-api-resource="files"><span>02</span><b>文件</b><small>音频 · 封面 · 上传凭证</small></button><button type="button" data-api-resource="distribution"><span>03</span><b>发行</b><small>提交 · 更新 · 下架</small></button><button type="button" data-api-resource="status"><span>04</span><b>发行状态</b><small>任务 · 平台结果</small></button><button type="button" data-api-resource="reference"><span>05</span><b>参考数据</b><small>地区 · 语言 · 风格 · 角色 · 平台</small></button></div><div class="api-resource-code"><div class="resource-code-head"><span>接口</span><b id="api-resource-title">内容与曲库</b></div>
    <div class="api-endpoints" data-api-endpoints="catalog"><p><em>POST</em><code>/v1/artists</code><span>创建艺人</span></p><p><em>POST</em><code>/v1/labels</code><span>创建厂牌</span></p><p><em>POST</em><code>/v1/albums</code><span>创建专辑 / 单曲</span></p><p><em>POST</em><code>/v1/tracks</code><span>创建歌曲</span></p><p><em class="get">GET</em><code>/v1/tracks/{trackId}</code><span>查询歌曲详情</span></p></div>
    <div class="api-endpoints" data-api-endpoints="files" hidden><p><em class="get">GET</em><code>/open/v1/oss/sts</code><span>获取临时上传凭证</span></p><p><em class="get">OSS</em><code>{basePath}/...</code><span>上传音频、封面与批次文件</span></p></div>
    <div class="api-endpoints" data-api-endpoints="distribution" hidden><p><em>POST</em><code>/v1/distributions</code><span>创建并提交发行</span></p><p><em class="get">GET</em><code>/v1/distributions/{distributionId}</code><span>查询发行详情</span></p><p><em>POST</em><code>/v1/distributions/{distributionId}/update</code><span>更新发行</span></p><p><em>POST</em><code>/v1/distributions/{distributionId}/takedown</code><span>指定平台下架</span></p><p><em>POST</em><code>/v1/distributions/{distributionId}/takedown-all</code><span>全部平台下架</span></p></div>
    <div class="api-endpoints" data-api-endpoints="status" hidden><p><em class="get">GET</em><code>/open/v1/kjson/tasks/{taskId}</code><span>查询当前发行任务</span></p><p><em class="get">GET</em><code>/open/v1/release/result/latest/{catalogNo}</code><span>查询最新平台发行结果</span></p><p><em class="get">GET</em><code>/v1/distributions/{distributionId}/platforms</code><span>V1 统一平台状态</span></p></div>
    <div class="api-endpoints" data-api-endpoints="reference" hidden><p><em class="get">GET</em><code>/v1/reference/territories</code><span>国家与地区</span></p><p><em class="get">GET</em><code>/v1/reference/languages</code><span>语言</span></p><p><em class="get">GET</em><code>/v1/reference/genres</code><span>音乐风格</span></p><p><em class="get">GET</em><code>/v1/reference/roles</code><span>贡献者角色</span></p><p><em class="get">GET</em><code>/v1/reference/dsps</code><span>发行平台</span></p></div>
  </div></div></div></section>

'''
html = html[:start] + new_explorer + html[end:]
path.write_text(html, encoding='utf-8')
