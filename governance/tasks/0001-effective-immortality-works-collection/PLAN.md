# Planning Summary

需求已对齐：搭建公共作品集三件套（永生史/健康手册/永生指南），时间维度=过去/现在/未来，
用途=内部个人决策辅助，约束=物理规律，目的=有效永生（作品集是认知手段）。

执行路径：先建骨架（TP-04）→ 再按依赖关系编写三个作品集（TP-01/02/03）→ 整体交叉验证。

# Lifecycle Gates

```text
SPEC -> PLAN -> BUILD -> TEST -> REVIEW -> SHIP
  ✔      ✔      进行中    →       →        →
```

- Gate 1（SPEC）：需求对齐完成（时间维度、用途、约束）——已过
- Gate 2（PLAN）：本任务文档定稿——已过
- Gate 3（BUILD）：三件套内容完成——未过
- Gate 4（TEST/REVIEW）：交叉引用与证据一致性自审——未过
- Gate 5（SHIP）：内部交付可用——未过

任何 gate 不得跳过：未闭合的 gate 必须回到对应阶段重做，不得以"内容简单/内部使用"为由跳过 TEST/REVIEW。

# Simplest Path

1. 落盘任务容器（本步）
2. 确认剩余歧义（手册粒度、指南组织、起步形态、物理落点）
3. 建立三件套骨架与索引（TP-04）
4. 逐件编写内容（TP-01 → TP-02 → TP-03，指南依赖史与手册的交叉引用约定）
5. 整体自审：时间维度、证据标注、交叉引用

# Split Strategy

按时间维度拆包：过去（史）/ 现在（手册）/ 未来（指南），加一个骨架索引包。
三个作品集内容相对独立，可并行编写，最后统一交叉引用。

# Execution Waves

- Wave 1：TP-04 骨架与索引（先于一切）
- Wave 2：TP-01 永生史 + TP-02 健康手册（相互独立）
- Wave 3：TP-03 永生指南（依赖前两者的交叉引用约定）
- Wave 4：整体验收

# Runtime Workflow Contract

- 内容编写：主代理直接执行（无 worker 分包）
- 证据引用：复用项目 reviewed artifacts 与外部权威来源
- 文档更新：每完成一件，更新 TODO/STATUS

# Next Executable Leaves

- TP-04 骨架与索引（当前 ready）
- 需用户确认 A1-A4 后进入

# Dependency Graph

```text
TP-04 骨架与索引
  ├── TP-01 永生史
  ├── TP-02 健康手册
  └── TP-03 永生指南（依赖 TP-01/TP-02 的交叉引用约定）
```

# Rollback Protocol

- 恢复 `INDEX.md` 当前任务行
- 恢复本任务目录到初始化状态
- 不得影响其他任务目录
