---
title: 科研标准
---

# 科研标准与工具链

Human Infra 的定量层需要从理论叙事进入可审查模型。这个页面记录当前 Web 应用应遵守的科研标准、工具链、模型报告结构和可视化规范。

## 总目标

<div class="section-band">
  <p class="section-kicker">Research Standard</p>
  <h2>从“概念解释”进入“可审查模型”</h2>
  <p class="long-copy">
    Human Infra 后续要整理资料、论文、数据集、工具和模型，把主体持续性问题从宏大叙事推进到可推导、可复核、可迭代的研究系统。网页承担两个职责：面向公众解释价值，面向研究者保留变量、证据、模型和边界。
  </p>
</div>

## 标准骨架

<div class="grid grid-cols-3">
  <div class="card compact-card accent-blue">
    <h2>论文阅读</h2>
    <p class="section-note">采用三遍阅读法：先判断主题、贡献和证据类型，再拆方法、变量、数据和反证条件，最后提炼可复用模型。</p>
  </div>
  <div class="card compact-card accent-teal">
    <h2>预测模型报告</h2>
    <p class="section-note">参考 TRIPOD / TRIPOD+AI 和 PROBAST，记录目标、数据、变量、验证、偏差、适用对象和限制。</p>
  </div>
  <div class="card compact-card accent-green">
    <h2>干预证据</h2>
    <p class="section-note">医学和 AI 干预研究参考 CONSORT-AI、SPIRIT-AI、目标试验模拟和因果推断框架。</p>
  </div>
</div>

## 方法栈

<table class="axis-table">
  <thead>
    <tr>
      <th>方法</th>
      <th>解决的问题</th>
      <th>Human Infra 中的位置</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>生存分析</td>
      <td>寿命 T、生存函数 S(t)、风险函数 lambda(t)、RMST、竞争风险和多状态模型。</td>
      <td>解释寿命、健康寿命、疾病发生时间、失能时间和死亡风险。</td>
    </tr>
    <tr>
      <td>因果推断</td>
      <td>DAG、SCM、反事实、do(X)、时间变化混杂、中介效应和敏感性分析。</td>
      <td>判断某项技术或因素是否真正改变生命路径分布。</td>
    </tr>
    <tr>
      <td>动态决策</td>
      <td>状态 X_t、行动 A_t、状态转移、策略 pi、控制论和受约束的 MDP 表达。</td>
      <td>表达长期策略如何持续改变主体状态。</td>
    </tr>
    <tr>
      <td>可靠性工程</td>
      <td>故障率、冗余、恢复能力、单点故障、尾部风险和复杂系统失效。</td>
      <td>把人体、工具、环境和协作视为多子系统共同维持的复杂系统。</td>
    </tr>
    <tr>
      <td>统计建模</td>
      <td>贝叶斯模型、层级模型、纵向数据分析、缺失数据处理和不确定性量化。</td>
      <td>从真实数据估计变量影响，避免把叙事强度当作证据强度。</td>
    </tr>
  </tbody>
</table>

## 研究对象契约

<div class="grid grid-cols-2">
  <div class="card compact-card">
    <h2>对象</h2>
    <ul>
      <li>主体持续性。</li>
      <li>寿命、健康寿命和有效时间。</li>
      <li>主观时间与相对时间。</li>
      <li>未来选择权。</li>
      <li>技术干预、资源约束和治理能力。</li>
    </ul>
  </div>
  <div class="card compact-card">
    <h2>边界</h2>
    <ul>
      <li>不输出个体死亡日期。</li>
      <li>不提供医学诊断或治疗建议。</li>
      <li>不把远期技术设想写成事实。</li>
      <li>不把 AI 总结当作事实源。</li>
      <li>不让图表掩盖证据不足。</li>
    </ul>
  </div>
</div>

## 数据与证据层级

<ul class="chain-list">
  <li><b>机制合理性</b>理论上可能影响某个变量，例如炎症、代谢、认知负荷、风险暴露或资源可及性。</li>
  <li><b>动物与体外实验</b>证明机制存在，但外推到人类长期寿命仍需谨慎。</li>
  <li><b>人体早期数据</b>提供安全性、剂量、可行性和短期生物标志物变化。</li>
  <li><b>疾病终点</b>观察真实疾病发生、进展或恢复，而非只看替代指标。</li>
  <li><b>死亡率与健康寿命</b>直接进入寿命模型，是最高价值但最难获得的证据。</li>
  <li><b>长期安全性</b>处理副作用、尾部风险、个体差异、可重复性和机会成本。</li>
