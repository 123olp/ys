# Domain DNS Web Presence Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/domain-dns-web-presence-continuity` |
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


`domain-dns-web-presence-continuity` 研究域名、DNS、注册商、WHOIS/RDAP、续费、证书、托管、邮箱域和网站可用性如何影响主体、组织、项目和作品的长期可达性。

> 核心问题：域名是公共地址、可信入口和数字身份资产；过期、劫持、DNS 配置失败或托管失效会让作品、业务、社区和邮件系统突然消失。

## 关注对象

- Domain registration、registrar account、DNS records、nameserver、WHOIS/RDAP、renewal、transfer lock 和 registry policy。
- TLS certificates、hosting、web redirects、custom email domain、subdomain ownership 和 content availability。
- 域名过期、续费失败、注册商账号接管、DNS hijacking、证书过期、托管停服、组织交接和死亡/失能后域名继承。
- 与品牌、研究作品、社区入口、邮箱域、支付/登录回调和长期引用的关系。

## Human Infra 链路

```text
域名/DNS 与 Web 存在连续
  -> 公共地址、邮箱域、证书、托管和链接入口保持可续费可迁移
  -> 域名过期、DNS 劫持、证书失效和托管中断导致的数字消失风险下降
  -> 项目、组织、作品、社区和通信入口保持长期可达
  -> 主体外部表达、信誉资产和协作网络连续性增强
```

## 非目标

- 不提供个人域名抢注、DNS 修改、证书配置、网站迁移、账号恢复、品牌争议、UDRP、绕过封禁或安全事件处置建议。
- 不替代注册商、DNS 托管商、CA、网站托管商、组织 IT、ICANN、律师或官方支持渠道。
- 不收集或处理域名账号、DNS 控制台、API token、证书私钥、托管凭证、注册人资料、支付资料或安全事件细节。

## Source Signals

- ICANN registrant and domain lifecycle resources: https://www.icann.org/
- IANA / DNS root zone and protocol context: https://www.iana.org/
- CISA DNS infrastructure security resources: https://www.cisa.gov/
- CA/Browser Forum and major CA public certificate lifecycle materials as implementation examples.

## 下一步

- 建立 `domain -> DNS -> certificate -> hosting/email -> public reachability` 变量表。
- 区分个人域名、组织域名、项目文档站、邮箱域和社区入口。
- 与 `email-account-recovery-continuity`、`long-term-digital-preservation-format-migration`、`notary-document-authentication-signature-continuity` 和 `digital-legacy-data-succession` 建立边界。
