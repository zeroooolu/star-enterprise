# 星球发行·企业版

> 状态：当前唯一权威基线  
> 更新日期：2026-09-14  
> 适用范围：产品定义、商业模型、版本与价格、官网表达、当前实现与后续 Roadmap。

本文件替代此前企业版目录中的业务基线、产品架构、商业模型、产品包装、Roadmap、各版 Prototype README 与 Release 说明。后续企业版范围、价格、命名或 Roadmap 如发生变化，统一更新本文件，不再新增并行版本文档。

---

## 1. 产品定义

星球发行·企业版是面向发行商、唱片公司、版权公司、AI 音乐平台、音乐科技及内容平台提供的企业音乐发行基础设施。

核心产品形态只有两个：

1. **自有品牌发行平台**：以企业品牌运营完整音乐发行业务，覆盖客户门户、企业管理后台、曲库、发行、平台状态、数据、收入与结算。
2. **发行 API**：保留现有网站、App、SaaS 或内部系统，通过标准 API 接入内容、发行、状态、报表与结算能力。

DDEX、XML、SFTP、Excel 等属于接入与数据交换方式，不作为第三个平级商业产品。

企业版不是普通星球发行的高阶会员，也不是重新建设一套独立发行 Domain。核心目标是将现有发行能力标准化、产品化并形成可持续销售和交付的 B2B 产品。

---

## 2. 业务关系与边界

### 2.1 默认业务链路

```text
企业下游客户 / 厂牌 / 音乐人
        ↓
企业发行平台或现有产品
        ↓
星球发行企业能力
        ↓
看见音乐发行审核与供应链
        ↓
音乐平台 / DSP
```

企业客户是企业版直接合同主体和业务 Operator；下游客户由企业客户经营，不作为企业版 P0 中看见侧的直接合同主体。

默认主链路中，看见侧发行审核是正式控制点。企业侧可存在资料检查、业务处理或自有审核流程，但不将“企业人工审核”设为所有客户必须经过的固定步骤。

### 2.2 现有能力直接复用

以下能力属于已有发行底座，不作为企业版当前阶段重新建设范围：

- Tenant / 企业空间基础能力
- 多账号与权限
- 企业管理后台
- 客户发行门户
- Artist / Label / Album / Track
- Metadata / Audio / Artwork / File
- ISRC / UPC
- Catalog / 曲库
- 发行任务与渠道配置
- 看见侧审核
- DSP 交付与状态
- 数据报表
- 收入、分账、结算与提现
- API / DDEX / XML / SFTP / Excel 等接入能力

### 2.3 当前产品化重点

当前新增和收口重点属于 Enterprise Commercial / Productization Layer：

- 企业官网与产品包装
- Pricing / Plan
- 企业申请与 Lead
- 商务方案与报价
- Contract / KYC Status
- Enterprise Account
- Tenant Provisioning
- Entitlement / Quota / Usage
- API Developer Experience
- Billing / Renewal
- Enterprise Sales / Ops
- 企业客户中心

---

## 3. 目标客户

当前重点覆盖四类企业客户：

### 发行商

需要自有品牌、客户门户、多客户运营、曲库、发行、数据和收入能力。

### 唱片公司 / 版权公司

拥有稳定或大规模曲库，需要统一内容管理、持续发行、历史迁移、批量处理与系统集成。

### AI 音乐 / 创作平台

已有创作产品和用户体系，需要通过 API 增加音乐发行服务，并持续接收发行状态、数据和收入结果。

### 音乐科技 / SaaS / 内容平台

已有成熟产品或内部系统，需要增量接入发行、状态、报表及结算能力，或通过 SFTP / XML / DDEX 与既有数据流程衔接。

---

## 4. 自有品牌发行平台

自有品牌发行平台用于建立完整的企业发行业务入口与运营体系。

核心组成：

```text
客户发行门户
+
企业管理后台
+
共享发行基础设施
```

核心能力：

- 企业品牌与 Logo
- 独立客户发行入口
- 按版本支持独立域名
- 合作客户与团队管理
- 艺人、专辑、歌曲和文件管理
- 客户提交与发行运营
- 发行资料校验与业务处理
- 渠道选择、提交和状态跟踪
- 更新、重传和下架等后续发行操作
- 数据与收入报表
- 合作方分账与结算
- 历史曲库迁移与批量导入
- 按版本提供 API、SFTP、XML、DDEX 等系统接入

---

## 5. 发行 API

发行 API 面向已有产品、账号体系和用户体验的企业。

对外能力按业务结果组织：

```text
客户与基础资料
内容与曲库
发行管理
渠道状态
数据与报表
收入与结算
```

Developer Product 应逐步具备：

