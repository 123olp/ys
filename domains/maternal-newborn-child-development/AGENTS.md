# maternal-newborn-child-development 目录说明

`domains/maternal-newborn-child-development/` 是 Human Infra 的母婴健康、儿童发展与早期生命基础设施域，负责把孕产、新生儿、儿童健康、生长和早期发展建模为主体能力形成的源头条件。

## 目录结构

```text
maternal-newborn-child-development/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义孕产健康、新生儿健康、儿童健康、生长标准、早期发展和养育照护的对象、链路、非目标和来源信号。
- 本域只做公开资料、变量模型、证据边界和反监控边界整理。
- 孕产/儿童个体医疗建议、育儿处方、发育诊断、家庭排名、保险筛选和家庭监控不属于本域。

## 上下游关系

- 上游：`reproductive-fertility-continuity/`、`nutrition-metabolic-health/` 和 `social-protection-benefits-delivery/`。
- 下游：`childcare-family-continuity/`、`learning-skill-acquisition/`、`mental-health-affective-stability/` 和 `healthcare-access-continuity/`。

## 维护规则

- 新增资料必须说明它支持的是孕产、新生儿、儿童健康、生长、早期发展、家庭调查还是养育照护变量。
- 不能把母婴儿童资料写成个体医疗、育儿、资格、保险、家庭监管或责任归因建议。
