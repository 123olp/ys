import * as d3 from "d3";
import * as Plot from "@observablehq/plot";

const SCENARIOS = {
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

export function scenarioNames() {
  return Object.entries(SCENARIOS).map(([value, profile]) => ({value, label: profile.label}));
}

export function computeModel({
  scenario = "assisted",
  ai,
  biomedical,
  interfaceLevel,
  waiting,
  governance
} = {}) {
  const key = scenarioKey(scenario);
  const profile = SCENARIOS[key] ?? SCENARIOS.assisted;
  const values = {
    ai: numeric(ai, profile.ai),
    biomedical: numeric(biomedical, profile.biomedical),
    interfaceLevel: numeric(interfaceLevel, profile.interfaceLevel),
    waiting: numeric(waiting, profile.waiting),
    governance: numeric(governance, profile.governance)
  };

  const riskReduction = clamp(
    values.biomedical * 0.34 +
      values.ai * 0.16 +
      values.governance * 0.12 +
      values.waiting * 0.1 -
      Math.max(0, values.interfaceLevel - values.governance) * 0.08,
    0,
    0.72
  );
  const capabilityGain = clamp(values.ai * 0.42 + values.interfaceLevel * 0.34 + values.governance * 0.12, 0, 0.92);
  const subjectiveCompression = clamp(values.waiting * 0.55 + values.ai * 0.08, 0, 0.68);
  const levRatio = clamp(
    values.biomedical * 0.74 +
      values.ai * 0.18 +
      values.waiting * 0.16 +
      values.interfaceLevel * 0.1 -
      Math.max(0, 0.5 - values.governance) * 0.18,
    0.12,
    1.38
  );
  const distributionShift = 4 + riskReduction * 42 + capabilityGain * 10 + subjectiveCompression * 16;
  const effectiveLife = 82 + distributionShift + (levRatio >= 1 ? 35 + (levRatio - 1) * 80 : 0);
  const healthspan = 63 + riskReduction * 34 + capabilityGain * 7;
  const optionValue = clamp(capabilityGain * 0.45 + riskReduction * 0.3 + values.governance * 0.18, 0, 1);

  return {
    label: profile.label,
    ...values,
    riskReduction,
    capabilityGain,
    subjectiveCompression,
    levRatio,
    distributionShift,
    effectiveLife,
    healthspan,
    optionValue,
    boundary: levRatio >= 1 ? "越过阈值 / 开放边界" : "低于阈值 / 有限边界",
    resourceBudget: {
      attention: Math.round((capabilityGain * 0.38 + riskReduction * 0.16) * 100),
      time: Math.round((distributionShift / 70 + subjectiveCompression * 0.22) * 100),
      energy: Math.round((riskReduction * 0.42 + values.biomedical * 0.18) * 100),
      cognition: Math.round(capabilityGain * 100),
      recovery: Math.round((values.biomedical * 0.48 + values.governance * 0.18) * 100),
      options: Math.round(optionValue * 100)
    }
  };
}

export function kpiCards(model) {
  return [
    {label: "预测有效寿命", value: model.levRatio >= 1 ? "开放边界" : `${model.effectiveLife.toFixed(1)} 年`},
    {label: "LEV 比率", value: `${model.levRatio.toFixed(2)}x`},
    {label: "健康寿命", value: `${model.healthspan.toFixed(1)} 年`},
    {label: "未来选择权", value: `${Math.round(model.optionValue * 100)}%`}
  ];
}

export function kpiGrid(model, {className = "grid grid-cols-4", cardClass = "kpi-card"} = {}) {
  const grid = document.createElement("div");
  grid.className = className;
  for (const item of kpiCards(model)) {
    const article = document.createElement("article");
    article.className = cardClass;
    const label = document.createElement("span");
    label.textContent = item.label;
    const value = document.createElement("strong");
    value.textContent = item.value;
    article.append(label, value);
    grid.append(article);
  }
  return grid;
}

export function mechanismMap(model, {width = 720, height = 420} = {}) {
  const academic = {
    ink: "#111827",
    muted: "#667085",
    line: "#cbd5e1",
    panel: "#f3f6f9",
    card: "#ffffff",
    accent: "#1f4e79",
    accentSoft: "#eef3f8"
  };
  const columns = [
    {
      title: "技术信号",
      note: "来自书籍叙事",
      items: [
        {id: "compute", title: "计算成本下降", note: "创新成本"},
        {id: "ai", title: "AI 能力提升", note: "工具变量"}
      ]
    },
    {
      title: "中间变量",
      note: "Human Infra 转译",
      items: [
        {id: "bio", title: "医学信息化", note: "生物变量"},
        {id: "interface", title: "人机接口", note: "认知变量"},
        {id: "resource", title: "资源预算", note: "时间/精力"},
        {id: "governance", title: "治理压力", note: "尾部风险"}
      ]
    },
    {
      title: "状态模型",
      note: "定量契约",
      items: [
        {id: "state", title: "主体状态 X_t", note: "状态向量"},
        {id: "hazard", title: "风险函数 λ(t)", note: "失效强度"},
        {id: "survival", title: "生存曲线 S(t)", note: "路径分布"}
      ]
    },
    {
      title: "价值读数",
      note: "网页输出",
      items: [
        {id: "continuity", title: "主体持续性", note: `LEV ${model.levRatio.toFixed(2)}x`, primary: true},
        {id: "effective", title: "预测有效寿命", note: model.levRatio >= 1 ? "开放边界" : `${model.effectiveLife.toFixed(1)} 年`},
        {id: "options", title: "未来选择权", note: `${Math.round(model.optionValue * 100)}%`}
      ]
    }
  ];
  const links = [
    ["compute", "ai"],
    ["ai", "bio"],
    ["ai", "interface"],
    ["ai", "resource"],
    ["ai", "governance"],
    ["bio", "state"],
    ["interface", "state"],
    ["resource", "state"],
    ["governance", "state"],
    ["state", "hazard"],
    ["hazard", "survival"],
    ["survival", "continuity"],
    ["survival", "effective"],
    ["continuity", "options"]
  ];
  const chartWidth = Math.max(width, 720);
  const margin = {top: 68, right: 22, bottom: 24, left: 22};
  const columnGap = 14;
  const cardGap = 12;
  const cardHeight = 56;
  const columnWidth = (chartWidth - margin.left - margin.right - columnGap * (columns.length - 1)) / columns.length;
  const itemTop = margin.top + 66;
  const markerId = `arrow-${Math.round(chartWidth)}-${Math.round(height)}`;
  const itemIndex = new Map();

  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, chartWidth, height])
    .attr("width", chartWidth)
    .attr("height", height)
    .attr("role", "img")
    .attr("aria-label", "指数技术汇入 Human Infra 的机制图");

  svg.append("rect").attr("width", chartWidth).attr("height", height).attr("rx", 8).attr("fill", academic.panel);
  svg.append("text")
    .attr("x", 24)
    .attr("y", 38)
    .attr("fill", academic.ink)
    .attr("font-weight", 800)
    .attr("font-size", 18)
    .text("从奇点叙事到主体持续性模型");
  svg.append("text")
    .attr("x", chartWidth - 24)
    .attr("y", 38)
    .attr("text-anchor", "end")
    .attr("fill", academic.muted)
    .attr("font-size", 12)
    .attr("font-weight", 700)
    .text("机制图 / 变量转译 / 风险函数");

  svg.append("defs")
    .append("marker")
    .attr("id", markerId)
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 9)
    .attr("refY", 0)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-4L9,0L0,4")
    .attr("fill", academic.line);

  columns.forEach((column, columnIndex) => {
    const columnX = margin.left + columnIndex * (columnWidth + columnGap);
    svg.append("rect")
      .attr("x", columnX)
      .attr("y", margin.top)
      .attr("width", columnWidth)
      .attr("height", height - margin.top - margin.bottom)
      .attr("rx", 6)
      .attr("fill", "#ffffff")
      .attr("stroke", academic.line);
    svg.append("text")
      .attr("x", columnX + 14)
      .attr("y", margin.top + 26)
      .attr("fill", academic.ink)
      .attr("font-size", 14)
      .attr("font-weight", 850)
      .text(column.title);
    svg.append("text")
      .attr("x", columnX + 14)
      .attr("y", margin.top + 48)
      .attr("fill", academic.muted)
      .attr("font-size", 11)
      .attr("font-weight", 700)
      .text(column.note);

    column.items.forEach((item, itemIndexInColumn) => {
      const x = columnX + 12;
      const y = itemTop + itemIndexInColumn * (cardHeight + cardGap);
      const w = columnWidth - 24;
      const h = cardHeight;
      itemIndex.set(item.id, {x, y, w, h, ...item});
    });
  });

  svg.append("g")
    .attr("fill", "none")
    .attr("stroke", academic.line)
    .attr("stroke-width", 1.6)
    .attr("stroke-opacity", 0.9)
    .attr("marker-end", `url(#${markerId})`)
    .selectAll("path")
    .data(links)
    .join("path")
    .attr("d", ([source, target]) => {
      const s = itemIndex.get(source);
      const t = itemIndex.get(target);
      const sx = s.x + s.w;
      const sy = s.y + s.h / 2;
      const tx = t.x;
      const ty = t.y + t.h / 2;
      const midX = sx + (tx - sx) / 2;
      return `M${sx},${sy} C${midX},${sy} ${midX},${ty} ${tx},${ty}`;
    });

  const item = svg.append("g").selectAll("g").data([...itemIndex.values()]).join("g");
  item.append("rect")
    .attr("x", (d) => d.x)
    .attr("y", (d) => d.y)
    .attr("width", (d) => d.w)
    .attr("height", (d) => d.h)
    .attr("rx", 5)
    .attr("fill", (d) => (d.primary ? academic.accentSoft : academic.card))
    .attr("stroke", (d) => (d.primary ? academic.accent : academic.line))
    .attr("stroke-width", (d) => (d.primary ? 1.8 : 1.2));
  item.append("text")
    .attr("x", (d) => d.x + 12)
    .attr("y", (d) => d.y + 23)
    .attr("fill", academic.ink)
    .attr("font-size", 12)
    .attr("font-weight", 850)
    .text((d) => d.title);
  item.append("text")
    .attr("x", (d) => d.x + 12)
    .attr("y", (d) => d.y + 43)
    .attr("fill", academic.muted)
    .attr("font-size", 10.5)
    .attr("font-weight", 700)
    .text((d) => d.note);

  return svg.node();
}

