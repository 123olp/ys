import * as d3 from "d3";

const scenarios = {
  baseline: {
    label: "基线",
    ai: 0.2,
    biomedical: 0.2,
    interfaceLevel: 0.05,
    waiting: 0.05,
    governance: 0.45
  },
  assisted: {
    label: "AI 辅助",
    ai: 0.55,
    biomedical: 0.35,
    interfaceLevel: 0.16,
    waiting: 0.08,
    governance: 0.52
  },
  convergence: {
    label: "指数技术汇聚",
    ai: 0.78,
    biomedical: 0.7,
    interfaceLevel: 0.42,
    waiting: 0.2,
    governance: 0.58
  },
  escape: {
    label: "LEV 临界探索",
    ai: 0.86,
    biomedical: 0.92,
    interfaceLevel: 0.5,
    waiting: 0.38,
    governance: 0.64
  }
};

const palette = {
  ink: "#15171a",
  muted: "#5f6673",
  faint: "#8a93a3",
  line: "#d9dee7",
  strong: "#b8c0cc",
  panel: "#ffffff",
  soft: "#f5f6f8",
  accent: "#24577a",
  green: "#39705f",
  amber: "#8a5a20",
  red: "#8a3434"
};

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function numeric(value, fallback) {
  const number = Number(value);
  return Number.isFinite(number) ? number : fallback;
}

function computeModel(values = {}) {
  const scenario = scenarios[values.scenario] ?? scenarios.convergence;
  const v = {
    ai: numeric(values.ai, scenario.ai),
    biomedical: numeric(values.biomedical, scenario.biomedical),
    interfaceLevel: numeric(values.interfaceLevel, scenario.interfaceLevel),
    waiting: numeric(values.waiting, scenario.waiting),
    governance: numeric(values.governance, scenario.governance)
  };
  const riskReduction = clamp(
    v.biomedical * 0.34 +
      v.ai * 0.16 +
      v.governance * 0.12 +
      v.waiting * 0.1 -
      Math.max(0, v.interfaceLevel - v.governance) * 0.08,
    0,
    0.72
  );
  const capabilityGain = clamp(v.ai * 0.42 + v.interfaceLevel * 0.34 + v.governance * 0.12, 0, 0.92);
  const subjectiveCompression = clamp(v.waiting * 0.55 + v.ai * 0.08, 0, 0.68);
  const levRatio = clamp(
    v.biomedical * 0.74 +
      v.ai * 0.18 +
      v.waiting * 0.16 +
      v.interfaceLevel * 0.1 -
      Math.max(0, 0.5 - v.governance) * 0.18,
    0.12,
    1.38
  );
  const distributionShift = 4 + riskReduction * 42 + capabilityGain * 10 + subjectiveCompression * 16;
  const effectiveLife = 82 + distributionShift + (levRatio >= 1 ? 35 + (levRatio - 1) * 80 : 0);
  const healthspan = 63 + riskReduction * 34 + capabilityGain * 7;
  const optionValue = clamp(capabilityGain * 0.45 + riskReduction * 0.3 + v.governance * 0.18, 0, 1);

  return {
    ...v,
    label: scenario.label,
    riskReduction,
    capabilityGain,
    subjectiveCompression,
    levRatio,
    distributionShift,
    effectiveLife,
    healthspan,
    optionValue,
    threshold: levRatio >= 1 ? "越过阈值 / 开放边界" : "低于阈值 / 有限边界",
    budget: {
      attention: Math.round((capabilityGain * 0.38 + riskReduction * 0.16) * 100),
      time: Math.round((distributionShift / 70 + subjectiveCompression * 0.22) * 100),
      recovery: Math.round((v.biomedical * 0.48 + v.governance * 0.18) * 100),
      option: Math.round(optionValue * 100)
    }
  };
}

function clear(element) {
  while (element.firstChild) element.removeChild(element.firstChild);
}