- Sandbox / Production 环境
- API Credential 与权限
- 认证与租户隔离
- Webhook
- Request / Response Log
- Webhook Log
- Error / Request ID
- Usage / Quota
- 开发者指南
- 联调与企业技术支持

原则：优先映射现有真实发行 API，不新建一套与现有业务模型并行的 Enterprise API Domain。

---

## 6. 正式 Plan、版本与价格

### 6.1 Plan 设计原则

企业版 Plan 不通过拆掉核心发行流程制造版本差异。三个版本均应具备完整的曲库、客户门户、发行、状态、数据与收入主链路，差异集中在五个维度：

1. **业务容量**：曲库规模与合作客户规模；
2. **企业运营能力**：独立域名、多客户经营与合作方分账；
3. **批量与系统集成**：Excel、SFTP、XML、DDEX 与发行 API；
4. **实施复杂度**：历史迁移、深度联调与项目制实施；
5. **服务等级**：标准支持、优先支持、专属客户经理与 SLA。

历史音乐资产管理 SaaS 报价中的资产管理、资产导入、数字发行、合规检测、版税报表、收入管理、单/多用户分账、建站、客户支持和培训支持继续作为企业版权益设计参考，但只吸收与企业发行产品边界一致的能力，不把歌单、版权法律服务等非核心模块强行塞入当前 Plan。

### 6.2 自有品牌发行平台价格

| 版本 | 年费 | 曲库规模 | 合作客户 | 主要适用阶段 |
| --- | ---: | ---: | ---: | --- |
| 基础版 | ¥12,800 / 年 | 1,000 首 | 50 个 | 小规模发行运营 |
| 专业版 | ¥59,800 / 年 | 5 万首 | 1,000 个 | 规模化多客户发行 |
| 企业版 | ¥129,800 / 年起 | 30 万首起 | 按项目配置 | 大型发行或平台级业务 |

三个版本统一收取：

**发行使用费：¥1 / 首 / 渠道**

一首歌曲发行至一个目标渠道计 1 次发行使用量。

### 6.3 Plan 权益矩阵

| 能力 | 基础版 | 专业版 | 企业版 |
| --- | --- | --- | --- |
| **业务容量** |  |  |  |
| 曲库规模 | 1,000 首 | 5 万首 | 30 万首起 |
| 合作客户 | 50 个 | 1,000 个 | 按项目配置 |
| **品牌、曲库与客户运营** |  |  |  |
| 企业品牌与 Logo | ✓ | ✓ | ✓ |
| 企业管理后台 + 客户发行门户 | ✓ | ✓ | ✓ |
| 艺人 / 厂牌 / 专辑 / 歌曲 / 文件管理 | ✓ | ✓ | ✓ |
| 合作客户与团队管理 | ✓ | ✓ | ✓ |
| 独立域名 | — | ✓ | ✓ |
| 页面 / Excel 批量导入 | ✓ | ✓ | ✓ |
| **发行与持续运营** |  |  |  |
| 国内外音乐平台发行 | ✓ | ✓ | ✓ |
| 发行资料校验与合规检查 | ✓ | ✓ | ✓ |
| 发行状态与异常跟踪 | ✓ | ✓ | ✓ |
| 更新 / 重传 / 下架 | ✓ | ✓ | ✓ |
| 批量发行 | — | ✓ | ✓ |
| API 自动化发行 | 随 API | 随 API | ✓ |
| **数据、收入与结算** |  |  |  |
| 平台数据与收入报表 | ✓ | ✓ | ✓ |
| 收入与提现管理 | ✓ | ✓ | ✓ |
| 合作方分账与结算 | — | ✓ | ✓ |
| 报表导出 | ✓ | ✓ | ✓ |
| **批量处理与系统集成** |  |  |  |
| Excel 数据交换 | ✓ | ✓ | ✓ |
| SFTP 文件 / 数据交换 | — | ✓ | ✓ |
| XML 结构化数据交换 | — | ✓ | ✓ |
| DDEX 行业标准接入 | — | — | ✓ |
| 发行 API | 可增购 | 可增购 | 包含 |
| Webhook / API 日志 | 随 API | 随 API | ✓ |
| **实施与服务** |  |  |  |
| 历史曲库迁移 | 可选服务 | 可选服务 | 按项目范围 |
| 客户支持 | 标准支持 | 优先支持 | 专属客户经理 |
| 上线与培训 | 标准上线指引 | 首次实施培训 | 项目制实施 / 定制培训 |
| 技术支持 | 标准技术支持 | 优先技术支持 | 专属技术支持 / SLA |

### 6.4 Plan Entitlement 基线

后续系统实现以 Entitlement 而不是页面文案作为版本判断依据。第一版建议至少固化以下字段：

