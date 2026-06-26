---
title: 预测模型
---

```js
import {computeModel, kpiGrid, levGauge, lifePathDistribution, resourceBudgetChart, scenarioNames} from "./components/model.js";

const scenarioInput = Inputs.select(scenarioNames(), {
  label: "模型场景",
  format: (d) => d.label,
  value: "assisted"
});
const aiInput = Inputs.range([0, 1], {label: "AI 工具增强", step: 0.01, value: 0.55});
const biomedicalInput = Inputs.range([0, 1], {label: "生物医学信息化", step: 0.01, value: 0.42});
const interfaceInput = Inputs.range([0, 1], {label: "人机接口成熟度", step: 0.01, value: 0.18});
const waitingInput = Inputs.range([0, 1], {label: "主观等待压缩", step: 0.01, value: 0.08});
const governanceInput = Inputs.range([0, 1], {label: "治理与安全能力", step: 0.01, value: 0.52});

const scenario = Generators.input(scenarioInput);
const ai = Generators.input(aiInput);
const biomedical = Generators.input(biomedicalInput);
const interfaceLevel = Generators.input(interfaceInput);
const waiting = Generators.input(waitingInput);
const governance = Generators.input(governanceInput);
const model = computeModel({scenario, ai, biomedical, interfaceLevel, waiting, governance});
```

# 生命路径预测模型

这个模型把相关技术视为改变生命路径概率分布的干预算子。核心问题是：技术通过什么机制改变哪些变量，这些变量如何改变死亡风险、健康寿命、主体能力、有效时间、主观时间、相对时间和未来选择权。

```text
技术 T
  -> 中间变量 X
  -> 系统状态 S
  -> 风险函数 lambda(t)
  -> 生存曲线 S(t)
  -> 寿命 / 有效时间 / 主观时间 / 相对时间 / 未来选择权
```

<div class="model-top-grid">
  <div class="card control-panel">
    <h2>控制台</h2>
    <div class="control-stack">
      ${scenarioInput}
      ${aiInput}
      ${biomedicalInput}
      ${interfaceInput}
      ${waitingInput}
      ${governanceInput}
    </div>
  </div>
  ${kpiGrid(model, {className: "grid grid-cols-2 model-kpi-grid", cardClass: "card kpi-card"})}
</div>

<div class="grid grid-cols-2">
  <div class="card grid-colspan-2">
    <h2>寿命概率分布位移</h2>
    ${resize((width) => lifePathDistribution(model, {width, height: 440}))}
  </div>
  <div class="card">
    <h2>长寿逃逸速度临界</h2>
    ${resize((width) => levGauge(model, {width, height: 280}))}
  </div>
  <div class="card">
    <h2>通用资源预算增量</h2>
    ${resize((width) => resourceBudgetChart(model, {width, height: 320}))}
  </div>
</div>

## 模型读法

<div class="section-band">
  <p class="section-kicker">Model Contract</p>
  <h2>这张图表达什么</h2>
  <p class="long-copy">
    图上的曲线表达模型层面的生命路径分布移动，不用于个体命运预测。曲线右移表示死亡风险和失能风险被延后，健康状态积分增加，主体可以在更长窗口内保持行动能力、学习能力、修正能力和未来选择权。
  </p>
  <p class="long-copy">
    当 LEV 比率接近 1.0x 时，图表进入临界叙事：年度生命收益接近年度时间消耗。超过阈值时，预测有效寿命显示开放边界，表达模型临界状态，不输出确定寿命终点。
  </p>
</div>

## 四种时间

<div class="grid grid-cols-4">
  <div class="card compact-card accent-teal">
    <h2>寿命</h2>
    <p class="section-note">死亡时间 T 的概率分布。它关注主体何时终止。</p>
  </div>
  <div class="card compact-card accent-blue">
    <h2>有效时间</h2>
    <p class="section-note">生存时间中具备行动能力、判断能力、恢复能力和任务执行能力的部分。</p>
  </div>
  <div class="card compact-card accent-green">
    <h2>主观时间</h2>
    <p class="section-note">主体实际体验到的时间。休眠、等待压缩和相对论路径会改变主观成本。</p>
  </div>
  <div class="card compact-card accent-amber">
    <h2>相对时间</h2>
    <p class="section-note">主体时间与外部文明时间的比例。黑洞等待室、相对论飞船属于这一类叙事。</p>
  </div>
</div>

## 变量层

<table class="axis-table">
  <thead>
    <tr>
      <th>变量组</th>
      <th>包含什么</th>
      <th>影响路径</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>生物变量</td>
      <td>炎症、代谢、免疫、细胞损伤、肿瘤风险、心血管风险、神经退行性风险。</td>
      <td>改变疾病发生时间、恢复能力、死亡风险和健康寿命。</td>
    </tr>
    <tr>
      <td>认知变量</td>
      <td>判断力、学习速度、注意力、记忆、决策质量、问题定义能力。</td>
      <td>改变行动质量和策略选择，从间接路径影响风险暴露和资源配置。</td>
    </tr>
    <tr>
      <td>资源变量</td>
      <td>财富、时间、医疗可及性、信息可及性、社会支持和工作结构。</td>
      <td>改变可采取的干预集合和失败后的恢复能力。</td>
    </tr>
    <tr>
      <td>工具变量</td>
      <td>AI、检测、自动化、诊断、药物研发、知识管理和风险预警。</td>
      <td>改变观测能力、决策能力、执行成本和研发速度。</td>
    </tr>
    <tr>
      <td>环境变量</td>
      <td>污染、事故风险、工作强度、城市基础设施、社会稳定性和制度质量。</td>
      <td>改变尾部风险和日常损耗。</td>
    </tr>
    <tr>
      <td>恢复变量</td>
      <td>睡眠、修复、康复、压力恢复、系统冗余和医疗应急能力。</td>
      <td>改变系统从损伤状态返回可行动状态的速度。</td>
    </tr>
  </tbody>
