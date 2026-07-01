# Domains

`domains/` 存放 Human Infra 的可独立演化研究域。正式研究域不再直接挂在 `domains/` 根目录下，而是按“可能性空间控制力”进入 C1-C6 六个物理层级目录。

## 控制面

- `_possibility-space-control/`：可能性空间控制分级索引。它不是普通研究域，而是按“研究域一旦成立或失效，能多深、多大、多长期地改写主体未来可能性空间”对全部正式研究域进行 C1-C6 分级。

## 物理分级目录

| 层级 | 物理目录 | 定位 |
| --- | --- | --- |
| C1 | `c1-boundary-rewriting/` | 直接改写寿命、死亡、时间、身份连续性和未来抵达边界。 |
| C2 | `c2-source-maintenance/` | 维护产生可能性的身体、脑、生命系统和衰老/损伤控制。 |
| C3 | `c3-generation-engine/` | 提升主体创造新路径的认知、学习、AI、工具和能力复利。 |
| C4 | `c4-conversion-channel/` | 把潜在可能性转成真实路径的研究、医疗、数据、制度和转化接口。 |
| C5 | `c5-ecological-substrate/` | 承载主体展开未来的能源、食物、水、治理、经济、通信和基础设施环境。 |
| C6 | `c6-local-unlocking/` | 解除具体疾病、流程、服务、职业、家庭、社区和专项风险中的局部阻塞。 |

## 查找方式

- 查完整研究域清单：`_possibility-space-control/classification.tsv`。
- 查层级判定规则：`_possibility-space-control/rubric.md`。
- 查统计摘要：`_possibility-space-control/summary.md`。
- 查具体研究域：进入 `classification.tsv` 的 `physical_path` 字段对应目录。

## 维护规则

- 新增正式研究域时，必须放入对应 C1-C6 物理目录，而不是放在 `domains/` 根目录。
- 新增、删除、重命名或移动研究域时，必须同步更新 `_possibility-space-control/classification.tsv`、`summary.md` 和必要的上游索引。
- 子域之间可以共享上位原则，但不能共享模糊所有权；数据、脚本和结论必须归属到明确子域。
- 分级只表达根本性、长远性和边界改写能力，不表达近期可行性、证据成熟度或商业化时间。
