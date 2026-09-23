from pathlib import Path

INDEX = Path('prototype-v4/index.html')
html = INDEX.read_text(encoding='utf-8')

api_start = html.index('<section class="page api-page" data-page="api">')
dev_start = html.index('<section class="page" data-page="developers">', api_start)
apply_start = html.index('<section class="page apply-page" data-page="apply">', dev_start)

api_section = r'''<section class="page api-page" data-page="api">
  <section class="subhero api-hero"><div class="container reveal"><span class="eyebrow">DISTRIBUTION API</span><h1>把音乐发行，<br>接进现有产品。</h1><p>面向已有网站、App、SaaS 或内部业务系统的企业，通过标准 API 接入内容管理、发行提交、渠道状态、数据报表与收入结算能力，在保留现有产品体验的同时扩展音乐发行业务。</p><div class="hero-actions"><a class="btn btn-primary btn-lg" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-secondary btn-lg" href="/enterprise/developers" data-route>查看开发者指南</a></div><div class="api-hero-proof"><span>标准 API</span><span>Webhook 状态回调</span><span>测试与生产环境</span><span>K-JSON · SFTP · XML · DDEX</span></div></div></section>

  <section class="api-console-wrap"><div class="container"><div class="api-console reveal"><div class="api-console-head"><div><i></i><i></i><i></i></div><span>Star Enterprise Open API</span><b>PUBLIC API MODEL</b></div><div class="api-console-grid"><div class="api-code-pane"><div class="code-pane-title"><span>REQUEST</span><b><em>POST</em> /v1/distributions</b></div><pre><code>{
  "album_id": "alb_8f12a",
  "release_date": "2026-10-02",
  "platforms": [
    "spotify", "apple_music", "qq_music"
  ],
  "territories": ["WORLDWIDE"]
}</code></pre></div><div class="api-code-pane response"><div class="code-pane-title"><span>RESPONSE</span><b><em>202</em> ACCEPTED</b></div><pre><code>{
  "id": "dist_4821",
  "status": "processing",
  "catalog_number": "CAT-2026-0001",
  "platform_count": 3
}</code></pre></div></div></div></div></section>

  <nav class="api-subnav" aria-label="发行 API 页面章节"><div class="container"><a href="#api-capabilities">API 能力</a><a href="#api-flow">接入流程</a><a href="#api-developer">开发者支持</a><a href="#api-integration">接入方式</a><a href="#api-pricing">商业方案</a></div></nav>

  <section class="section" id="api-capabilities"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">API CAPABILITIES</span><h2>按业务需要，接入对应能力。</h2></div><p>围绕音乐发行全生命周期开放标准化能力。企业可根据现有产品架构选择所需模块，并通过统一接口完成业务集成。</p></div><div class="api-module-grid reveal"><article><span>01 · BUSINESS</span><h3>客户与基础资料</h3><p>同步企业、合作客户、地区、语言、角色及发行所需基础配置，使发行能力与现有业务体系保持一致。</p></article><article><span>02 · CATALOG</span><h3>内容与曲库</h3><p>创建和维护艺人、厂牌、专辑、歌曲、音频文件、封面及发行元数据，建立统一的音乐内容对象。</p></article><article><span>03 · DISTRIBUTION</span><h3>发行管理</h3><p>创建发行任务，配置目标平台与发行时间，并支持发行后的修改、更新、单渠道下架与全部下架。</p></article><article><span>04 · STATUS</span><h3>渠道状态</h3><p>按任务、批次或 Catalog Number 获取处理结果，查看目标平台状态、平台专辑 ID 与失败信息。</p></article><article><span>05 · REPORTING</span><h3>数据与报表</h3><p>按合作范围开放发行后的平台数据与业务报表，为产品展示、运营分析及企业内部数据处理提供基础。</p></article><article><span>06 · SETTLEMENT</span><h3>收入与结算</h3><p>按合作范围开放收入报表、分账结果与结算状态，将发行后的财务数据接入企业现有业务与财务流程。</p></article></div></div></section>

  <section class="section api-explorer-section"><div class="container"><div class="visual-section-head reveal"><div><span class="eyebrow">API EXPLORER</span><h2>围绕统一业务对象开放接口</h2></div><p>现有艺人、专辑、曲目等业务能力统一封装为 Public API；发行提交沿用已跑通的 K-JSON 发行链路，并对外抽象为更简洁的 Distribution 资源。</p></div><div class="api-explorer reveal" data-api-explorer><div class="api-resource-nav"><button class="active" type="button" data-api-resource="catalog"><span>01</span><b>Catalog</b><small>内容与曲库</small></button><button type="button" data-api-resource="distribution"><span>02</span><b>Distribution</b><small>发行管理</small></button><button type="button" data-api-resource="status"><span>03</span><b>Status</b><small>渠道状态</small></button><button type="button" data-api-resource="reports"><span>04</span><b>Reports</b><small>数据与结算</small></button></div><div class="api-resource-code"><div class="resource-code-head"><span>ENDPOINTS</span><b id="api-resource-title">Catalog</b></div>
    <div class="api-endpoints" data-api-endpoints="catalog"><p><em>POST</em><code>/v1/artists</code><span>Create artist</span></p><p><em class="get">GET</em><code>/v1/artists/{artistId}</code><span>Get artist</span></p><p><em>POST</em><code>/v1/albums</code><span>Create album / single</span></p><p><em>POST</em><code>/v1/tracks</code><span>Create track</span></p><p><em class="get">GET</em><code>/v1/reference/*</code><span>Languages · territories · genres · roles</span></p></div>
    <div class="api-endpoints" data-api-endpoints="distribution" hidden><p><em>POST</em><code>/v1/distributions</code><span>Create distribution</span></p><p><em class="get">GET</em><code>/v1/distributions/{id}</code><span>Get distribution</span></p><p><em>POST</em><code>/v1/distributions/{id}/update</code><span>Update release</span></p><p><em>POST</em><code>/v1/distributions/{id}/takedown</code><span>Request takedown</span></p><p><em>POST</em><code>/v1/distributions/{id}/takedown-all</code><span>Take down all platforms</span></p></div>
    <div class="api-endpoints" data-api-endpoints="status" hidden><p><em class="get">GET</em><code>/v1/distributions/{id}/platforms</code><span>Platform status</span></p><p><em class="get">GET</em><code>/v1/releases/{catalogNo}/latest</code><span>Latest release result</span></p><p><em>POST</em><code>/v1/webhooks</code><span>Create webhook</span></p><p><em class="get">GET</em><code>/v1/webhook-deliveries</code><span>Webhook delivery log</span></p></div>
    <div class="api-endpoints" data-api-endpoints="reports" hidden><p><em class="get">GET</em><code>/v1/reports</code><span>Performance reports</span></p><p><em class="get">GET</em><code>/v1/revenue</code><span>Revenue reports</span></p><p><em class="get">GET</em><code>/v1/settlements</code><span>Settlement status</span></p></div>
  </div></div></div></section>

  <section class="section dark api-flow-section" id="api-flow"><div class="container"><div class="section-head reveal"><span class="eyebrow light">END-TO-END FLOW</span><h2>一套接口贯穿完整发行链路</h2><p>对外使用统一的资源模型；底层发行链路由内容与文件准备、K-JSON 任务、渠道传输和结果查询组成。</p></div><div class="api-flow reveal"><article><b>01</b><h3>认证与基础配置</h3><p>获取访问凭证，并读取地区、语言、角色等发行基础数据。</p></article><article><b>02</b><h3>同步内容与文件</h3><p>建立艺人、专辑、歌曲与文件对象，准备 UPC、ISRC、封面和音频等资料。</p></article><article><b>03</b><h3>创建并提交发行</h3><p>配置 DSP、发行日期、地区与可用期，创建发行任务；底层生成标准 K-JSON 进入发行链路。</p></article><article><b>04</b><h3>获取渠道状态</h3><p>按任务、批次或 Catalog Number 查询入库与各 DSP 的上架、失败和处理中状态。</p></article><article><b>05</b><h3>持续管理与数据</h3><p>支持后续更新、下架，并按合作范围接入平台数据、收入和结算结果。</p></article></div></div></section>

  <section class="api-event-band"><div class="container"><div class="api-event-layout reveal"><div><span class="eyebrow light">WEBHOOK EVENT STREAM</span><h2>关键发行状态实时回传</h2><p>Open API V1 将发行任务与平台结果统一为事件回调，减少持续轮询，并与现有产品状态保持同步。</p><a class="text-link light-link" href="/enterprise/developers#webhook" data-route>查看 Webhook 设计 →</a></div><div class="event-stream"><div><time>10:32:05</time><i></i><p><b>distribution.created</b><span>dist_4821 · accepted</span></p><em>200</em></div><div><time>10:32:21</time><i></i><p><b>platform.processing</b><span>Spotify · processing</span></p><em>200</em></div><div><time>10:33:08</time><i class="ok"></i><p><b>platform.live</b><span>Apple Music · platform album id ready</span></p><em>200</em></div><div><time>10:36:42</time><i class="warn"></i><p><b>platform.failed</b><span>QQ Music · fail code returned</span></p><em>200</em></div></div></div></div></section>

  <section class="section soft api-dev-section" id="api-developer"><div class="container"><div class="section-head reveal"><span class="eyebrow">DEVELOPER EXPERIENCE</span><h2>从已跑通发行链路，扩展为完整 Open API</h2><p>现有认证、STS 上传、K-JSON 任务与发行结果查询作为真实发行底座；艺人、专辑、歌曲等现有业务接口统一封装开放，并补齐 Webhook、日志、用量和版本管理。</p></div><div class="feature-grid api-dev-grid reveal"><article><b>01 · SANDBOX</b><h3>测试环境</h3><p>使用现有测试环境完成认证、文件上传、发行任务与结果查询的真实联调。</p></article><article><b>02 · CREDENTIALS</b><h3>凭证与权限</h3><p>通过 appKey、appSecret 获取 accessToken，并根据企业合作范围控制资源与接口权限。</p></article><article><b>03 · K-JSON</b><h3>专业发行协议</h3><p>保留 K-JSON 作为批量和高级发行能力，覆盖资源、艺人、DSP、地区、发行时间与商业模式。</p></article><article><b>04 · WEBHOOK</b><h3>事件回调</h3><p>统一补齐发行与平台状态事件、签名校验、重试机制和投递记录。</p></article><article><b>05 · OBSERVABILITY</b><h3>日志与 Request ID</h3><p>补齐请求日志、Webhook 投递日志与 Request ID，形成可追踪的企业级排障链路。</p></article><article><b>06 · VERSIONING</b><h3>版本与变更记录</h3><p>以 /v1 为稳定 Public API 契约，并通过 Changelog 管理字段、枚举和行为变更。</p></article></div><div class="api-doc-row reveal"><div><b>Developer Documentation</b><span>开发者中心已按真实发行网关、Public Resource API、K-JSON 与 V1 配套能力重新组织。</span></div><a class="text-link" href="/enterprise/developers" data-route>查看开发者指南 →</a></div></div></section>

  <section class="section" id="api-integration"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">INTEGRATION OPTIONS</span><h2>兼容实时 API 与批量数据交换</h2></div><p>根据业务实时性、数据规模及既有技术体系，可选择 API、Excel、SFTP、XML、DDEX 或 K-JSON，支持从标准批量导入到行业级数据交换。</p></div><div class="method-grid api-method-grid reveal"><div class="primary"><small>REAL-TIME</small><b>API</b><span>适用于网站、App、SaaS 与内部系统的实时业务集成。</span></div><div><small>STANDARD RELEASE</small><b>K-JSON</b><span>适用于完整发行数据、批量任务及高级系统级发行接入。</span></div><div><small>BATCH</small><b>Excel</b><span>适用于标准模板下的内容、元数据与发行信息批量导入。</span></div><div><small>FILE EXCHANGE</small><b>SFTP</b><span>适用于大批量文件、音频素材及配套数据的稳定交换。</span></div><div><small>STRUCTURED DATA</small><b>XML</b><span>适用于企业已有结构化数据流与批量业务系统对接。</span></div><div><small>INDUSTRY STANDARD</small><b>DDEX</b><span>适用于采用音乐行业标准协议的大规模专业发行数据交换。</span></div></div></div></section>

  <section class="section soft api-commercial-section" id="api-pricing"><div class="container"><div class="section-head split reveal"><div><span class="eyebrow">COMMERCIAL MODEL</span><h2>清晰的 API 商业方案</h2></div><p>按年开通 API 服务，并按照实际发行使用量计费；大型或复杂集成项目可结合企业版与专项实施服务。</p></div><div class="api-commercial-card reveal"><div class="api-commercial-prices"><div><span>API 服务年费</span><strong>¥9,800<small>/年起</small></strong></div><i>+</i><div><span>发行使用费</span><strong>¥1<small>/首/渠道</small></strong></div></div><div class="api-commercial-includes"><span>发行 API 接入权限</span><span>内容与发行核心能力</span><span>测试环境与开发者指南</span><span>接入联调与技术支持</span></div><div class="api-commercial-actions"><a class="btn btn-primary" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="text-link" href="/enterprise/pricing" data-route>查看完整价格说明 →</a></div><p class="api-commercial-note">具体接口范围、接入方式与服务等级以企业合作方案为准。发行使用量按“歌曲 × 实际目标平台”计算。</p></div></div></section>

  <section class="enterprise-contact-cta"><div class="container"><div class="enterprise-contact-panel reveal"><div><span class="eyebrow light">CONTACT SALES</span><h2>获取适配业务需求的企业发行方案</h2><p>提交基本业务信息，结合曲库规模、客户协作方式与系统集成需求，评估适合的产品版本、发行 API 或组合方案。</p></div><div class="enterprise-contact-actions"><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a></div></div></div></section>
</section>'''

