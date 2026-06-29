# Telomere Maintenance

Telomere Maintenance 负责整理端粒长度、端粒酶、复制衰老、组织更新、癌症风险和细胞分裂边界。

核心问题：

> 许多组织需要持续更新；端粒系统既限制过度复制，也可能限制长期修复能力，因此它同时连接衰老、癌症和组织再生。

## 先验位置

```text
主体持续性最大化
  -> 组织维护依赖细胞更新和复制边界
  -> 端粒缩短会影响复制能力、细胞衰老和组织更新
  -> 端粒酶激活又可能改变癌症风险和细胞选择压力
  -> 因此端粒维护是修复能力与肿瘤风险之间的边界条件
```

## 关注对象

- 端粒长度、端粒酶、复制衰老、组织更新、癌症风险和遗传端粒疾病。
- 端粒与细胞衰老、干细胞储备、免疫细胞更新和肿瘤发生的关系。
- 端粒指标作为风险变量的适用范围、测量误差和解释边界。
- 与 `cellular-senescence-clearance/` 的关系：本域关注复制边界和端粒机制；衰老细胞域关注 senescence burden 与 SASP。

## Human Infra 模型链路

```text
端粒相关干预 / 暴露 T
  -> 改变端粒长度、端粒酶活性、复制能力和衰老触发 X
  -> 改变组织更新状态 S
  -> 改变修复能力、免疫更新、癌症和退行风险
  -> 改变健康寿命和长期维护窗口
```

## 非目标

- 不提供端粒检测解释、端粒酶激活方案、补剂、药物或治疗建议。
- 不把端粒长度等同于真实年龄或寿命。
- 不忽略端粒延长与癌症风险之间的张力。

## Source Signals

- Hallmarks of Aging: https://pubmed.ncbi.nlm.nih.gov/36599349/
- NCI Telomeres and Cancer: https://www.cancer.gov/about-cancer/causes-prevention/genetics/telomeres-fact-sheet
