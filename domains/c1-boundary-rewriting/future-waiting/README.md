# Future Waiting

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/future-waiting` |
| 分级 | `C1` - 可能性边界改写层 |
| 控制轴 | 时间/未来边界 |
| 分级理由 | 直接处理主体固有时间、外部未来和等待未来的边界条件。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何直接改写主体持续性边界，例如寿命、死亡、时间差分、身份连续性或未来抵达能力？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


Future Waiting 是 Human Infra 中负责“以较少主观时间抵达更远未来”的远期路径研究域。

它关注的不是直接治疗衰老、复活死人或上传人格，而是各种“压缩等待”的思想实验、技术路线和边界条件。

## 核心定位

```text
不一定延长本地寿命，而是减少抵达未来所需经历的主观时间。
```

## 当前路径

- `paths/black-hole-waiting-room.md`：度规红移固有时差分路径，传播名“黑洞等待室”，基于强引力时空中的度规红移因子压缩主体固有时的未来等待思想实验。

## 论文页

- `web/src/pages/papers/metric-redshift-recursive-waiting.astro`：度规红移递归等待假设，提出可控强红移等待区、等待倍率和等待-升级递归循环的条件性模型。
- `web/src/pages/papers/proper-time-differential-waiting-hypothesis.astro`：度规红移固有时差分路径专项论文页，把“黑洞等待室”收敛为可审查的未来等待假设。
- `web/src/pages/papers/controllable-metric-waiting-room-hypothesis.astro`：可控度规等待室假设，提出“等待室 -> 技术升级 -> 退出采用 -> 再等待”的递归未来等待模型。

## 与其他子域的关系

- 与 `longevity-evidence/` 的区别：Longevity Evidence 评估健康寿命干预证据；Future Waiting 评估“去未来”的等待机制。
- 与 `disembodied-cns/` 的区别：Disembodied CNS 关注外部系统代理身体和中枢生命维持；Future Waiting 可以依赖生命支持，但不以中枢接口为核心对象。
- 与 `memory-editing/` 的区别：Memory Editing 关注记忆痕迹与人格连续性；Future Waiting 关注时间路径、等待成本和返回未来的可行性边界。

## 安全边界

本子域只做概念建模、证据整理和风险边界，不提供太空任务、黑洞接近、极端轨道控制或人体实验的可执行方案。

不能写成：

- 当前可执行的永生工程。
- 战胜死亡或复活方案。
- 可以安全靠近黑洞的工程路线。
- 可以保证抵达未来并返航的技术承诺。

## 目录结构

```text
future-waiting/
├── AGENTS.md
├── README.md
└── paths/
    └── black-hole-waiting-room.md
```
