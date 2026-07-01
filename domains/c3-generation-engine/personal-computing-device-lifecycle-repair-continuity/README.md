# Personal Computing Device Lifecycle Repair Continuity

`personal-computing-device-lifecycle-repair-continuity` 研究个人手机、电脑、平板、外设和本地存储设备的采购、维修、替换、备件、数据迁移、保修、远程锁定和报废如何影响主体的数字行动连续性。

> 核心问题：主体的大量任务已经通过个人计算设备完成；设备失效、不可维修或无法迁移数据，会把账号、资料、工作流和恢复通道同时切断。

## 关注对象

- 手机、电脑、平板、外设、充电器、本地硬盘、备份盘、安全密钥和关键配件。
- 维修权、备件可得性、保修、维修文档、授权维修、二手设备、设备锁定、MDM 和远程擦除。
- 数据迁移、设备替换、加密磁盘恢复、旧设备交接、报废擦除和电子废弃物。
- 设备不可用、供应中断、维修成本过高、平台停止支持、配件断供和本地资料丢失。

## Human Infra 链路

```text
个人计算设备生命周期可维修
  -> 本地计算、通信、认证、资料访问和任务执行入口保持可用
  -> 设备故障、停产、锁定和迁移失败造成的行动中断下降
  -> 学习、工作、医疗、金融、创作和协作系统可持续接入
  -> 主体数字行动能力和有效时间增强
```

## 非目标

- 不提供绕过设备锁、破解加密、规避 MDM、盗取数据、拆机攻击、保修欺诈或维修操作指导。
- 不替代厂商、授权维修、数据恢复服务、消费者保护机构、IT 管理员或法律建议。
- 不收集序列号、设备指纹、密码、恢复密钥、定位记录、企业管理配置或私人文件。

## Source Signals

- FTC right to repair and repair restriction materials: https://www.ftc.gov/
- iFixit / manufacturer public repair documentation as implementation examples.
- NIST media sanitization and endpoint security references: https://www.nist.gov/
- EPA electronics recycling and e-waste resources: https://www.epa.gov/

## 下一步

- 建立 `device -> repairability -> support window -> data migration -> action continuity` 变量表。
- 区分个人设备、工作设备、学校设备、受管设备和医疗辅助设备的所有权边界。
- 与 `digital-inclusion-connectivity`、`password-manager-secret-vault-continuity`、`cloud-backup-file-sync-data-portability-continuity` 和 `long-term-digital-preservation-format-migration` 建立边界。