export function lifePathDistribution(model, {width = 760, height = 360} = {}) {
  const data = [];
  for (let age = 35; age <= 180; age += 1) {
    data.push({age, scenario: "基线", density: normal(age, 82, 10)});
    data.push({age, scenario: "当前模型", density: normal(age, Math.min(model.effectiveLife, 150), model.levRatio >= 1 ? 18 : 13)});
  }
  return Plot.plot({
    width,
    height,
    marginLeft: 56,
    marginBottom: 46,
    x: {label: "年龄 / 主体时间尺度", grid: true},
    y: {label: "生命路径概率密度", grid: true},
    color: {legend: true, domain: ["基线", "当前模型"], range: ["#98a2b3", "#1f4e79"]},
    marks: [
      Plot.lineY(data, {x: "age", y: "density", stroke: "scenario", strokeWidth: 2.6, curve: "basis"}),
      Plot.ruleX([82], {stroke: "#98a2b3", strokeDasharray: "4 4"}),
      Plot.ruleX([Math.min(model.effectiveLife, 150)], {stroke: "#1f4e79", strokeDasharray: "4 4"}),
      Plot.text([{age: 45, density: 0.035, label: `路径位移 +${model.distributionShift.toFixed(1)} 年`}], {
        x: "age",
        y: "density",
        text: "label",
        fill: "#111827",
        fontWeight: 800
      })
    ]
  });
}