function drawMechanism(target, model) {
  clear(target);
  const width = Math.max(760, target.clientWidth || 860);
  const height = 520;
  const margin = {top: 70, right: 28, bottom: 32, left: 28};
  const columns = [
    {
      title: "技术信号",
      nodes: [
        {id: "compute", title: "计算成本下降", note: "加速回报"},
        {id: "ai", title: "AI 能力提升", note: "工具变量"}
      ]
    },
    {
      title: "中间变量",
      nodes: [
        {id: "bio", title: "医学信息化", note: "生物变量"},
        {id: "interface", title: "人机接口", note: "认知变量"},
        {id: "waiting", title: "等待压缩", note: "主观时间"},
        {id: "governance", title: "治理能力", note: "尾部风险"}
      ]
    },
    {
      title: "模型位置",
      nodes: [
        {id: "state", title: "主体状态 X_t", note: "状态向量"},
        {id: "hazard", title: "风险函数 λ(t)", note: "失效强度"},
        {id: "survival", title: "生存曲线 S(t)", note: "路径分布"}
      ]
    },
    {
      title: "价值读数",
      nodes: [
        {id: "lev", title: "LEV 临界", note: `${model.levRatio.toFixed(2)}x`, primary: true},
        {id: "effective", title: "预测有效寿命", note: model.levRatio >= 1 ? "开放边界" : `${model.effectiveLife.toFixed(1)} 年`},
        {id: "option", title: "未来选择权", note: `${Math.round(model.optionValue * 100)}%`}
      ]
    }
  ];
  const links = [
    ["compute", "ai"],
    ["ai", "bio"],
    ["ai", "interface"],
    ["ai", "waiting"],
    ["ai", "governance"],
    ["bio", "state"],
    ["interface", "state"],
    ["waiting", "state"],
    ["governance", "state"],
    ["state", "hazard"],
    ["hazard", "survival"],
    ["survival", "lev"],
    ["survival", "effective"],
    ["lev", "option"]
  ];
  const columnGap = 18;
  const colWidth = (width - margin.left - margin.right - columnGap * (columns.length - 1)) / columns.length;
  const nodeHeight = 60;
  const nodeGap = 14;
  const nodeMap = new Map();
  const markerId = `arrow-${Math.round(width)}`;

  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height])
    .attr("role", "img")
    .attr("aria-label", "Human Infra 技术信号到生命路径模型的机制图");

  svg.append("rect")
    .attr("width", width)
    .attr("height", height)
    .attr("rx", 6)
    .attr("fill", palette.soft);

  svg.append("text")
    .attr("x", margin.left)
    .attr("y", 38)
    .attr("fill", palette.ink)
    .attr("font-size", 18)
    .attr("font-weight", 850)
    .text("从奇点叙事到主体持续性模型");

  svg.append("text")
    .attr("x", width - margin.right)
    .attr("y", 38)
    .attr("fill", palette.muted)
    .attr("font-size", 12)
    .attr("font-weight", 760)
    .attr("text-anchor", "end")
    .text("技术信号 -> 变量 -> 风险函数 -> 价值读数");

  svg.append("defs")
    .append("marker")
    .attr("id", markerId)
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 10)
    .attr("refY", 0)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-4L10,0L0,4")
    .attr("fill", palette.strong);

  columns.forEach((column, columnIndex) => {
    const x = margin.left + columnIndex * (colWidth + columnGap);
    svg.append("rect")
      .attr("x", x)
      .attr("y", margin.top)
      .attr("width", colWidth)
      .attr("height", height - margin.top - margin.bottom)
      .attr("rx", 5)
      .attr("fill", palette.panel)
      .attr("stroke", palette.line);
    svg.append("text")
      .attr("x", x + 14)
      .attr("y", margin.top + 28)
      .attr("fill", palette.ink)
      .attr("font-size", 14)
      .attr("font-weight", 850)
      .text(column.title);

    column.nodes.forEach((node, nodeIndex) => {
      const y = margin.top + 58 + nodeIndex * (nodeHeight + nodeGap);
      nodeMap.set(node.id, {x, y, width: colWidth, height: nodeHeight});
      svg.append("rect")
        .attr("x", x + 12)
        .attr("y", y)
        .attr("width", colWidth - 24)
        .attr("height", nodeHeight)
        .attr("rx", 4)
        .attr("fill", node.primary ? "#eaf2f7" : "#fbfcfd")
        .attr("stroke", node.primary ? palette.accent : palette.line);
      svg.append("text")
        .attr("x", x + 24)
        .attr("y", y + 25)
        .attr("fill", palette.ink)
        .attr("font-size", 13)
        .attr("font-weight", 820)
        .text(node.title);
      svg.append("text")
        .attr("x", x + 24)
        .attr("y", y + 44)
        .attr("fill", palette.muted)
        .attr("font-size", 11)
        .attr("font-weight", 700)
        .text(node.note);
    });
  });

  for (const [source, targetId] of links) {
    const a = nodeMap.get(source);
    const b = nodeMap.get(targetId);
    if (!a || !b) continue;
    const x1 = a.x + a.width - 12;
    const y1 = a.y + a.height / 2;
    const x2 = b.x + 12;
    const y2 = b.y + b.height / 2;
    const mid = (x1 + x2) / 2;
    svg.append("path")
      .attr("d", `M${x1},${y1} C${mid},${y1} ${mid},${y2} ${x2},${y2}`)
      .attr("fill", "none")
      .attr("stroke", palette.strong)
      .attr("stroke-width", 1.4)
      .attr("marker-end", `url(#${markerId})`);
  }

  target.append(svg.node());
}

