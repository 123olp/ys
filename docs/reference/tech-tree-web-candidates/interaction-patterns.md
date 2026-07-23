# Human Infra 科技树交互模式

## 目标树

```text
目的
├── 永生
│   ├── 主体持续性定义
│   ├── 身体持续
│   ├── 认知与人格连续
│   ├── 时间路径扩展
│   ├── 技术窗口压缩
│   └── 社会与环境承载
└── 记忆编辑
    ├── 记忆识别
    ├── 记忆读取
    ├── 记忆巩固与消退
    ├── 记忆修改
    ├── 记忆写入
    └── 身份与伦理连续性
```

视觉采用自下而上：基础证据与机制在下方，工程系统居中，最终目标在顶部，点亮沿依赖边向上流动。

## 节点状态

| 状态 | 视觉 | 语义 |
|---|---|---|
| `unknown` | 空心灰色 | 尚未定义或缺少资料 |
| `researched` | 蓝灰描边 | 已形成研究域和资料包 |
| `evidence-found` | 蓝色半亮 | 已有证据，未满足验收 |
| `in-validation` | 琥珀脉冲 | 正在复核、实验或工程验证 |
| `validated` | 绿色常亮 | 达到预设验收标准 |
| `blocked` | 红色断边 | 关键依赖、风险或反证阻塞 |
| `speculative` | 紫色虚线 | 远期假设，只允许研究展示 |

状态必须同时使用颜色、图标和文字。研究成熟度、工程成熟度与目标完成度是三个字段，禁止混成一个百分比。

## 点亮契约

```text
node.state = validated
  iff required_dependencies 均满足
  and acceptance_checks 均通过
  and blocking_falsifiers 未触发
  and evidence_packet 存在
  and review_status 满足门槛
```

## 详情抽屉

点击节点显示：定义、状态、前置依赖、后续解锁、验收与失败标准、论文与 Source Card、项目产物、反证条件、证据边界和禁止推论。

## 画布交互

- 缩放、平移、搜索、小地图和返回根目标。
- 悬停高亮上游依赖与下游影响；双击聚焦子树。
- 筛选已点亮、受阻、证据缺口和远期假设。
- 支持“永生”“记忆编辑”“全部目标”三种视图。
- 语义缩放：远景显示域和阶段，近景显示节点与证据数。

## 最小节点契约

```json
{
  "id": "string",
  "goal_id": "immortality | memory-editing",
  "title": "string",
  "kind": "goal | domain | milestone | evidence | gate",
  "state": "unknown | researched | evidence-found | in-validation | validated | blocked | speculative",
  "maturity_level": "string",
  "dependencies": ["node-id"],
  "acceptance_checks": ["check-id"],
  "blocking_falsifiers": ["falsifier-id"],
  "evidence_refs": ["source-card-id"],
  "artifact_refs": ["repository-path"],
  "updated_at": "ISO-8601"
}
```

首选实现为 React Flow 配合 ELK/Dagre，因为目标包含多父依赖、折叠分组、大图导航和自定义节点。Astro 继续负责路由、科研叙事和静态发布，科技树作为受控交互岛加载。若先用现有 D3 验证信息结构，不得把临时单父树固化为最终数据契约。
