# Liver Cancer Cirrhosis Surveillance Treatment Continuity

`liver-cancer-cirrhosis-surveillance-treatment-continuity/` 研究肝癌、肝硬化监测、病毒性肝炎/MASLD 上游风险、超声/AFP 监测、治疗可及、肝功能储备和移植/支持照护入口如何影响主体持续性。

> 核心问题：肝癌连续性不只看肿瘤，也看肝硬化和肝功能储备；主体风险来自癌症进展、失代偿、感染/代谢上游和治疗窗口同时变化。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖肝脏解毒、代谢和合成能力长期维持
  -> 肝癌常与肝硬化、病毒性肝炎、MASLD/MASH 和失代偿风险交织
  -> 监测、治疗、肝功能储备、移植入口和上游风险治理决定主体是否保留生理冗余
  -> 因此肝癌是癌症连续性与肝脏基础设施交叉域
```

## 关注对象

- Liver cancer / hepatocellular carcinoma, cirrhosis surveillance, viral hepatitis, MASLD / MASH, ultrasound / AFP pathway, liver function reserve, treatment access, transplant / supportive continuity。
- 与 `chronic-viral-hepatitis-screening-liver-protection-continuity/` 和 `chronic-liver-disease-masld-mash-continuity/` 的关系：本域承接上游肝病风险进入肝癌监测和治疗窗口。
- 与 `renal-hepatic-clearance/` 的关系：肝功能储备是主体基础代谢设施的一部分。

## Human Infra 模型链路

```text
肝癌肝硬化监测系统 T
  -> 改变上游肝病控制、监测覆盖、异常追踪、治疗可及、肝功能储备和移植/支持入口变量 X
  -> 改变肿瘤阶段、肝失代偿、治疗耐受性、感染/出血风险和资源状态 S
  -> 改变死亡、急性失代偿、有效时间损失和照护资源消耗 λ(t)
  -> 影响主体健康寿命、生理冗余、行动能力和未来选择权
```

## 非目标

- 不提供超声/AFP 判读、监测频率、肝硬化分期、肝病治疗、抗病毒/代谢治疗、介入治疗、移植判断、用药或个体建议。
- 不生成个人肝癌风险计算器、影像/肿瘤标志物解释、治疗排序、移植资格判断或商业检测推广。
- 不收集个案肝病史、影像、AFP、病毒指标、肝功能、病理、饮酒史或治疗资料。

## Source Signals

- NCI liver cancer: https://www.cancer.gov/types/liver
- CDC liver cancer: https://www.cdc.gov/cancer/liver/
- CDC viral hepatitis: https://www.cdc.gov/hepatitis/

## 下一步

- 建立 Liver Cancer Continuity Card：cirrhosis surveillance, viral / metabolic upstream, abnormal follow-up, liver reserve, treatment access, transplant / supportive pathway。
- 与 `chronic-viral-hepatitis-screening-liver-protection-continuity/`、`chronic-liver-disease-masld-mash-continuity/` 和 `renal-hepatic-clearance/` 建立接口。
