from pathlib import Path

index_path = Path('prototype-v4/index.html')
style_path = Path('prototype-v4/styles.css')

html = index_path.read_text(encoding='utf-8')
start = html.index('<section class="page" data-page="developers">')
end = html.index('<section class="page apply-page" data-page="apply">')

new_dev = r'''<section class="page" data-page="developers">
  <section class="dev-shell">
    <button class="dev-mobile-nav" type="button" aria-expanded="false" aria-controls="developer-nav"><span>开发者中心目录</span><b>☰</b></button>
    <aside class="dev-side" id="developer-nav">
      <div class="dev-side-title">开发者中心</div>
      <b>开始</b>
      <a href="#overview">概览</a>
      <a href="#quickstart">快速开始</a>
      <a href="#authentication">身份认证</a>
      <a href="#environment">环境与凭证</a>

      <b>API 参考</b>
      <a href="#artists">艺人</a>
      <a href="#labels">厂牌</a>
      <a href="#albums">专辑</a>
      <a href="#tracks">歌曲</a>
      <a href="#files">文件</a>
      <a href="#distributions">发行</a>
      <a href="#release-status">发行状态</a>
      <a href="#reference-data">参考数据</a>

      <b>发行指南</b>
      <a href="#guide-create">创建内容</a>
      <a href="#guide-submit">提交发行</a>
      <a href="#guide-update">更新发行</a>
      <a href="#guide-takedown">下架</a>
      <a href="#guide-batch">批量发行</a>
      <a href="#guide-kjson">K-JSON</a>

      <b>事件</b>
      <a href="#webhooks">事件回调</a>
      <a href="#event-types">事件类型</a>
      <a href="#signature">签名校验</a>

      <b>参考</b>
      <a href="#territories">国家与地区</a>
      <a href="#languages">语言</a>
      <a href="#genres">音乐风格</a>
      <a href="#roles">角色</a>
      <a href="#dsps">发行平台</a>
      <a href="#statuses">状态码</a>
      <a href="#error-codes">错误码</a>
      <a href="#changelog">更新记录</a>
    </aside>

    <article class="dev-main">
      <section id="overview">
        <span class="eyebrow">开发者中心</span>
        <h1>企业发行 Open API</h1>
        <p class="lead">用于将艺人、厂牌、专辑、歌曲、文件、发行任务和平台状态接入企业现有网站、App、SaaS 或内部系统。建议按照“内容准备 → 发行提交 → 状态回传 → 更新 / 下架”的业务顺序接入。</p>
        <div class="dev-actions"><a class="btn btn-primary" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-secondary" href="/enterprise/api" data-route>返回发行 API</a></div>
        <div class="dev-notice"><b>文档说明</b><span>认证、OSS 临时凭证、K-JSON 任务和发行结果查询来自当前已跑通的真实发行链路；艺人、厂牌、专辑、歌曲、统一发行资源与事件回调按照 Open API V1 对外标准进行封装。文档中会明确标注“当前可用”与“V1 规划”。</span></div>
        <div class="dev-paths">
          <article><small>推荐接入</small><h3>标准资源 API</h3><p>按艺人、专辑、歌曲、发行等业务对象接入，适合网站、App、音乐 SaaS 与内容平台。</p><span>艺人 → 专辑 → 歌曲 → 文件 → 发行 → 平台状态</span></article>
          <article><small>批量 / 高级接入</small><h3>K-JSON 发行链路</h3><p>直接提交完整发行数据与素材，适合大型发行商、大曲库迁移和批量系统对接。</p><span>认证 → STS → OSS → K-JSON → 任务 → 结果</span></article>
        </div>
      </section>

      <section id="quickstart">
        <div class="dev-section-kicker">开始</div><h2>快速开始</h2>
        <p>一次完整发行通常需要先准备内容对象，再创建发行任务。当前真实发行网关已经可以完成认证、文件上传、K-JSON 提交和结果查询；标准资源 API 会在此基础上降低接入复杂度。</p>
        <div class="dev-steps"><div><b>1</b><span>获取访问凭证</span></div><div><b>2</b><span>创建内容资料</span></div><div><b>3</b><span>上传音频与封面</span></div><div><b>4</b><span>提交发行任务</span></div><div><b>5</b><span>查询平台状态</span></div></div>
        <h3>当前可用的发行网关</h3>
        <pre><code>GET  /open/v1/token
GET  /open/v1/oss/sts
POST /open/v1/kjson/tasks
GET  /open/v1/kjson/tasks/{taskId}
GET  /open/v1/release/result/latest/{catalogNo}</code></pre>
        <p class="caption">创建 K-JSON 任务后的 taskId 返回结构在现有文档中尚未完整定义，联调时以实际测试环境返回为准。</p>
      </section>

      <section id="authentication">
        <h2>身份认证</h2><div class="dev-state"><span class="current">当前可用</span></div>
        <p>使用企业开通时分配的 <code>appKey</code> 与 <code>appSecret</code> 获取 <code>accessToken</code>，后续请求通过 Bearer Token 认证。</p>
        <pre><code>GET /open/v1/token?appKey={appKey}&amp;appSecret={appSecret}

Authorization: Bearer {accessToken}</code></pre>
        <div class="doc-table"><div class="head"><b>字段</b><b>来源</b><b>用途</b></div><div><span>appKey / appSecret</span><span>企业开通后分配</span><span>换取访问令牌</span></div><div><span>accessToken</span><span>认证接口返回</span><span>后续接口鉴权</span></div><div><span>contentProvider</span><span>平台配置</span><span>现有发行网关识别内容提供方</span></div><div><span>tenantkey</span><span>平台配置</span><span>现有发行网关租户标识；标准资源 API 将尽量由凭证上下文自动识别</span></div></div>
      </section>

      <section id="environment">
        <h2>环境与凭证</h2><div class="dev-state"><span class="current">测试环境已提供</span></div>
        <p>测试环境用于完成认证、上传、发行任务与结果查询。生产环境与正式凭证在企业合作和联调阶段开通。</p>
        <div class="doc-table"><div class="head"><b>项目</b><b>测试环境</b><b>生产环境</b></div><div><span>发行网关地址</span><span>https://api.test.kanjian.com/open/v1</span><span>项目开通后提供</span></div><div><span>用途</span><span>接口联调与发行验证</span><span>真实业务发行</span></div><div><span>凭证</span><span>测试 appKey / appSecret</span><span>独立生产凭证</span></div></div>
        <p class="caption">标准资源 API 的正式 Base URL 会在 V1 对外开放时统一提供，不与现有内部接口地址直接绑定。</p>
      </section>

      <section id="artists">
        <div class="dev-section-kicker">API 参考</div><h2>艺人</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>创建和维护发行中使用的艺人资料，包括艺名、语种、角色及平台艺人信息。对外接口由现有艺人能力标准化封装。</p>
        <div class="dev-endpoints"><div><b>POST</b><code>/v1/artists</code><span>创建艺人</span></div><div><b class="get">GET</b><code>/v1/artists</code><span>查询艺人列表</span></div><div><b class="get">GET</b><code>/v1/artists/{artistId}</code><span>查询艺人详情</span></div><div><b class="patch">PATCH</b><code>/v1/artists/{artistId}</code><span>更新艺人</span></div></div>
      </section>

      <section id="labels">
        <h2>厂牌</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>维护发行品牌、版权方或厂牌信息，并与专辑和发行内容建立关联。</p>
        <div class="dev-endpoints"><div><b>POST</b><code>/v1/labels</code><span>创建厂牌</span></div><div><b class="get">GET</b><code>/v1/labels</code><span>查询厂牌列表</span></div><div><b class="get">GET</b><code>/v1/labels/{labelId}</code><span>查询厂牌详情</span></div><div><b class="patch">PATCH</b><code>/v1/labels/{labelId}</code><span>更新厂牌</span></div></div>
      </section>

      <section id="albums">
        <h2>专辑</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>创建专辑或单曲版本，并维护 UPC、封面、发行日期、厂牌、版权声明、曲目关系等发行元数据。</p>
        <div class="dev-endpoints"><div><b>POST</b><code>/v1/albums</code><span>创建专辑 / 单曲</span></div><div><b class="get">GET</b><code>/v1/albums</code><span>查询专辑列表</span></div><div><b class="get">GET</b><code>/v1/albums/{albumId}</code><span>查询专辑详情</span></div><div><b class="patch">PATCH</b><code>/v1/albums/{albumId}</code><span>更新专辑</span></div></div>
        <p class="caption">现有业务模型已包含标题、封面、UPC、发行日期、厂牌、目录号、C-Line / P-Line 与曲目关联等信息。</p>
      </section>

      <section id="tracks">
        <h2>歌曲</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>维护歌曲标题、ISRC、音频、歌词、语种、音乐风格、艺人与词曲作者等信息，并关联所属专辑。</p>
        <div class="dev-endpoints"><div><b>POST</b><code>/v1/tracks</code><span>创建歌曲</span></div><div><b class="get">GET</b><code>/v1/tracks</code><span>查询歌曲列表</span></div><div><b class="get">GET</b><code>/v1/tracks/{trackId}</code><span>查询歌曲详情</span></div><div><b class="patch">PATCH</b><code>/v1/tracks/{trackId}</code><span>更新歌曲</span></div></div>
      </section>

      <section id="files">
        <h2>文件</h2><div class="dev-state"><span class="current">当前可用</span></div>
        <p>发行链路通过 STS 获取临时 OSS 凭证，用于上传音频、封面、K-JSON 与批次文件。上传路径必须位于返回的 <code>basePath</code> 下。</p>
        <pre><code>GET /open/v1/oss/sts
Authorization: Bearer {accessToken}</code></pre>
        <div class="doc-table"><div class="head"><b>返回字段</b><b>说明</b><b>备注</b></div><div><span>accessKeyId / accessKeySecret</span><span>临时访问凭证</span><span>仅用于本次授权范围</span></div><div><span>stsToken</span><span>临时安全令牌</span><span>与访问凭证配套使用</span></div><div><span>region / bucket</span><span>存储区域与桶</span><span>按返回值上传</span></div><div><span>basePath</span><span>允许上传的基础路径</span><span>不可越权写入其他目录</span></div><div><span>有效期</span><span>3600 秒</span><span>过期后重新获取</span></div></div>
      </section>

      <section id="distributions">
        <h2>发行</h2><div class="dev-state"><span class="planned">V1 统一资源</span><span class="current">底层链路已跑通</span></div>
        <p>对外统一使用“发行”资源，屏蔽底层 K-JSON 任务编排。创建发行时配置目标平台、发行日期、地区与可用期；后续更新和下架继续围绕同一个发行对象操作。</p>
        <div class="dev-endpoints"><div><b>POST</b><code>/v1/distributions</code><span>创建并提交发行</span></div><div><b class="get">GET</b><code>/v1/distributions/{distributionId}</code><span>查询发行详情</span></div><div><b>POST</b><code>/v1/distributions/{distributionId}/update</code><span>更新发行</span></div><div><b>POST</b><code>/v1/distributions/{distributionId}/takedown</code><span>指定平台下架</span></div><div><b>POST</b><code>/v1/distributions/{distributionId}/takedown-all</code><span>全部平台下架</span></div></div>
        <div class="doc-table"><div class="head"><b>对外操作</b><b>底层 K-JSON</b><b>说明</b></div><div><span>新建内容</span><span>ContentState = INSERT</span><span>新增发行内容</span></div><div><span>更新内容</span><span>ContentState = UPDATE</span><span>更新已有内容</span></div><div><span>上架</span><span>DSP = RELEASE</span><span>向指定发行平台提交</span></div><div><span>下架</span><span>DSP = TAKE_DOWN</span><span>指定平台下架</span></div><div><span>全部下架</span><span>DSP = TAKE_DOWN_ALL</span><span>全部目标平台下架</span></div></div>
      </section>

      <section id="release-status">
        <h2>发行状态</h2><div class="dev-state"><span class="current">当前查询能力可用</span><span class="planned">V1 统一状态接口</span></div>
        <p>当前发行网关支持按 taskId、batchPath 或 catalogNo 查询处理结果；标准资源 API 会统一为发行对象及平台级状态。</p>
        <pre><code>GET /open/v1/kjson/tasks/{taskId}
GET /open/v1/kjson/tasks?batchPath={batchPath}
GET /open/v1/release/result/latest/{catalogNo}

# V1 统一接口
GET /v1/distributions/{distributionId}/platforms</code></pre>
        <p>平台级结果至少包含 <code>status</code>、<code>dspId</code>、<code>dspName</code>、<code>platformAlbumId</code> 与 <code>failCode</code>。</p>
      </section>

      <section id="reference-data">
        <h2>参考数据</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>语言、地区、音乐风格、角色与发行平台统一通过参考数据接口读取，避免客户在代码中长期维护内部 ID。</p>
        <div class="dev-endpoints"><div><b class="get">GET</b><code>/v1/reference/languages</code><span>语言</span></div><div><b class="get">GET</b><code>/v1/reference/territories</code><span>国家与地区</span></div><div><b class="get">GET</b><code>/v1/reference/genres</code><span>音乐风格</span></div><div><b class="get">GET</b><code>/v1/reference/roles</code><span>贡献者角色</span></div><div><b class="get">GET</b><code>/v1/reference/dsps</code><span>发行平台</span></div></div>
      </section>

      <section id="guide-create">
        <div class="dev-section-kicker">发行指南</div><h2>创建内容</h2>
        <p>标准接入建议先建立可复用的内容对象，再创建发行任务。这样艺人、厂牌、专辑与歌曲可以在后续更新、重发和多版本发行中持续复用。</p>
        <div class="dev-flow-line"><span>艺人</span><i>→</i><span>厂牌</span><i>→</i><span>专辑</span><i>→</i><span>歌曲</span><i>→</i><span>音频 / 封面</span></div>
        <div class="doc-table"><div class="head"><b>对象</b><b>关键标识</b><b>主要内容</b></div><div><span>艺人</span><span>artistId</span><span>艺名、语种、角色、平台艺人信息</span></div><div><span>专辑</span><span>albumId / UPC</span><span>标题、封面、厂牌、发行日期、版权声明</span></div><div><span>歌曲</span><span>trackId / ISRC</span><span>标题、音频、歌词、艺人、词曲作者、风格</span></div><div><span>文件</span><span>上传路径</span><span>音频、封面及发行批次文件</span></div></div>
      </section>

      <section id="guide-submit">
        <h2>提交发行</h2>
        <p>内容准备完成后创建发行任务，选择目标发行平台、发行日期和地区。标准资源 API 会由服务端生成底层 K-JSON 并进入现有发行链路。</p>
        <pre><code>POST /v1/distributions
{
  "album_id": "alb_xxx",
  "platforms": ["spotify", "apple_music", "qq_music"],
  "release_date": "2026-10-02",
  "territories": ["WORLDWIDE"]
}</code></pre>
        <p class="caption">以上为 V1 对外资源模型示例；最终字段命名与枚举以正式开放契约为准。</p>
      </section>

      <section id="guide-update">
        <h2>更新发行</h2>
        <p>发行后的元数据、文件或平台配置发生变化时，通过原发行对象提交更新。底层对应 <code>ContentState = UPDATE</code>，并继续复用原有发行关系。</p>
        <pre><code>POST /v1/distributions/{distributionId}/update</code></pre>
        <p>建议在更新前先读取当前发行详情与平台状态，避免对仍在处理中的任务重复提交冲突操作。</p>
      </section>

      <section id="guide-takedown">
        <h2>下架</h2>
        <p>支持指定发行平台下架和全部平台下架。底层分别映射到 <code>TAKE_DOWN</code> 与 <code>TAKE_DOWN_ALL</code>。</p>
        <pre><code>POST /v1/distributions/{distributionId}/takedown
POST /v1/distributions/{distributionId}/takedown-all</code></pre>
        <p>下架同样是异步任务，需要继续查询平台状态或通过事件回调获取最终处理结果。</p>
      </section>

      <section id="guide-batch">
        <h2>批量发行</h2><div class="dev-state"><span class="current">K-JSON 链路当前可用</span></div>
        <p>大批量目录、历史曲库迁移或系统级发行可直接采用 K-JSON。典型流程为获取凭证、获取 STS、上传批次、创建任务并查询处理结果。</p>
        <div class="dev-flow-line"><span>认证</span><i>→</i><span>STS</span><i>→</i><span>OSS 上传</span><i>→</i><span>K-JSON 任务</span><i>→</i><span>发行结果</span></div>
        <pre><code>GET  /open/v1/token
GET  /open/v1/oss/sts
POST /open/v1/kjson/tasks
GET  /open/v1/kjson/tasks/{taskId}
GET  /open/v1/release/result/latest/{catalogNo}</code></pre>
      </section>

      <section id="guide-kjson">
        <h2>K-JSON</h2><div class="dev-state"><span class="current">V0.3.1</span></div>
        <p>K-JSON 是现有发行链路使用的完整发行数据格式，继续作为批量和高级系统接入协议保留。</p>
        <div class="resource-grid"><div><code>MessageHeader</code><span>租户、内容提供方、UPC、任务与消息信息</span></div><div><code>传输状态</code><span>内容新增 / 更新与平台上架 / 下架操作</span></div><div><code>ResourceList</code><span>歌曲、音频、ISRC、角色、风格与版权信息</span></div><div><code>ArtistList</code><span>艺人、平台主页、翻译与厂牌信息</span></div><div><code>ReleaseList</code><span>发行平台、日期、地区、有效期与商业模式</span></div></div>
        <p>K-JSON 的发行信息可配置目标平台、<code>releaseDate</code>、<code>territoryCodes</code>、<code>validtyPeriod</code>、<code>CommercialModelTypes</code> 与 <code>Usage</code>。</p>
      </section>

      <section id="webhooks">
        <div class="dev-section-kicker">事件</div><h2>事件回调</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>事件回调用于把发行任务和各平台处理结果主动推送到客户系统，减少持续轮询。V1 会提供回调地址管理、投递记录与失败重试。</p>
        <div class="dev-endpoints"><div><b>POST</b><code>/v1/webhooks</code><span>创建回调地址</span></div><div><b class="get">GET</b><code>/v1/webhooks</code><span>查询回调配置</span></div><div><b class="delete">DELETE</b><code>/v1/webhooks/{webhookId}</code><span>删除回调地址</span></div></div>
      </section>

      <section id="event-types">
        <h2>事件类型</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>事件名保持稳定的机器可读格式，中文文档解释其业务含义。</p>
        <div class="doc-table"><div class="head"><b>事件</b><b>中文含义</b><b>触发场景</b></div><div><span>distribution.created</span><span>发行已创建</span><span>发行任务创建成功</span></div><div><span>distribution.processing</span><span>发行处理中</span><span>发行链路正在处理</span></div><div><span>distribution.completed</span><span>发行任务完成</span><span>任务级处理完成</span></div><div><span>distribution.failed</span><span>发行任务失败</span><span>任务级异常</span></div><div><span>platform.processing</span><span>平台处理中</span><span>单个平台正在处理</span></div><div><span>platform.live</span><span>平台已上线</span><span>单个平台已完成上架</span></div><div><span>platform.failed</span><span>平台处理失败</span><span>返回平台失败原因</span></div><div><span>platform.takedown</span><span>平台已下架</span><span>下架完成</span></div></div>
      </section>

      <section id="signature">
        <h2>签名校验</h2><div class="dev-state"><span class="planned">V1 规划</span></div>
        <p>Webhook 会使用独立 Secret 对回调请求进行签名，客户服务端应先验证签名再处理事件，并使用事件 ID 做幂等去重。</p>
        <div class="doc-table"><div class="head"><b>要求</b><b>作用</b><b>说明</b></div><div><span>独立 Secret</span><span>验证回调来源</span><span>与 API 访问凭证分离</span></div><div><span>时间戳</span><span>降低重放风险</span><span>校验允许的时间窗口</span></div><div><span>event_id</span><span>幂等去重</span><span>同一事件只处理一次</span></div><div><span>失败重试</span><span>提高投递可靠性</span><span>非 2xx 响应进入重试</span></div></div>
        <p class="caption">具体签名算法与 Header 名称会在 V1 正式契约中固定，当前资料尚未提供已上线的签名规范。</p>
      </section>

      <section id="territories">
        <div class="dev-section-kicker">参考</div><h2>国家与地区</h2><div class="dev-state"><span class="planned">V1 参考数据</span></div>
        <p>用于定义发行可用地区、限制地区和平台覆盖范围。建议通过参考数据接口实时读取，不在客户系统中长期写死内部 ID。</p>
        <pre><code>GET /v1/reference/territories</code></pre>
      </section>

      <section id="languages">
        <h2>语言</h2><div class="dev-state"><span class="planned">V1 参考数据</span></div>
        <p>用于艺人、专辑、歌曲与歌词等内容的语种标识。正式接口会返回稳定代码和展示名称。</p>
        <pre><code>GET /v1/reference/languages</code></pre>
      </section>

      <section id="genres">
        <h2>音乐风格</h2><div class="dev-state"><span class="planned">V1 参考数据</span></div>
        <p>用于专辑和歌曲的主风格、子风格等分类。不同平台对风格的支持可能存在差异，提交前由发行校验统一处理。</p>
        <pre><code>GET /v1/reference/genres</code></pre>
      </section>

      <section id="roles">
        <h2>角色</h2><div class="dev-state"><span class="planned">V1 参考数据</span></div>
        <p>用于表达主艺人、伴唱艺人、作词、作曲等参与关系。现有业务模型已使用角色信息组织艺人和创作者。</p>
        <pre><code>GET /v1/reference/roles</code></pre>
      </section>

      <section id="dsps">
        <h2>发行平台</h2><div class="dev-state"><span class="planned">V1 参考数据</span></div>
        <p>返回可选择的目标发行平台及稳定平台代码，用于创建发行任务和查询平台状态。</p>
        <pre><code>GET /v1/reference/dsps</code></pre>
      </section>

      <section id="statuses">
        <h2>状态码</h2><div class="dev-state"><span class="current">当前发行网关</span></div>
        <div class="doc-table"><div class="head"><b>状态</b><b>中文含义</b><b>业务场景</b></div><div><span>UP_RUNNING</span><span>上架处理中</span><span>入库 / 上架进行中</span></div><div><span>UP_SUCCESS</span><span>上架成功</span><span>入库 / 上架成功</span></div><div><span>UP_FAILED</span><span>上架失败</span><span>入库 / 上架失败</span></div><div><span>DOWN_RUNNING</span><span>下架处理中</span><span>下架任务处理中</span></div><div><span>DOWN_SUCCESS</span><span>下架成功</span><span>平台已完成下架</span></div><div><span>DOWN_FAILED</span><span>下架失败</span><span>下架任务失败</span></div></div>
      </section>

      <section id="error-codes">
        <h2>错误码</h2><div class="dev-state"><span class="planned">V1 统一错误模型</span></div>
        <p>对外 V1 使用 HTTP 状态码 + 业务错误码 + Request ID。现有发行结果中的 <code>failCode</code> 继续用于表达具体平台失败原因。</p>
        <div class="doc-table"><div class="head"><b>类型</b><b>需要查看</b><b>处理方式</b></div><div><span>认证 / 权限</span><span>HTTP 状态码、业务错误码</span><span>检查令牌和接口权限</span></div><div><span>参数校验</span><span>字段路径与错误原因</span><span>修正请求后重试</span></div><div><span>发行处理</span><span>任务、目录号、平台状态</span><span>等待处理或修正发行资料</span></div><div><span>平台失败</span><span>failCode、dspId</span><span>按平台要求修正后重新提交</span></div><div><span>系统异常</span><span>Request ID、请求时间</span><span>提交技术支持排查</span></div></div>
      </section>

      <section id="changelog">
        <h2>更新记录</h2><div class="dev-state"><span class="planned">V1 版本管理</span></div>
        <p>Open API 以 <code>/v1</code> 作为稳定版本边界。新增字段、枚举扩展、行为调整和废弃计划会在更新记录中统一说明，避免企业接入方因接口变化被动修改。</p>
        <div class="dev-notice"><b>版本原则</b><span>兼容性新增优先在当前版本内演进；存在破坏性变更时进入新的主版本，并提前提供迁移说明与过渡期。</span></div>
        <div class="hero-actions"><a class="btn btn-primary" href="/enterprise/apply?solution=api" data-route>申请 API 接入</a><a class="btn btn-secondary" href="/enterprise/api" data-route>返回发行 API</a></div>
      </section>
    </article>
  </section>
  <section class="enterprise-contact-cta"><div class="container"><div class="enterprise-contact-panel reveal"><div><span class="eyebrow light">企业合作</span><h2>获取适配业务需求的企业发行方案</h2><p>提交基本业务信息，结合曲库规模、客户协作方式与系统集成需求，评估适合的产品版本、发行 API 或组合方案。</p></div><div class="enterprise-contact-actions"><a class="btn btn-white btn-lg" href="/enterprise/apply" data-route>申请企业方案</a></div></div></div></section>
</section>
'''

