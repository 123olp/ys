---
title: Human Infra × 奇点更近
toc: false
---

```js
import {computeModel, kpiGrid, mechanismMap, scenarioNames} from "./components/model.js";

const scenarioInput = Inputs.select(scenarioNames(), {
  label: "模型场景",
  format: (d) => d.label,
  value: "convergence"
});
const scenario = Generators.input(scenarioInput);
const model = computeModel({scenario});
```

<div class="hero-block">
  <section class="hero-copy">
    <div class="eyebrow">Research Narrative / Life-Path Model</div>
    <h1 class="hero-title">把奇点叙事接入人类基础设施</h1>
    <p class="lead">
      这套页面把《奇点更近》的学习资料、Human Infra 的主体持续性理论、寿命与有效时间的预测模型、科研论文标准和交互可视化组织成一个可传播、可迭代、可审查的研究作品。
    </p>
    <div class="pill-row">
      <span>书籍介绍</span>
      <span>主体持续性</span>
      <span>概率分布</span>
      <span>长寿逃逸速度</span>
      <span>科研标准</span>
      <span>传播作品</span>
    </div>
  </section>
  <section class="hero-visual-card">
    ${resize((width) => mechanismMap(model, {width, height: 520}))}
  </section>
</div>

${kpiGrid(model)}

<div class="section-band">
  <p class="section-kicker">Core Thesis</p>
  <h2>这是一套 Human Infra 的外部语料接入实验</h2>
  <p class="long-copy">
    《奇点更近》给出的关键价值，是把 AI、计算、生物技术、纳米技术、脑机接口、工作重组、长寿医学和文明风险放到同一个指数技术叙事里。Human Infra 要做的，是把这类叙事拆成变量、因果链、证据边界和模型位置，观察它们如何改变一个主体继续存在、继续行动、继续学习、继续修正和继续进入未来的能力。
  </p>
  <div class="grid grid-cols-3">
    <div class="card compact-card accent-teal">
      <h2>书籍层</h2>
      <p class="section-note">整理作者关于加速回报、AI 接近人类水平、人机融合、长寿逃逸速度、纳米技术和风险治理的观点。</p>
    </div>
    <div class="card compact-card accent-blue">
      <h2>理论层</h2>
      <p class="section-note">把书中信号转成 Human Infra 的主体持续性变量：寿命、健康寿命、有效时间、主观时间、相对时间和未来选择权。</p>
    </div>
    <div class="card compact-card accent-green">
      <h2>模型层</h2>
      <p class="section-note">把宏观叙事变成可讨论的预测模型：变量影响状态，状态改变风险函数，风险函数改变生命路径概率分布。</p>
    </div>
  </div>
</div>

## 项目问题

<div class="grid grid-cols-2">
  <div class="statement-panel">
    <strong>Human Infra 的核心问题</strong>
    <p class="section-note">
      一切价值、目标和创造，都预设一个能够持续行动的主体。主体持续性受到衰老、疾病、资源约束、认知上限、环境风险和制度风险侵蚀。主体一旦终止，感知、判断、行动、学习、创造和未来选择权同步终止。
    </p>
  </div>
  <div class="statement-panel">
    <strong>本 Web 的核心问题</strong>
    <p class="section-note">
      如何把“奇点”“AI”“长寿逃逸速度”“脑机接口”“医学信息化”这类宏大概念，转成可观察变量、可解释图表、可验证假设和可持续扩写的研究页面。
    </p>
  </div>
</div>

<ul class="chain-list">
  <li><b>边界条件</b>主体能够持续存在和持续行动，是所有事业、成果、选择、学习和创造的前提。</li>
  <li><b>定性阶段</b>先解释价值链：主体持续性为什么重要，哪些技术和制度进入 Human Infra 的范围。</li>
  <li><b>定量阶段</b>再建立预测契约：因素如何影响风险函数、生存曲线、有效时间、主观时间和未来选择权。</li>
  <li><b>作品阶段</b>把材料、模型、图表和判断标准做成网页，让不同读者能快速理解项目价值。</li>
</ul>

## 从《奇点更近》抽取的六组信号