function survivalPoints(model) {
  const ages = d3.range(40, 141, 2);
  const base = ages.map((age) => ({
    age,
    baseline: Math.exp(-Math.pow(Math.max(0, age - 52), 2.32) / 3800),
    intervention: Math.exp(-Math.pow(Math.max(0, age - (52 + model.distributionShift * 0.72)), 2.24) / (3900 + model.riskReduction * 1800))
  }));
  if (model.levRatio >= 1) {
    return base.map((d) => ({
      ...d,
      intervention: Math.max(d.intervention, 0.34 + 0.1 * Math.sin((d.age - 40) / 12))
    }));
  }
  return base;
}

function drawSurvival(target, model) {
  clear(target);
  const width = Math.max(760, target.clientWidth || 900);
  const height = 470;
  const margin = {top: 42, right: 34, bottom: 62, left: 68};
  const data = survivalPoints(model);
  const x = d3.scaleLinear().domain([40, 140]).range([margin.left, width - margin.right]);
  const y = d3.scaleLinear().domain([0, 1]).range([height - margin.bottom, margin.top]);
  const line = (key) => d3.line()
    .x((d) => x(d.age))
    .y((d) => y(d[key]))
    .curve(d3.curveMonotoneX);

  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height])
    .attr("role", "img")
    .attr("aria-label", "预测有效寿命和生存曲线图");

  svg.append("rect").attr("width", width).attr("height", height).attr("rx", 6).attr("fill", "#ffffff");

  svg.append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(8).tickFormat((d) => `${d} 岁`))
    .call((g) => g.select(".domain").attr("stroke", palette.strong))
    .call((g) => g.selectAll("text").attr("font-weight", 700).attr("fill", palette.muted));
  svg.append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(5).tickFormat((d) => `${Math.round(d * 100)}%`))
    .call((g) => g.select(".domain").attr("stroke", palette.strong))
    .call((g) => g.selectAll("text").attr("font-weight", 700).attr("fill", palette.muted));

  svg.append("text")
    .attr("x", width / 2)
    .attr("y", height - 18)
    .attr("text-anchor", "middle")
    .attr("fill", palette.muted)
    .attr("font-weight", 800)
    .attr("font-size", 12)
    .text("年龄");
  svg.append("text")
    .attr("x", 18)
    .attr("y", height / 2)
    .attr("transform", `rotate(-90,18,${height / 2})`)
    .attr("text-anchor", "middle")
    .attr("fill", palette.muted)
    .attr("font-weight", 800)
    .attr("font-size", 12)
    .text("生存概率 S(t)");

  svg.append("line")
    .attr("x1", x(82))
    .attr("x2", x(82))
    .attr("y1", y(0))
    .attr("y2", y(1))
    .attr("stroke", palette.line)
    .attr("stroke-dasharray", "4 4");

  svg.append("line")
    .attr("x1", margin.left)
    .attr("x2", width - margin.right)
    .attr("y1", y(0.5))
    .attr("y2", y(0.5))
    .attr("stroke", palette.line)
    .attr("stroke-dasharray", "4 4");

  svg.append("path")
    .datum(data)
    .attr("d", line("baseline"))
    .attr("fill", "none")
    .attr("stroke", palette.faint)
    .attr("stroke-width", 2.2);
  svg.append("path")
    .datum(data)
    .attr("d", line("intervention"))
    .attr("fill", "none")
    .attr("stroke", model.levRatio >= 1 ? palette.green : palette.accent)
    .attr("stroke-width", 3);

  const effectiveX = x(Math.min(model.effectiveLife, 140));
  svg.append("circle")
    .attr("cx", effectiveX)
    .attr("cy", y(model.levRatio >= 1 ? 0.5 : 0.45))
    .attr("r", 5)
    .attr("fill", model.levRatio >= 1 ? palette.green : palette.accent);
  svg.append("text")
    .attr("x", Math.min(width - 230, effectiveX + 12))
    .attr("y", y(model.levRatio >= 1 ? 0.5 : 0.45) - 10)
    .attr("fill", palette.ink)
    .attr("font-size", 12)
    .attr("font-weight", 850)
    .text(model.levRatio >= 1 ? "临界值进入开放边界" : `预测有效寿命 ${model.effectiveLife.toFixed(1)} 岁`);

  const legend = [
    {label: "基线生命路径", color: palette.faint},
    {label: "干预后路径", color: model.levRatio >= 1 ? palette.green : palette.accent},
    {label: "50% 阈值", color: palette.line}
  ];
  const lg = svg.append("g").attr("transform", `translate(${margin.left},18)`);
  legend.forEach((item, index) => {
    const x0 = index * 150;
    lg.append("line").attr("x1", x0).attr("x2", x0 + 24).attr("y1", 0).attr("y2", 0).attr("stroke", item.color).attr("stroke-width", 3);
    lg.append("text").attr("x", x0 + 31).attr("y", 4).attr("fill", palette.muted).attr("font-size", 12).attr("font-weight", 760).text(item.label);
  });

  target.append(svg.node());
}

