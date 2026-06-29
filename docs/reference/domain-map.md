# 域地图

Human Infra 的上位对象是“人类任务执行系统”。不同子域分别处理这个系统的不同层次、尺度和风险。

## 目标终态

如果没有历史包袱，项目应按下面的边界组织：

- `docs/`：稳定理论、伦理原则、域地图和资料归档。
- `domains/longevity-evidence/`：健康寿命、干预证据、临床试验和安全边界。
- `domains/cellular-reprogramming/`：细胞重编程、表观遗传年轻化、身份保持和肿瘤风险边界。
- `domains/regenerative-medicine/`：再生医学、组织修复、器官再生和部件替换。
- `domains/cancer-control/`：癌症预防、早筛、治疗、复发和长期肿瘤风险。
- `domains/immune-maintenance/`：免疫衰老、感染防御、慢性炎症、自身免疫和免疫监视。
- `domains/neuro-continuity/`：大脑、记忆、意识、人格和主体身份连续性。
- `domains/future-waiting/`：去未来、压缩等待和低主观时间成本等待路径。
- `domains/disembodied-cns/`：去具身外部维持型中枢生命系统。
- `domains/memory-editing/`：记忆读写、人格连续性和主体权利保护。
- `domains/biostasis-cryopreservation/`：生物停滞、冷冻保存、休眠和等待未来修复。
- `domains/cognitive-augmentation/`：AI、外部记忆、学习系统、脑机接口和认知增强。
- `domains/risk-engineering/`：事故、灾害、暴力、系统故障和尾部风险工程。
- `domains/resource-social-infra/`：食物、水、能源、住房、医疗、照护和社会支持。
- `domains/governance-rights/`：同意、退出、数据权、法律身份、AI 治理和研究伦理。
- `domains/measurement-feedback/`：主体状态测量、风险评分、预测模型和反馈闭环。

## 域关系

```text
Human Infra
├── Human Runtime Infrastructure
│   ├── 生理基础设施
│   ├── 认知基础设施
│   ├── 情绪与动机基础设施
│   ├── 环境与工具基础设施
│   └── 观测、反馈与恢复基础设施
├── Longevity Evidence
│   ├── 长寿干预
│   ├── 临床试验
│   ├── 药品安全
│   └── 公开证据账本
├── Cellular Reprogramming
│   ├── OSKM / OSK / iPS
│   ├── 部分重编程
│   ├── mRNA / 化学重编程
│   ├── AI 设计因子 / 表观遗传编辑
│   └── 年轻化、去分化、身份保持和肿瘤风险边界
├── Regenerative Medicine
│   ├── 干细胞 / 组织工程
│   ├── 器官再生 / 器官替代
│   └── 长期整合与功能恢复
├── Cancer Control
│   ├── 预防 / 早筛
│   ├── 治疗 / 复发
│   └── 肿瘤演化和长期风险
├── Immune Maintenance
│   ├── 免疫衰老
│   ├── 感染防御
│   ├── 慢性炎症
│   └── 免疫监视
├── Future Waiting
│   ├── 度规红移固有时差分路径（黑洞等待室）
│   ├── 相对论时间膨胀等待
│   ├── 休眠 / 冬眠等待
│   └── 等待未来的主观时间成本
├── Disembodied CNS
│   ├── 人工生命支持
│   ├── 神经接口
│   ├── 外部控制器
│   ├── 传感器反馈
│   └── 主体连续性
├── Neuro Continuity
│   ├── 大脑保存 / 神经保护
│   ├── 认知退行防控
│   └── 意识、人格和身份连续
├── Memory Editing
│   ├── 记忆痕迹读写
│   ├── 记忆删除、写入和重构的验证
│   ├── 人格连续性
│   └── 同意、退出和审计
├── Biostasis And Cryopreservation
│   ├── 冷冻保存
│   ├── 生物停滞
│   └── 未来修复依赖
├── Cognitive Augmentation
│   ├── AI 协作
│   ├── 外部记忆 / 知识系统
│   └── 学习、判断和行动放大
├── Risk Engineering
│   ├── 事故 / 灾害 / 暴力
│   ├── 预警 / 响应 / 恢复
│   └── 尾部风险
├── Resource And Social Infrastructure
│   ├── 食物 / 水 / 能源 / 住房
│   ├── 医疗 / 照护 / 康复
│   └── 教育 / 就业 / 社会支持
├── Governance And Rights
│   ├── 同意 / 退出 / 审计
│   ├── 数据权 / 法律身份
│   └── AI、神经和医学治理
└── Measurement And Feedback
    ├── 生物标志物 / 生物年龄
    ├── 风险评分 / 预测模型
    └── 反馈闭环
```

