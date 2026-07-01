# Opt-Out Preference Signal Consent Revocation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/opt-out-preference-signal-consent-revocation-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


Opt-Out Preference Signal Consent Revocation Continuity 关注 consent、opt-out preference signal、Global Privacy Control、cookie/ad choices、revocation 和 dark pattern 如何决定主体能否持续撤回、限制或修改数据使用许可。

## 对象

- Opt-out preference signal、Global Privacy Control、consent banner、privacy preference、revocation、dark pattern 和 notice。
- 网站、应用、广告网络、数据经纪、订阅、cookie、tracking pixel 和跨站数据共享中的同意与撤回失败。
- 同意疲劳、默认捆绑、难以取消、设计诱导和跨设备偏好不同步。

## Human Infra 价值

```text
主体持续性需要同意不是一次性被消费
-> 数字服务持续请求、解释、记录和再利用主体许可
-> 同意设计若不可理解、不可撤回或被 dark pattern 扭曲，主体控制权会被长期消耗
-> 偏好信号、撤回机制和同意治理让主体能持续限制数据使用
-> 注意力、隐私、安全和未来选择权更少被默认画像吞噬
```

## 边界

- 本域不提供法律合规判断、cookie banner 规避、广告追踪绕过、订阅取消代办、请求模板或个案投诉策略。
- 不提供自动点击、批量 opt-out、机器人投诉、规避反滥用系统或伪造偏好信号的方法。
- 不判断某个 consent flow、广告系统或偏好信号是否违法或有效。
- 只整理公开资料、偏好机制、撤回失败模式、设计风险和禁止用途。

## 上下游

- 上游：`digital-identity-security/`、`health-data-privacy-governance/`、`language-access-plain-communication/`。
- 下游：`commercial-surveillance-adtech-profile-continuity/`、`data-broker-registry-opt-out-deletion-continuity/`、`online-safety-digital-harm-prevention/`。

## Source Signals

- California Privacy Protection Agency opt-out preference signal materials.
- Federal Trade Commission dark pattern and privacy materials.
- NIST Privacy Framework.
- W3C / Global Privacy Control public materials as technical context.