function readControls(root) {
  const values = {};
  root.querySelectorAll("[data-model-input]").forEach((input) => {
    values[input.name] = input.value;
  });
  return values;
}

function updateOutputs(root, model) {
  root.querySelectorAll("[data-output]").forEach((node) => {
    const key = node.dataset.output;
    const value = {
      effectiveLife: model.levRatio >= 1 ? "开放边界" : `${model.effectiveLife.toFixed(1)} 年`,
      levRatio: `${model.levRatio.toFixed(2)}x`,
      healthspan: `${model.healthspan.toFixed(1)} 年`,
      optionValue: `${Math.round(model.optionValue * 100)}%`,
      threshold: model.threshold,
      attention: `${model.budget.attention}%`,
      time: `${model.budget.time}%`,
      recovery: `${model.budget.recovery}%`,
      option: `${model.budget.option}%`
    }[key];
    if (value) node.textContent = value;
  });
  root.querySelectorAll("output[data-for]").forEach((node) => {
    const input = root.querySelector(`[name="${node.dataset.for}"]`);
    if (input) node.textContent = Number(input.value).toFixed(2);
  });
}

function initModelLab(root) {
  const survivalTarget = root.querySelector("[data-chart='survival']");
  const mechanismTarget = document.querySelector("[data-chart='mechanism']");

  function render() {
    const model = computeModel(readControls(root));
    updateOutputs(root, model);
    if (survivalTarget) drawSurvival(survivalTarget, model);
    if (mechanismTarget) drawMechanism(mechanismTarget, model);
  }

  root.querySelectorAll("[data-model-input]").forEach((input) => {
    input.addEventListener("input", render);
    input.addEventListener("change", render);
  });
  const scenarioInput = root.querySelector("[name='scenario']");
  if (scenarioInput) {
    scenarioInput.addEventListener("change", () => {
      const profile = scenarios[scenarioInput.value] ?? scenarios.convergence;
      for (const [key, value] of Object.entries(profile)) {
        if (key === "label") continue;
        const input = root.querySelector(`[name="${key}"]`);
        if (input) input.value = value;
      }
      render();
    });
  }
  render();
}

function initStaticCharts() {
  const mechanismTarget = document.querySelector("[data-chart='mechanism']");
  if (mechanismTarget && !document.querySelector("[data-model-lab]")) {
    drawMechanism(mechanismTarget, computeModel({scenario: "convergence"}));
  }
}

window.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-model-lab]").forEach(initModelLab);
  initStaticCharts();
});