</table>

## 数学位置

<div class="grid grid-cols-2">
  <div class="model-equation">
    <span>X_t = t 时刻主体状态</span>
    <span>A_t = t 时刻采取的技术或干预</span>
    <span>T = 死亡时间</span>
    <span>lambda(t) = t 时刻死亡风险</span>
  </div>
  <div class="model-equation">
    <span>P(X_{t+1} | X_t, A_t)</span>
    <span>lambda(t | X_t, A_t)</span>
    <span>S(t) = P(T > t)</span>
    <span>健康时间积分 = ∫ 生存状态 × 健康质量 dt</span>
  </div>
</div>

## 干预如何起作用

<ul class="chain-list">
  <li><b>改变当前状态</b>让身体、认知、资源或环境状态变好，例如诊断、药物、运动、睡眠、财富和工具。</li>
  <li><b>改变转移函数</b>让衰退更慢、恢复更快、疾病进展更慢、事故暴露更低。</li>
  <li><b>改变观测能力</b>更早发现风险，例如早筛、可穿戴设备、多组学检测和 AI 诊断。</li>
  <li><b>改变行动能力</b>让主体更容易做出正确选择，例如 AI 助手、医学决策支持、自动化和知识系统。</li>
  <li><b>改变外部世界速度</b>AI 加速医学、材料、制造和协作，使未来技术更早到达。</li>
</ul>

## 当前模型读数

<div class="grid grid-cols-2">
  <div class="card">
    <h2>变量位置</h2>
    <ul class="metric-list">
      <li><b>AI</b><span>改变认知放大、诊断、自动化、学习速度和行动能力。</span></li>
      <li><b>生物医学</b><span>改变疾病风险、恢复能力、健康寿命和衰退速度。</span></li>
      <li><b>人机接口</b><span>改变认知容量、记忆外部化和工具耦合强度。</span></li>
      <li><b>等待压缩</b><span>改变主观时间消耗和相对时间尺度。</span></li>
      <li><b>治理能力</b><span>降低尾部风险，并决定技术能否安全进入主体持续性系统。</span></li>
    </ul>
  </div>
  <div class="card">
    <h2>当前读数</h2>
    <ul class="metric-list">
      <li><b>路径位移</b><span>${model.distributionShift.toFixed(1)} 年，表示当前模型相对基线的中心位移。</span></li>
      <li><b>LEV</b><span>${model.levRatio.toFixed(2)}x，${model.boundary}。</span></li>
      <li><b>健康寿命</b><span>${model.healthspan.toFixed(1)} 年，表达健康质量积分的近似读数。</span></li>
      <li><b>选择权</b><span>${Math.round(model.optionValue * 100)}%，表达未来可选行动集合的相对开放程度。</span></li>
    </ul>
  </div>
</div>

## 判断公式

<div class="section-band">
  <div class="model-equation">
    <span>技术价值 =</span>
    <span>影响变量的重要性 × 因果路径可信度 × 效应大小 × 持续时间 × 可获得性 × 可组合性</span>
    <span>- 风险 - 不确定性 - 机会成本</span>
  </div>
  <p class="long-copy">
    这个公式用于组织判断，不作为最终数学定理。它要求每个技术都回答三个问题：影响什么变量，通过什么因果路径进入风险函数，以多大确定性延展主体持续性。
  </p>
</div>

## 长寿逃逸速度如何处理

<div class="grid grid-cols-3">
  <div class="card compact-card accent-amber">
    <h2>低于阈值</h2>
    <p class="section-note">年度生命收益小于年度时间消耗。寿命曲线可右移，但仍处在有限边界内。</p>
  </div>
  <div class="card compact-card accent-green">
    <h2>接近阈值</h2>
    <p class="section-note">医学和工具进步速度接近时间消耗速度，模型进入临界讨论区。</p>
  </div>
  <div class="card compact-card accent-teal">
    <h2>越过阈值</h2>
    <p class="section-note">预测有效寿命显示开放边界，表示模型临界状态，而非给出某个死亡日期。</p>
  </div>
</div>

## 禁止用途

<div class="grid grid-cols-2">
  <div class="card compact-card accent-rose">
    <h2>个体决策</h2>
    <p class="section-note">当前模型不能用于个体医疗建议、保险定价、雇佣筛选、个体死亡日期预测或任何剥夺权利的决策。</p>
  </div>
  <div class="card compact-card accent-blue">
    <h2>模型定位</h2>
    <p class="section-note">当前版本用于解释机制、展示研究方向和组织未来变量。真实预测需要数据、校准、外部验证和误差审计。</p>
  </div>
</div>

## 下一步模型化路线

<ul class="reading-list">
  <li><b>第一阶段：变量字典</b>为 AI、生物医学、接口、等待压缩和治理能力建立清晰定义。</li>
  <li><b>第二阶段：证据映射</b>把论文、数据集、临床试验、队列研究和工具报告接入每个变量。</li>
  <li><b>第三阶段：生存模型</b>从示意曲线进入 Cox、AFT、RMST、竞争风险或多状态模型。</li>
  <li><b>第四阶段：因果层</b>引入 DAG、目标试验模拟、时间变化混杂处理和敏感性分析。</li>
  <li><b>第五阶段：可视化治理</b>建立模型版本、参数说明、适用对象、失败边界和图表审查清单。</li>
</ul>
