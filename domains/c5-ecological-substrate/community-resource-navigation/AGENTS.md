# community-resource-navigation 目录说明

`domains/c5-ecological-substrate/community-resource-navigation/` 是 Human Infra 的社区资源导航域，负责把本地服务目录、社会需求筛查、转介和闭环回访建模为资源转化接口。

## 目录结构

```text
community-resource-navigation/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义社区资源导航、服务目录、社会需求转介、闭环回访和本地服务断点。
- 本域只做公开资料整理、变量建模、证据边界和资源导航机制分析。
- 个体资格判断、申请建议、机构推荐、资源实时可得承诺、危机替代和敏感需求数据处理不属于本域。

## 上下游关系

- 上游：`resource-social-infra/`、`health-literacy-navigation/`、`digital-inclusion-connectivity/` 和 `social-connection-relational-infra/`。
- 下游：`social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`housing-built-environment-stability/` 和 `food-security-nutrition-access/`。

## 维护规则

- 新增资料必须说明它支持的是资源目录、筛查、匹配、转介、回访、人工协助、数据标准还是隐私治理变量。
- 不能把社区资源资料写成个体资格、申请、危机、医疗或法律建议。