```text
catalog_limit
client_limit
custom_domain
distribution_core
revenue_reporting
partner_split
excel_import
sftp_access
xml_access
ddex_access
distribution_api
webhook_and_api_logs
batch_distribution
api_automation
migration_service
support_level
onboarding_level
sla_level
```

取值基线：

```text
Basic
- catalog_limit: 1000
- client_limit: 50
- custom_domain: false
- partner_split: false
- sftp_access: false
- xml_access: false
- ddex_access: false
- distribution_api: addon
- batch_distribution: false
- api_automation: with_api
- support_level: standard
- onboarding_level: guide
- sla_level: standard

Professional
- catalog_limit: 50000
- client_limit: 1000
- custom_domain: true
- partner_split: true
- sftp_access: true
- xml_access: true
- ddex_access: false
- distribution_api: addon
- batch_distribution: true
- api_automation: with_api
- support_level: priority
- onboarding_level: first_implementation_training
- sla_level: priority

Enterprise
- catalog_limit: 300000+
- client_limit: project_based
- custom_domain: true
- partner_split: true
- sftp_access: true
- xml_access: true
- ddex_access: true
- distribution_api: included
- batch_distribution: true
- api_automation: true
- support_level: dedicated_manager
- onboarding_level: project_implementation
- sla_level: contracted_sla
```

`distribution_core`、`revenue_reporting`、`excel_import` 三个版本均为开启状态。

### 6.5 独立发行 API

**¥9,800 / 年起 + ¥1 / 首 / 渠道**

独立 API 方案面向只需要系统接入能力的企业，不默认包含完整客户发行门户和企业发行平台交付。

### 6.6 可选实施与集成

以下内容根据项目范围单独评估：

- 历史曲库迁移
- 复杂字段映射与数据整理
- API 深度集成
- SFTP / XML / DDEX 对接
- 大型项目实施
- 专属 SLA 与技术服务

企业版商业模型以 **年度平台服务费 + 实际发行使用量 + 必要的项目实施 / 高级服务** 为主，不以普通星球发行的版权分成作为主要收费逻辑。

---

## 7. 企业商业生命周期

企业版应形成以下完整商业链路：

```text
访问官网
→ 了解产品 / 价格 / API
→ 提交企业申请
→ Lead / 需求确认
→ 方案与报价
→ 合同 / KYC
→ Enterprise Account
→ Plan / Entitlement
→ Tenant 创建或关联
→ Provisioning / Quota / Credential
→ 联调与上线
→ Active
→ Usage / Billing
→ 续费 / 升级 / 扩容 / 终止
```

内部建议状态：

```text
APPLIED
QUALIFYING
PROPOSAL
CONTRACTING
SIGNED
PROVISIONING
INTEGRATING
ACTIVE
SUSPENDED
RENEWING
EXPIRED
CLOSED
```

Enterprise Account 管理商业关系；现有 Distribution Console 管理具体发行操作。

---

## 8. Enterprise Plan / Entitlement 模型

企业签约后，需要从商业合同映射到系统能力。

```text
Enterprise Plan
├── Product Mode
│   ├── Branded Platform
│   └── Distribution API
├── Catalog Quota
├── Client Quota
├── DSP Scope
├── API Access
├── Integration Methods
├── Revenue / Settlement
├── Support Level
├── SLA
└── Additional Services
```

原则：Plan 决定 Entitlement，Entitlement 决定 Tenant 可见和可调用的能力，Quota / Usage 用于容量和计费管理。

---

## 9. 官网与信息架构

当前正式实现位于：

`03-enterprise/prototype-v4/`

根目录 `vercel.json` 中的 `/enterprise*` 路由指向该版本。

正式页面：

- `/enterprise`
- `/enterprise/product`
- `/enterprise/solutions`
- `/enterprise/pricing`
- `/enterprise/api`
- `/enterprise/developers`
- `/enterprise/apply`

官网商业叙事顺序优先回答：

1. 产品是什么
2. 适合哪些企业
3. 可以完成哪些业务
4. 采用哪种接入方式
5. 版本和价格如何选择
6. 如何申请企业方案

技术架构、协议、凭证、Webhook 与资源模型进入 API / Developers 第二层信息。

---

## 10. 对外语言规则

### 10.1 产品与业务术语

| 内部 / 行业表达 | 对外优先表达 |
| --- | --- |
| White Label | 自有品牌发行平台 |
| Catalog | 曲库 / 音乐内容 |
| DSP | 音乐平台；发行操作与计费场景可使用“渠道” |
| Distribution Workflow | 发行流程 |
| Revenue / Settlement | 收入与结算 |
| Integration | 系统对接 |
| Migration | 历史曲库迁移 / 导入 |
| Developer Center | 开发者中心 |
| API Docs | 开发者指南 |
| CP | 合作客户 / 合作方；仅内部业务或技术语境使用 CP |

Provisioning、Entitlement、Tenant、Quota 等内部架构词不进入商业页面第一层。

