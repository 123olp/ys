# telehealth-remote-monitoring-access 目录说明

`domains/telehealth-remote-monitoring-access/` 是 Human Infra 的远程医疗与居家监测接入域，负责把虚拟照护、远程随访、居家监测、设备和升级路径建模为医疗连续性的空间扩展条件。

## 目录结构

```text
telehealth-remote-monitoring-access/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义远程医疗、远程患者监测、居家设备、数字照护连续性和服务升级边界。
- 本域只做公开资料整理、变量建模、证据边界和远程照护断点分析。
- 诊断、分诊、设备处方、治疗建议、报销判断、平台背书和急诊替代不属于本域。

## 上下游关系

- 上游：`digital-inclusion-connectivity/`、`patient-data-interoperability/` 和 `health-literacy-navigation/`。
- 下游：`healthcare-access-continuity/`、`caregiving-long-term-care/`、`measurement-feedback/` 和慢病相关健康域。

## 维护规则

- 新增资料必须说明它支持的是服务可达、监测可见、设备可靠、升级路径、覆盖规则、隐私安全还是临床责任变量。
- 不能把远程医疗资料写成具体医疗服务、设备、保险或治疗建议。