dev_section = r'''<section class="page" data-page="developers">
  <section class="dev-shell"><button class="dev-mobile-nav" type="button" aria-expanded="false" aria-controls="developer-nav"><span>开发者中心目录</span><b>☰</b></button><aside class="dev-side" id="developer-nav"><div class="dev-side-title">开发者中心</div><b>开始</b><a href="#overview">概览</a><a href="#quickstart">Quick Start</a><a href="#authentication">认证</a><a href="#environment">环境</a><b>Public API</b><a href="#resources">资源 API</a><a href="#distribution">发行 API</a><a href="#files">文件上传</a><a href="#kjson">K-JSON</a><b>运行与事件</b><a href="#status">状态模型</a><a href="#webhook">Webhook</a><a href="#errors">错误与日志</a><a href="#reference">枚举与参考</a><a href="#support">技术支持</a></aside><article class="dev-main">

    <section id="overview"><span class="eyebrow">DEVELOPER CENTER</span><h1>Star Enterprise Open API</h1><p class="lead">面向发行商、唱片公司、版权公司、音乐平台与 SaaS 产品的企业级音乐发行接口。开发者中心以现有已跑通的发行网关为底座，同时将艺人、专辑、歌曲等业务能力标准化封装为 Public API。</p><div class="dev-actions"><a class="btn btn-primary" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-secondary" href="/enterprise/api" data-route>返回发行 API</a></div><div class="dev-notice"><b>文档状态说明</b><span>“发行网关”部分来自当前已跑通的真实链路；“Public Resource API / Webhook / Logs”按照 Open API V1 对外标准化设计，并以企业联调时开放的最终契约为准。</span></div></section>

    <section id="quickstart"><h2>Quick Start</h2><p>当前真实发行链路可按以下步骤完成一次完整发行：认证 → 获取 OSS 临时凭证 → 上传 K-JSON 与素材 → 创建 K-JSON 任务 → 查询导入与 DSP 发行结果。</p><div class="dev-steps"><div><b>1</b><span>GET /token</span></div><div><b>2</b><span>GET /oss/sts</span></div><div><b>3</b><span>Upload to OSS</span></div><div><b>4</b><span>POST /kjson/tasks</span></div><div><b>5</b><span>Query result</span></div></div><pre><code>GET /open/v1/token?appKey={appKey}&appSecret={appSecret}

Authorization: Bearer {accessToken}

GET  /open/v1/oss/sts
POST /open/v1/kjson/tasks
GET  /open/v1/kjson/tasks/{taskId}
GET  /open/v1/release/result/latest/{catalogNo}</code></pre><p class="caption">创建 K-JSON 任务的 taskId 返回结构在现有文档中尚未完整定义，联调时以实际环境返回为准。</p></section>

    <section id="authentication"><h2>认证</h2><p>使用企业开通时分配的 appKey 与 appSecret 获取 accessToken，后续请求通过 Bearer Token 认证。contentProvider 与 tenantkey 用于识别合作方与租户范围。</p><div class="doc-table"><div class="head"><b>字段</b><b>来源</b><b>用途</b></div><div><span>appKey / appSecret</span><span>商务开通后分配</span><span>换取 accessToken</span></div><div><span>accessToken</span><span>GET /token</span><span>Authorization: Bearer</span></div><div><span>contentProvider</span><span>平台开通时分配</span><span>识别 CP / 内容提供方</span></div><div><span>tenantkey</span><span>平台分配</span><span>租户标识，现有发行网关默认 star</span></div></div></section>

    <section id="environment"><h2>环境</h2><p>现有发行网关已提供测试环境；正式环境地址与生产凭证在项目开通及联调阶段提供。</p><div class="doc-table"><div class="head"><b>项目</b><b>测试环境</b><b>生产环境</b></div><div><span>Base URL</span><span>https://api.test.kanjian.com/open/v1</span><span>项目开通后提供</span></div><div><span>用途</span><span>接口联调与发行验证</span><span>正式发行</span></div><div><span>凭证</span><span>测试 appKey / appSecret</span><span>独立生产凭证</span></div></div></section>

    <section id="resources"><h2>Public Resource API</h2><p>现有内部艺人、专辑、歌曲、厂牌及基础字典能力，将统一按 Public API V1 封装，避免客户直接依赖内部 tenantKey、organizeId、Referer 等实现细节。</p><div class="resource-grid"><div><code>Artist</code><span>创建、查询、更新艺人与角色信息</span></div><div><code>Label</code><span>厂牌与发行品牌信息</span></div><div><code>Album</code><span>专辑 / 单曲及 UPC、发行元数据</span></div><div><code>Track</code><span>歌曲、ISRC、音频、歌词与贡献者</span></div><div><code>File</code><span>音频、封面与上传凭证</span></div><div><code>Reference</code><span>语言、地区、风格、角色与 DSP</span></div></div><h3>建议的 V1 资源接口</h3><pre><code>POST   /v1/artists
GET    /v1/artists
GET    /v1/artists/{artistId}
PATCH  /v1/artists/{artistId}

POST   /v1/albums
GET    /v1/albums
GET    /v1/albums/{albumId}
PATCH  /v1/albums/{albumId}

POST   /v1/tracks
GET    /v1/tracks
GET    /v1/tracks/{trackId}
PATCH  /v1/tracks/{trackId}

GET    /v1/reference/languages
GET    /v1/reference/territories
GET    /v1/reference/genres
GET    /v1/reference/roles</code></pre></section>

    <section id="distribution"><h2>发行 API</h2><p>对外以 Distribution 作为统一发行资源，屏蔽底层 K-JSON 任务编排；底层仍复用现有已经跑通的 K-JSON 导入与 DSP 传输链路。</p><pre><code>POST /v1/distributions
GET  /v1/distributions/{distributionId}
POST /v1/distributions/{distributionId}/update
POST /v1/distributions/{distributionId}/takedown
POST /v1/distributions/{distributionId}/takedown-all
GET  /v1/distributions/{distributionId}/platforms</code></pre><div class="doc-table"><div class="head"><b>操作</b><b>K-JSON 状态</b><b>说明</b></div><div><span>新增 / 首次提交</span><span>ContentState = INSERT</span><span>建立或新增发行内容</span></div><div><span>更新</span><span>ContentState = UPDATE</span><span>更新已有内容</span></div><div><span>上架</span><span>DSP = RELEASE</span><span>向指定 DSP 发行</span></div><div><span>下架</span><span>DSP = TAKE_DOWN</span><span>指定 DSP 下架</span></div><div><span>全部下架</span><span>DSP = TAKE_DOWN_ALL</span><span>全部目标平台下架</span></div></div></section>

    <section id="files"><h2>文件与 OSS 上传</h2><p>现有发行链路通过 STS 获取临时 OSS 凭证。返回信息包含 accessKeyId、accessKeySecret、region、stsToken、bucket 与 basePath，凭证有效期为 3600 秒。</p><pre><code>GET /open/v1/oss/sts
Authorization: Bearer {accessToken}

# 上传范围必须位于 STS 返回的 basePath 下
# 完成文件上传后，将批次路径提交给 /kjson/tasks</code></pre></section>

    <section id="kjson"><h2>K-JSON</h2><p>K-JSON V0.3.1 是现有发行链路的标准数据格式，适合批量与高级系统接入。Open API 的 Resource API 会降低日常接入复杂度，但 K-JSON 继续作为完整发行协议保留。</p><div class="resource-grid"><div><code>MessageHeader</code><span>租户、CP、UPC、任务与消息信息</span></div><div><code>Transfer State</code><span>内容新增 / 更新与 DSP 上下架操作</span></div><div><code>ResourceList</code><span>歌曲、音频、ISRC、角色、风格与版权信息</span></div><div><code>ArtistList</code><span>艺人、DSP 主页、翻译与厂牌信息</span></div><div><code>ReleaseList</code><span>DSP、日期、地区、有效期与商业模式</span></div></div><p>K-JSON 中的发行信息可配置目标 DSP、releaseDate、territoryCodes、validtyPeriod、CommercialModelTypes 与 Usage。</p></section>

    <section id="status"><h2>状态与发行结果</h2><p>当前发行网关支持按 taskId、batchPath 或 catalogNo 查询处理结果。平台级结果包括 status、dspId、dspName、platformAlbumId 与 failCode。</p><div class="doc-table"><div class="head"><b>状态</b><b>含义</b><b>场景</b></div><div><span>UP_RUNNING</span><span>处理中</span><span>入库 / 上架进行中</span></div><div><span>UP_SUCCESS</span><span>成功</span><span>入库 / 上架成功</span></div><div><span>UP_FAILED</span><span>失败</span><span>入库 / 上架失败</span></div><div><span>DOWN_RUNNING</span><span>下架中</span><span>下架任务处理中</span></div><div><span>DOWN_SUCCESS</span><span>下架成功</span><span>平台已完成下架</span></div><div><span>DOWN_FAILED</span><span>下架失败</span><span>下架任务失败</span></div></div></section>

    <section id="webhook"><h2>Webhook</h2><p>Open API V1 将现有查询式状态能力补充为事件回调。事件名称、签名和重试机制属于对外 V1 契约的一部分，在生产开放前固定版本。</p><pre><code>distribution.created
distribution.processing
distribution.completed
distribution.failed
platform.processing
platform.live
platform.failed
platform.takedown</code></pre><h3>V1 配套要求</h3><p>Webhook 需要包含 event_id、occurred_at、resource_id、event_type 与 payload；使用独立 Secret 完成签名校验，并保留投递记录与失败重试。</p></section>

    <section id="errors"><h2>错误与日志</h2><p>对外 V1 统一使用 HTTP 状态码 + 业务错误码，并补充 Request ID。现有 failCode 继续用于表达 DSP 发行失败信息。</p><div class="doc-table"><div class="head"><b>类型</b><b>需要查看</b><b>处理方式</b></div><div><span>认证 / 权限</span><span>HTTP 状态码、错误码</span><span>检查 Token 与接口权限</span></div><div><span>参数校验</span><span>字段路径与错误原因</span><span>修正请求后重试</span></div><div><span>发行处理</span><span>task / catalog / DSP 状态</span><span>等待处理或修正发行资料</span></div><div><span>DSP 失败</span><span>failCode、dspId</span><span>按平台要求修正后重新提交</span></div><div><span>系统异常</span><span>Request ID、时间</span><span>提交技术支持排查</span></div></div></section>

    <section id="reference"><h2>枚举与参考数据</h2><p>Public API 将地区、语言、风格、角色、DSP 与状态等字典作为 Reference API 统一开放，避免客户在代码中维护内部 ID。</p><div class="resource-grid"><div><code>Languages</code><span>语言与脚本代码</span></div><div><code>Territories</code><span>国家与地区</span></div><div><code>Genres</code><span>主风格与子风格</span></div><div><code>Roles</code><span>MainArtist、Lyricist、Composer 等</span></div><div><code>DSPs</code><span>目标发行平台</span></div><div><code>Status</code><span>发行与平台状态</span></div></div></section>

    <section id="support"><h2>技术支持</h2><p>接入前先在测试环境完成认证、上传、任务提交与结果查询；Resource API、Webhook 与生产凭证按企业合作范围开通。大型批量发行客户可继续使用 K-JSON、SFTP、XML 或 DDEX。</p><div class="hero-actions"><a class="btn btn-primary" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-secondary" href="/enterprise/api" data-route>返回发行 API</a></div></section>
  </article><aside class="dev-code-rail" aria-label="代码示例"><div class="dev-code-card"><div class="dev-code-card-head"><span>LIVE RELEASE GATEWAY</span><div><button class="active" type="button">cURL</button></div></div><pre><code>curl -X GET \
  'https://api.test.kanjian.com/open/v1/token?appKey=$APP_KEY&appSecret=$APP_SECRET'

# response
{
  "accessToken": "...",
  "expiresIn": 3600
}</code></pre><div class="dev-code-response"><span>200 OK</span><code>accessToken</code></div></div><div class="dev-code-card mini"><span>K-JSON</span><b>Release Gateway</b><small>已跑通的批量发行底座</small></div><div class="dev-code-card mini"><span>PUBLIC API V1</span><b>Resource Model</b><small>Artist · Album · Track · Distribution</small></div><div class="dev-code-card mini"><span>OBSERVABILITY</span><b>Webhook + Request ID</b><small>作为 V1 企业级配套能力补齐</small></div></aside></section>
  <section class="enterprise-contact-cta"><div class="container"><div class="enterprise-contact-panel reveal"><div><span class="eyebrow light">CONTACT SALES</span><h2>获取适配业务需求的企业发行方案</h2><p>提交基本业务信息，结合曲库规模、客户协作方式与系统集成需求，评估适合的产品版本、发行 API 或组合方案。</p></div><div class="enterprise-contact-actions"><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a></div></div></div></section>
</section>'''

new_html = html[:api_start] + api_section + '\n\n' + dev_section + '\n' + html[apply_start:]
INDEX.write_text(new_html, encoding='utf-8')
print('Updated API and Developer Center sections in prototype-v4/index.html')