### 10.2 文案风格

- 官网商业页面不使用第一、第二人称或指向性人称表达，包括“你 / 你的 / 我 / 我们 / 你们 / 自己”等。
- 标题优先直接表达业务结论，不使用口语化提问或内部讨论式措辞。
- 能描述业务结果时，不优先堆系统模块名称。
- API / DDEX / XML / SFTP 仅在技术接入语境使用。
- 不新增超出当前确认范围的能力承诺。

---

## 11. CTA 规则

全站通用主 CTA：**申请企业方案**

API 产品关键入口可使用：**申请 API 接入**

Pricing 版本卡：

- 申请基础版
- 申请专业版
- 联系商务

Apply 表单提交：**提交企业咨询**

页面底部统一 Contact Sales：

**CONTACT SALES**  
**获取适配业务需求的企业发行方案**  
提交基本业务信息，结合曲库规模、客户协作方式与系统集成需求，评估适合的产品版本、发行 API 或组合方案。  
**申请企业方案**

当前没有无需商务审核即可直接进入的企业试用环境，因此不使用“免费试用”。

---

## 12. Enterprise Visual System

商业页面使用产品证据解释能力，不以装饰性音乐图片作为主要视觉。

统一视觉组件：

- **Product Window**：后台、门户、曲库、发行、收入界面
- **Architecture Diagram**：企业系统与发行能力的连接关系
- **Flow Diagram**：发行、实施与接入流程
- **Data Dashboard**：规模、状态、数据、收入与结算
- **Code Console**：API Request / Response 与开发示例
- **Event Stream**：Webhook 与渠道状态变化

设计原则：每 1～1.5 屏形成一个明确视觉焦点，避免连续出现“标题 + 段落 + 多张文字卡片”的单一节奏。

---

## 13. 当前已完成

截至 2026-09-14，已完成：

- 企业版产品范围收口
- 两个核心产品形态确定
- 基础版 / 专业版 / 企业版价格与容量确定
- API-only 商业方案确定
- 官网 7 个正式页面
- 全站文案与术语统一
- 全站 CTA 统一
- Product / Solutions / Pricing / API / Developers 视觉化升级
- Apply 轻量企业咨询表单 Demo
- Pricing / API 到 Apply 的方案上下文继承
- API Developer Product 的公开信息架构 Demo

---

## 14. 下一阶段 Roadmap

后续不再重构现有发行后台，重点打通真实商业闭环。

### P0 — 企业申请与 Sales / Ops

- Apply 提交真实 Enterprise Lead
- Lead 列表与客户档案
- 需求、方案、报价与合同状态
- 企业客户与现有 Tenant 关联

### P0 — Plan / Provisioning / Entitlement

- Plan Schema
- Entitlement
- Catalog / Client / Usage Quota
- Tenant 创建或关联
- 品牌、域名、DSP、API 配置
- 开通 Checklist

### P1 — API Developer Product 正式化

- 现有接口 Endpoint Mapping
- Sandbox / Production Credential
- Webhook
- 调用与回调日志
- Usage / Quota
- 正式开发者指南

### P1 — Enterprise Customer Center

- 企业信息
- 当前方案与已开通能力
- 使用量与额度
- 合同
- API
- 账单
- 续费 / 升级 / 扩容
- 技术支持

### P1 — Billing / Renewal

- 年度到期日期
- 实际发行使用量
- 超额量
- 账单状态
- 续费提醒
- Plan 升级与额度扩容
- 暂停 / 到期 / 终止

P0 不要求建设完整 CRM、ERP 或复杂在线自动支付系统；重点是让商务合同、Tenant 能力和持续服务状态形成可追踪闭环。

---

## 15. 当前明确不做

- 重做现有 Enterprise Console
- 重做客户发行门户
- 重做 Tenant CRUD
- 重做 Catalog / Release / DSP / Report / Revenue Domain
- 新建与现有发行模型平行的 Enterprise API Domain
- 将 DDEX / XML / SFTP 包装成第三个商业产品
- 将 Own DSP Deal / Hybrid Deal 作为当前 P0 核心卖点
- 构建完整 CRM
- 构建完整财务 ERP

---

## 16. 文档维护规则

`03-enterprise/README.md` 是企业版唯一产品事实源。

后续更新规则：

1. 产品定义、价格、版本、商业规则、官网命名与 Roadmap 只更新本文件。
2. Prototype 目录只保留实现代码，不再维护独立产品定义 README。
3. 研究过程、历史报价和被推翻方案不继续保留为当前文档；如需追溯，使用 Git 历史。
4. 共享三产品架构仍以 `00-overview/`、`01-shared-foundation/` 与 `07-decisions/` 中的跨产品文档为准，不在企业版目录重复维护。