export function levGauge(model, {width = 620, height = 240} = {}) {
  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height])
    .attr("width", width)
    .attr("height", height)
    .attr("role", "img")
    .attr("aria-label", "长寿逃逸速度临界图");
  const margin = {left: 44, right: 44, top: 72, bottom: 54};
  const x = d3.scaleLinear().domain([0, 1.4]).range([margin.left, width - margin.right]);
  svg.append("rect").attr("width", width).attr("height", height).attr("rx", 8).attr("fill", "#f3f6f9");
  svg.append("text").attr("x", margin.left).attr("y", 32).attr("font-size", 18).attr("font-weight", 800).text("LEV 临界面");
  svg.append("text").attr("x", margin.left).attr("y", 54).attr("fill", "#667085").attr("font-size", 13).text("年度生命收益 / 年度时间消耗，阈值为 1.0x");
  svg.append("line").attr("x1", x(0)).attr("x2", x(1.4)).attr("y1", 126).attr("y2", 126).attr("stroke", "#d0d5dd").attr("stroke-width", 10).attr("stroke-linecap", "round");
  svg.append("line").attr("x1", x(0)).attr("x2", x(model.levRatio)).attr("y1", 126).attr("y2", 126).attr("stroke", "#1f4e79").attr("stroke-width", 10).attr("stroke-linecap", "round");
  svg.append("line").attr("x1", x(1)).attr("x2", x(1)).attr("y1", 92).attr("y2", 160).attr("stroke", "#111827").attr("stroke-width", 2).attr("stroke-dasharray", "5 5");
  svg.append("circle").attr("cx", x(model.levRatio)).attr("cy", 126).attr("r", 16).attr("fill", "#111827");
  svg.append("text").attr("x", x(model.levRatio)).attr("y", 132).attr("text-anchor", "middle").attr("fill", "#fff").attr("font-size", 11).attr("font-weight", 800).text(model.levRatio.toFixed(2));
  svg.append("text").attr("x", margin.left).attr("y", 196).attr("fill", "#111827").attr("font-size", 15).attr("font-weight", 800).text(model.boundary);
  svg.append("text").attr("x", width - margin.right).attr("y", 196).attr("text-anchor", "end").attr("fill", "#667085").attr("font-size", 13).text(model.levRatio >= 1 ? "预测有效寿命进入开放边界" : "仍处在有限边界内");
  return svg.node();
}

