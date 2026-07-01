# transportation-access-mobility 目录说明

`transportation-access-mobility/` 是 Human Infra 的交通接入与日常移动域，负责研究外部交通系统如何让主体连接到医疗、工作、食物、照护、社区和应急资源。

## 目录结构

```text
transportation-access-mobility/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义交通接入域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做交通可达性、无障碍、出行负担、交通安全和服务连接资料整理。
- 个体路线、驾驶、车辆、交通法律、应急撤离和出行操作建议不属于本域。

## 上下游关系

- 上游：`housing-built-environment-stability/`、`physical-activity-mobility/`、`financial-resilience-access/`。
- 下游：`healthcare-access-continuity/`、`occupational-work-design/`、`social-connection-relational-infra/` 和 `emergency-preparedness-response/`。

## 维护规则

- 新增资料必须区分外部交通可达性与身体移动能力。
- 禁止输出具体路线、撤离操作、驾驶法律或车辆购买建议。
