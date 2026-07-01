# Research Software, Capsule and Computational Reproducibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-software-capsule-reproducibility-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


## Scope

This domain studies research software citation, executable environments, containers, computational capsules, dependency capture, archival snapshots and reproducible analysis packages.

Human Infra treats computational reproducibility as a tool continuity layer: if code, dependencies and execution context vanish, then models cannot be checked, reused or upgraded.

## Human Infra Chain

```text
claim depends on computation
  -> computation depends on code, dependencies, parameters, runtime and data paths
  -> reproducibility packages capture executable context and citation metadata
  -> reviewers and future researchers can rerun, inspect and adapt the analysis
  -> model errors, dependency drift and hidden assumptions become easier to detect
  -> long-horizon research capacity increases
```

## Non-Goals

- No malware packaging, exploit reproduction, credential leakage or unsafe execution instructions.
- No guarantee that rerunnable code proves scientific truth.
- No private data packaging or license laundering inside reproducibility bundles.
- No dependency pinning advice that bypasses security patches.

## Source Signals

- FORCE11 Software Citation Principles: https://force11.org/info/software-citation-principles/
- Software Heritage archive: https://www.softwareheritage.org/
- CITATION.cff format: https://citation-file-format.github.io/
- Zenodo GitHub archiving: https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- The Turing Way reproducible research guide: https://the-turing-way.netlify.app/

## Next Notes

- Define minimum reproducibility package fields: code, data pointer, environment, seed, parameters, license and citation.
- Connect to D3/Observable/Web paper outputs without mixing demo code with validated scientific models.
- Track reproducibility failure modes: dependency rot, hidden state, nondeterminism, missing data and hardware assumptions.