html = html[:start] + new_dev + html[end:]
# 中文化 API 页面中与开发者相关的辅助标签，不改动原有核心市场文案。
replacements = {
    'END-TO-END FLOW': '完整发行链路',
    'WEBHOOK EVENT STREAM': '事件回调',
    'DEVELOPER EXPERIENCE': '开发者支持',
    'Developer Documentation': '开发者文档',
    '01 · SANDBOX': '01 · 测试环境',
    '02 · CREDENTIALS': '02 · 凭证与权限',
    '03 · K-JSON': '03 · K-JSON',
    '04 · WEBHOOK': '04 · 事件回调',
    '05 · OBSERVABILITY': '05 · 日志追踪',
    '06 · VERSIONING': '06 · 版本管理',
    'INTEGRATION OPTIONS': '接入方式',
    'COMMERCIAL MODEL': '商业方案',
}
for old, new in replacements.items():
    html = html.replace(old, new)
index_path.write_text(html, encoding='utf-8')

css = style_path.read_text(encoding='utf-8')
marker = '/* Developer Center Chinese IA */'
if marker not in css:
    css += r'''

/* Developer Center Chinese IA */
[data-page="developers"] .dev-shell{display:grid;grid-template-columns:230px minmax(0,1fr);max-width:var(--max);margin:0 auto;padding:0 28px;min-height:calc(100vh - 72px)}
[data-page="developers"] .dev-side{position:sticky;top:72px;height:calc(100vh - 72px);padding:30px 22px 40px 0;border-right:1px solid var(--line);overflow:auto}
[data-page="developers"] .dev-side-title{font-size:17px;font-weight:850;margin-bottom:20px}
[data-page="developers"] .dev-side>b{display:block;margin:22px 0 7px;color:#9aa3b1;font-size:10px;letter-spacing:.08em}
[data-page="developers"] .dev-side a{display:block;padding:7px 10px;border-radius:7px;color:#667284;font-size:12px;line-height:1.35}
[data-page="developers"] .dev-side a:hover{background:#f3f6fa;color:var(--ink)}
[data-page="developers"] .dev-main{max-width:none;min-width:0;padding:70px 0 100px 54px}
[data-page="developers"] .dev-main section{padding:0 0 54px;margin-bottom:48px;border-bottom:1px solid var(--line);scroll-margin-top:102px}
[data-page="developers"] .dev-main section:last-child{border-bottom:0}
[data-page="developers"] .dev-main h1{margin:0 0 18px;font-size:48px;line-height:1.08;letter-spacing:-.05em}
[data-page="developers"] .dev-main h2{margin:0 0 14px;font-size:30px;letter-spacing:-.035em}
[data-page="developers"] .dev-main h3{margin:28px 0 10px;font-size:17px}
[data-page="developers"] .dev-main p{max-width:820px;color:#667285;font-size:14px;line-height:1.82}
[data-page="developers"] .dev-main .lead{max-width:830px;font-size:17px;line-height:1.8}
[data-page="developers"] .dev-code-rail{display:none!important}
[data-page="developers"] .dev-section-kicker{margin-bottom:10px;color:var(--blue);font-size:10px;font-weight:850;letter-spacing:.08em}
[data-page="developers"] .dev-state{display:flex;gap:7px;flex-wrap:wrap;margin:-4px 0 18px}
[data-page="developers"] .dev-state span{display:inline-flex;padding:5px 8px;border-radius:999px;font-size:9px;font-weight:800}
[data-page="developers"] .dev-state .current{background:#eef8f3;color:#177a4f}
[data-page="developers"] .dev-state .planned{background:#edf2ff;color:#3158c8}
[data-page="developers"] .dev-paths{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:28px}
[data-page="developers"] .dev-paths article{padding:22px;border:1px solid var(--line);border-radius:14px;background:#fff}
[data-page="developers"] .dev-paths small{color:#8c97a8;font-size:9px;font-weight:800;letter-spacing:.06em}
[data-page="developers"] .dev-paths h3{margin:9px 0 8px;font-size:18px}
[data-page="developers"] .dev-paths p{margin:0;font-size:12px;line-height:1.65}
[data-page="developers"] .dev-paths span{display:block;margin-top:16px;padding-top:14px;border-top:1px solid #edf0f4;color:#53617a;font-size:11px;font-weight:750}
[data-page="developers"] .dev-endpoints{margin-top:20px;border:1px solid var(--line);border-radius:13px;overflow:hidden;background:#fff}
[data-page="developers"] .dev-endpoints>div{display:grid;grid-template-columns:66px minmax(240px,.9fr) 1fr;gap:12px;align-items:center;padding:13px 15px;border-bottom:1px solid #edf0f4}
[data-page="developers"] .dev-endpoints>div:last-child{border-bottom:0}
[data-page="developers"] .dev-endpoints b{justify-self:start;padding:4px 7px;border-radius:5px;background:#eaf0ff;color:#3158c8;font-size:8px;font-weight:900}
[data-page="developers"] .dev-endpoints b.get{background:#e9f8f1;color:#187d58}
[data-page="developers"] .dev-endpoints b.patch{background:#fff4df;color:#9a6700}
[data-page="developers"] .dev-endpoints b.delete{background:#fff0f0;color:#b64242}
[data-page="developers"] .dev-endpoints code{color:#293750;font-size:11px;font-weight:700;overflow-wrap:anywhere}
[data-page="developers"] .dev-endpoints span{color:#8792a3;font-size:10px}
[data-page="developers"] .dev-flow-line{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:22px 0;padding:18px;border:1px solid #dfe5ef;border-radius:12px;background:#fafbfe}
[data-page="developers"] .dev-flow-line span{padding:8px 10px;border:1px solid #e1e6ef;border-radius:8px;background:#fff;color:#344159;font-size:11px;font-weight:750}
[data-page="developers"] .dev-flow-line i{color:#a0aabc;font-style:normal}
[data-page="developers"] .dev-main code{overflow-wrap:anywhere}
[data-page="developers"] .dev-mobile-nav{display:none}
@media(max-width:1050px){[data-page="developers"] .dev-shell{grid-template-columns:205px minmax(0,1fr)}[data-page="developers"] .dev-main{padding-left:38px}}
@media(max-width:820px){[data-page="developers"] .dev-shell{display:block;padding:0 20px}[data-page="developers"] .dev-mobile-nav{display:flex;position:sticky;top:64px;z-index:31;align-items:center;justify-content:space-between;width:100%;padding:13px 0;border:0;border-bottom:1px solid var(--line);background:rgba(255,255,255,.97);color:#26334b;font-size:12px;font-weight:800;backdrop-filter:blur(14px)}[data-page="developers"] .dev-side{display:none!important}[data-page="developers"] .dev-side.open{display:block!important;position:sticky;top:108px;z-index:30;height:auto;max-height:calc(100vh - 108px);padding:18px;background:#fff;border-right:0;border:1px solid var(--line);border-radius:0 0 12px 12px}[data-page="developers"] .dev-main{padding:50px 0 78px}[data-page="developers"] .dev-paths{grid-template-columns:1fr}[data-page="developers"] .dev-endpoints>div{grid-template-columns:58px minmax(0,1fr)}[data-page="developers"] .dev-endpoints span{grid-column:2}}
@media(max-width:560px){[data-page="developers"] .dev-main h1{font-size:39px}[data-page="developers"] .dev-main h2{font-size:27px}[data-page="developers"] .dev-main .lead{font-size:15px}[data-page="developers"] .dev-flow-line{gap:7px;padding:14px}[data-page="developers"] .doc-table{overflow:auto}[data-page="developers"] .doc-table>div{min-width:620px}}
'''
    style_path.write_text(css, encoding='utf-8')