<div class="grid grid-cols-3">
  <div class="card compact-card accent-blue">
    <span class="big-number">01</span>
    <h2>加速回报</h2>
    <p class="section-note">计算成本下降，创新成本下降，更多领域被信息化，AI 参与下一轮科学发现。它给 Human Infra 提供“技术进步速度”变量。</p>
  </div>
  <div class="card compact-card accent-teal">
    <span class="big-number">02</span>
    <h2>AI 增强</h2>
    <p class="section-note">AI 从语言、代码、医学、材料和模拟进入任务执行系统，改变判断质量、学习速度、自动化能力和行动密度。</p>
  </div>
  <div class="card compact-card accent-green">
    <span class="big-number">03</span>
    <h2>医学信息化</h2>
    <p class="section-note">基因组学、蛋白质结构预测、药物发现和个体化检测，把生命系统逐步转成可计算对象。</p>
  </div>
  <div class="card compact-card accent-amber">
    <span class="big-number">04</span>
    <h2>长寿逃逸速度</h2>
    <p class="section-note">当每年医学进步带来的生命收益接近或超过一年时间消耗，寿命边界从固定终局转向开放临界。</p>
  </div>
  <div class="card compact-card accent-rose">
    <span class="big-number">05</span>
    <h2>人机接口</h2>
    <p class="section-note">脑机接口和云端新皮质的远期设想，进入认知容量、记忆外部化、身份连续性和工具耦合问题。</p>
  </div>
  <div class="card compact-card accent-blue">
    <span class="big-number">06</span>
    <h2>技术风险</h2>
    <p class="section-note">核、生物、纳米和 AI 风险说明强技术必须与治理能力共同建模，尾部风险会反向吞噬主体持续性收益。</p>
  </div>
</div>

## Human Infra 的转译链

<div class="section-band">
  <div class="model-equation">
    <span>书中宏观信号 -> Human Infra 变量</span>
    <span>Human Infra 变量 -> 主体状态 X_t</span>
    <span>主体状态 X_t -> 风险函数 lambda(t)</span>
    <span>风险函数 lambda(t) -> 生存曲线 S(t)</span>
    <span>生存曲线 S(t) + 健康质量 + 主观时间压缩 -> 有效持续时间与未来选择权</span>
  </div>
</div>

<table class="axis-table">
  <thead>
    <tr>
      <th>书籍概念</th>
      <th>Human Infra 转译</th>
      <th>网页表达</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>奇点</td>
      <td>智能、生命、制造和治理系统的共同加速阶段。</td>
      <td>首页机制图与书籍转译页。</td>
    </tr>
    <tr>
      <td>长寿逃逸速度</td>
      <td>寿命边界是否从固定终局转向开放临界。</td>
      <td>模型页 LEV 临界图。</td>
    </tr>
    <tr>
      <td>AI 与人类融合</td>
      <td>主体能力向量被工具、接口和外部智能放大。</td>
      <td>通用资源预算图和变量说明。</td>
    </tr>
    <tr>
      <td>风险治理</td>
      <td>技术收益和技术尾部风险共同决定未来路径分布。</td>
      <td>科研标准页和模型治理说明。</td>
    </tr>
  </tbody>
</table>

## 页面导航

<div class="grid grid-cols-3">
  <a class="card compact-card accent-teal" href="./book">
    <h2>书籍转译</h2>
    <p class="section-note">把《奇点更近》的核心问题、章节主线、概念定义、因果链、证据边界和误读点转成 Human Infra 语料。</p>
  </a>
  <a class="card compact-card accent-blue" href="./model">
    <h2>预测模型</h2>
    <p class="section-note">用交互控件展示技术变量如何改变风险函数、生存曲线、LEV 阈值、有效时间和通用资源预算。</p>
  </a>
  <a class="card compact-card accent-green" href="./research-standards">
    <h2>科研标准</h2>
    <p class="section-note">沉淀论文阅读、生存分析、因果推断、预测报告规范、可视化工具和模型治理要求。</p>
  </a>
</div>

## 作品路线

<div class="grid grid-cols-4">
  <div class="card compact-card">
    <h2>资料整理</h2>
    <p class="section-note">把书籍、论文、工具、典故、谱系和讨论材料整理成稳定语料。</p>
  </div>
  <div class="card compact-card">
    <h2>理论组织</h2>
    <p class="section-note">把主体持续性、通用资源、技术干预和未来选择权放到同一条主线。</p>
  </div>
  <div class="card compact-card">
    <h2>模型推导</h2>
    <p class="section-note">从定性判断进入定量契约，明确变量、路径、阈值和风险函数。</p>
  </div>
  <div class="card compact-card">
    <h2>可视化传播</h2>
    <p class="section-note">用网页、图表和长文解释项目价值，使非专业读者能理解核心问题。</p>
  </div>
</div>

## 阅读顺序

<ul class="reading-list">
  <li><b>第一步：先看书籍转译</b>理解《奇点更近》提供了哪些外部信号，以及这些信号如何进入 Human Infra。</li>
  <li><b>第二步：再看预测模型</b>理解技术作为干预算子，如何改变状态转移、死亡风险、健康质量和未来选择权。</li>
  <li><b>第三步：最后看科研标准</b>理解这个 Web 后续如何从展示走向可审查、可复现、可迭代的研究系统。</li>
</ul>

## 边界声明

<div class="section-band">
  <p class="long-copy">
    这里展示的是研究框架和学习化转译，不输出个体死亡日期，不提供医学建议，不把书中预测写成已经实现的事实。它建立一个框架：把未来技术放进主体持续性模型里，判断它改变了哪些变量、通过什么路径改变风险函数、以多大确定性扩展主体继续行动的窗口。
  </p>
</div>