## 为什么拆分

旧 Biocat 只覆盖“长寿证据与健康干预”。它能回答某个干预有没有证据、效果多大、风险在哪里，但无法承载 Human Infra 的全部问题。

“永生”和“记忆编辑”也不应直接混入 Biocat，因为它们不是普通长寿干预证据页，而是远期高风险研究域：

- `disembodied-cns` 关注身体功能由外部系统代理后的生命支持、接口闭环和主体连续性。
- `memory-editing` 关注神经系统中记忆痕迹的读写、删除、重构、验证和伦理约束。
- `future-waiting` 关注通过物理或生物状态改变减少等待未来的主观时间成本，例如度规红移固有时差分路径（黑洞等待室）。
- `cellular-reprogramming` 关注细胞身份、表观遗传年龄、组织功能和重编程风险之间的机制关系。它不是普通“长寿干预条目”，而是细胞状态可重写范式的独立机制域。
- `regenerative-medicine`、`cancer-control` 和 `immune-maintenance` 关注身体基底长期可维护性中的不同失败模式。
- `neuro-continuity`、`cognitive-augmentation`、`memory-editing` 和 `disembodied-cns` 关注延续的是否仍是能够行动、记忆和选择的同一主体。
- `biostasis-cryopreservation` 关注暂停损耗并等待未来修复，与 `future-waiting` 的时间差分路径互补。
- `risk-engineering`、`resource-social-infra` 和 `governance-rights` 关注主体不被外部风险、资源断裂或制度控制截断。
- `measurement-feedback` 关注所有研究域如何被观测、建模、反馈和校正。

把它们拆开，能避免一个错误概念：用“长寿方法”统摄所有人类增强、生命延续和神经干预问题。

## 本轮迁移切片

- 根目录从 Biocat 改为 Human Infra。
- 旧 Biocat 文档、数据和脚本迁入 `domains/longevity-evidence/`。
- 四份最新资料改名归档到 `docs/source-notes/`。
- 新增 Human Infra 总理论、域地图、伦理边界和两个远期研究域 README。
- 新增 `domains/cellular-reprogramming/`，承载山中因子到部分重编程、化学重编程、AI 因子设计和表观遗传编辑的机制谱系。
- 新增研究域图谱和 10 个先验条件域骨架，全部只创建 README / AGENTS，不创建空数据或脚本目录。

## 主动不做

- 不把 Biocat 采集脚本泛化为 Human Infra 通用采集框架。
- 不引入 Web 框架、数据库或服务端目录。
- 不新增记忆编辑或中枢生命支持的实验协议。
- 不新增细胞重编程实验协议、载体构建、剂量、给药或人体应用建议。
- 不新增再生医学、癌症、免疫、神经、生物停滞、认知增强等高风险域的操作协议或个体建议。
- 不把度规红移固有时差分路径、相对论等待或其他未来等待路径写成当前可执行工程。
- 不把远期研究域伪装成当前可执行产品。

## 验证点

- 根 README 能解释 Human Infra，而不是只解释 Biocat。
- Biocat 的数据和脚本仍能在子域内被定位和编译。
- “永生”和“记忆编辑”有独立边界，不污染长寿证据模型。
- “细胞重编程”有独立机制边界，不把山中因子、部分重编程、化学重编程或商业公告混入普通长寿干预证据账本。
- “度规红移固有时差分路径（黑洞等待室）”有独立 Future Waiting 边界，不污染长寿证据、记忆编辑或去具身中枢模型。
- 新增研究域都能回到 [Research Domain Atlas](research-domain-atlas.md) 的先验条件和域判定契约。
- 原始资料有稳定归档路径，后续不会继续留在根目录。