</ul>

## Web 实现标准

<div class="grid grid-cols-2">
  <div class="card compact-card accent-teal">
    <h2>当前主栈</h2>
    <ul>
      <li>Observable Framework：多页科研叙事和数据应用。</li>
      <li>D3：机制图、网络图、阈值图和复杂自定义 SVG。</li>
      <li>Observable Plot：生存曲线、预算条形图、统计图。</li>
      <li>Markdown：页面叙事、公式、说明和引用入口。</li>
    </ul>
  </div>
  <div class="card compact-card accent-blue">
    <h2>升级触发</h2>
    <ul>
      <li>出现真实纵向数据集后，接入 data loader。</li>
      <li>出现多模型版本后，建立模型 registry。</li>
      <li>出现可复现实验后，接入 Quarto / notebook。</li>
      <li>出现公众传播长卷后，单独引入 scrollytelling 页面。</li>
    </ul>
  </div>
</div>

## 图表规范

<table class="axis-table">
  <thead>
    <tr>
      <th>图表</th>
      <th>用途</th>
      <th>工具</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>机制图</td>
      <td>展示计算、AI、医学、接口、资源和治理如何汇入主体持续性。</td>
      <td>D3 SVG。</td>
    </tr>
    <tr>
      <td>生命路径概率分布</td>
      <td>展示基线曲线和当前模型曲线的右移。</td>
      <td>Observable Plot。</td>
    </tr>
    <tr>
      <td>LEV 临界图</td>
      <td>展示年度生命收益与年度时间消耗的阈值关系。</td>
      <td>D3 SVG。</td>
    </tr>
    <tr>
      <td>资源预算图</td>
      <td>展示注意力、有效时间、精力、认知、恢复和未来选择权的增量。</td>
      <td>Observable Plot。</td>
    </tr>
    <tr>
      <td>证据矩阵</td>
      <td>展示每项技术的证据等级、效应路径、风险和适用边界。</td>
      <td>Markdown table / Arquero / Data loader。</td>
    </tr>
  </tbody>
</table>

## 模型报告模板

<div class="grid grid-cols-3">
  <div class="card compact-card">
    <h2>1. 目标</h2>
    <p class="section-note">明确估计目标：寿命、健康寿命、有效时间、主观时间、相对时间或未来选择权。</p>
  </div>
  <div class="card compact-card">
    <h2>2. 人群</h2>
    <p class="section-note">记录适用对象、年龄范围、健康状态、地区、数据来源和排除条件。</p>
  </div>
  <div class="card compact-card">
    <h2>3. 变量</h2>
    <p class="section-note">定义状态变量、干预变量、混杂变量、中介变量和观测指标。</p>
  </div>
  <div class="card compact-card">
    <h2>4. 模型</h2>
    <p class="section-note">说明生存模型、因果模型、状态转移模型或动态决策模型的选择理由。</p>
  </div>
  <div class="card compact-card">
    <h2>5. 验证</h2>
    <p class="section-note">记录内部验证、外部验证、校准、敏感性分析和失败案例。</p>
  </div>
  <div class="card compact-card">
    <h2>6. 边界</h2>
    <p class="section-note">写清适用范围、风险、误用场景、数据缺口和后续升级触发条件。</p>
  </div>
</div>

## 后续资料沉淀

<ul class="reading-list">
  <li><b>论文库</b>按生存分析、因果推断、AI 医学、长寿干预、脑机接口、风险治理分组。</li>
  <li><b>工具库</b>按 Observable、D3、Plot、Quarto、R survival、lifelines、PyMC、DoWhy 等方向沉淀。</li>
  <li><b>证据库</b>把每项技术的机制、证据、风险、成本、可获得性和组合性结构化。</li>
  <li><b>模型库</b>保存模型版本、参数、输入输出契约、可视化模板和验证结果。</li>
</ul>

## 来源入口

- Observable Framework: <https://observablehq.com/framework/>
- D3: <https://d3js.org/>
- Observable Plot: <https://observablehq.com/plot/>
- Quarto: <https://quarto.org/>
- TRIPOD: <https://www.tripod-statement.org/>
- PROBAST: <https://www.probast.org/>
- CONSORT-AI: <https://www.equator-network.org/reporting-guidelines/consort-artificial-intelligence/>
- Stanford How to Read a Paper: <https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf>