export function resourceBudgetChart(model, {width = 620, height = 300} = {}) {
  const labels = {
    attention: "注意力",
    time: "有效时间",
    energy: "精力",
    cognition: "认知",
    recovery: "恢复",
    options: "未来选择权"
  };
  const data = Object.entries(model.resourceBudget).map(([key, value]) => ({resource: labels[key], value}));
  return Plot.plot({
    width,
    height,
    marginLeft: 72,
    marginBottom: 40,
    x: {label: "相对预算增量（%）", grid: true, domain: [0, 100]},
    y: {label: null},
    marks: [
      Plot.barX(data, {y: "resource", x: "value", fill: "#1f4e79", rx: 3}),
      Plot.text(data, {y: "resource", x: "value", text: (d) => `${d.value}%`, dx: 18, fill: "#111827", fontWeight: 800})
    ]
  });
}

export function bookSignalTable(signals) {
  const table = document.createElement("table");
  table.className = "signal-table";
  table.innerHTML = `
    <thead>
      <tr>
        <th>书中信号</th>
        <th>书内作用</th>
        <th>Human Infra 变量</th>
        <th>模型位置</th>
        <th>边界</th>
      </tr>
    </thead>
    <tbody>
      ${signals.map((row) => `
        <tr>
          <td><strong>${escapeHtml(row.signal)}</strong></td>
          <td>${escapeHtml(row.bookRole)}</td>
          <td>${escapeHtml(row.humanInfraVariable)}</td>
          <td>${escapeHtml(row.modelPosition)}</td>
          <td>${escapeHtml(row.boundary)}</td>
        </tr>
      `).join("")}
    </tbody>
  `;
  return table;
}

function normal(x, mean, sd) {
  return Math.exp(-0.5 * ((x - mean) / sd) ** 2) / (sd * Math.sqrt(2 * Math.PI));
}

function clamp(value, min, max) {
  const number = Number(value);
  if (!Number.isFinite(number)) return min;
  return Math.max(min, Math.min(max, number));
}

function scenarioKey(value) {
  if (value && typeof value === "object" && "value" in value) return value.value;
  return typeof value === "string" ? value : "assisted";
}

function numeric(value, fallback) {
  if (value && typeof value === "object" && "value" in value) value = value.value;
  const number = Number(value);
  return Number.isFinite(number) ? number : fallback;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}
