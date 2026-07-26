import * as d3 from "d3";

const palette = {
  ink: "#15171a",
  muted: "#5f6673",
  line: "#d9dee7",
  strong: "#b8c0cc",
  paper: "#ffffff",
  soft: "#f5f6f8",
  blue: "#24577a",
  green: "#39705f",
  amber: "#8a5a20",
  red: "#8a3434"
};

function readModel() {
  const element = document.getElementById("lev-model-data");
  if (!element?.textContent) return null;
  try {
    return JSON.parse(element.textContent);
  } catch (error) {
    console.error("Failed to parse LEV model data", error);
    return null;
  }
}

function clear(target) {
  while (target.firstChild) target.removeChild(target.firstChild);
}

function createSvg(target, height, label) {
  clear(target);
  const width = Math.max(760, target.clientWidth || 900);
  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height])
    .attr("role", "img")
    .attr("aria-label", label);

  svg.append("rect")
    .attr("width", width)
    .attr("height", height)
    .attr("rx", 6)
    .attr("fill", palette.soft);

  target.append(svg.node());
  return {svg, width, height};
}

function drawGateChart(target, model) {
  const gates = model.summaries.gateCounts;
  const {svg, width, height} = createSvg(target, 420, "LEV 概率门断点分布图");
  const margin = {top: 58, right: 28, bottom: 82, left: 56};
  const x = d3.scaleBand()
    .domain(gates.map((gate) => gate.id))
    .range([margin.left, width - margin.right])
    .padding(0.24);
  const y = d3.scaleLinear()
    .domain([0, d3.max(gates, (gate) => gate.count) ?? 1])
    .nice()
    .range([height - margin.bottom, margin.top]);

  svg.append("text")
    .attr("x", margin.left)
    .attr("y", 34)
    .attr("fill", palette.ink)
    .attr("font-size", 18)
    .attr("font-weight", 850)
    .text("概率门出现频次");

  svg.append("text")
    .attr("x", width - margin.right)
    .attr("y", 34)
    .attr("fill", palette.muted)
    .attr("font-size", 12)
    .attr("font-weight", 760)
    .attr("text-anchor", "end")
    .text("路线卡 + 多阶效应卡");

  svg.append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(5))
    .call((g) => g.select(".domain").remove())
    .call((g) => g.selectAll("line").attr("stroke", palette.line))
    .call((g) => g.selectAll("text").attr("fill", palette.muted));

  svg.append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x))
    .call((g) => g.selectAll("text")
      .attr("transform", "rotate(-35)")
      .attr("text-anchor", "end")
      .attr("fill", palette.muted)
      .attr("font-size", 11))
    .call((g) => g.select(".domain").attr("stroke", palette.line));

  svg.append("g")
    .selectAll("rect")
    .data(gates)
    .join("rect")
    .attr("x", (gate) => x(gate.id))
    .attr("y", (gate) => y(gate.count))
    .attr("width", x.bandwidth())
    .attr("height", (gate) => y(0) - y(gate.count))
    .attr("rx", 4)
    .attr("fill", (gate) => gate.id.includes("avoid") || gate.id.includes("calibrate") ? palette.amber : palette.blue);

  svg.append("g")
    .selectAll("text")
    .data(gates)
    .join("text")
    .attr("x", (gate) => (x(gate.id) ?? 0) + x.bandwidth() / 2)
    .attr("y", (gate) => y(gate.count) - 8)
    .attr("text-anchor", "middle")
    .attr("fill", palette.ink)
    .attr("font-size", 12)
    .attr("font-weight", 850)
    .text((gate) => gate.count);
}

function drawRouteGateMatrix(target, model) {
  const routes = model.routeCards;
  const gates = model.summaries.gateCounts.map((gate) => gate.id);
  const {svg, width, height} = createSvg(target, 520, "LEV 路线与概率门矩阵");
  const margin = {top: 72, right: 24, bottom: 38, left: 160};
  const x = d3.scaleBand().domain(gates).range([margin.left, width - margin.right]).padding(0.12);
  const y = d3.scaleBand().domain(routes.map((route) => route.route_id)).range([margin.top, height - margin.bottom]).padding(0.16);

  svg.append("text")
    .attr("x", margin.left)
    .attr("y", 34)
    .attr("fill", palette.ink)
    .attr("font-size", 18)
    .attr("font-weight", 850)
    .text("主流路线 x 概率门");

  svg.append("text")
    .attr("x", margin.left)
    .attr("y", 54)
    .attr("fill", palette.muted)
    .attr("font-size", 12)
    .text("颜色表示该路线明确依赖或受该门槛约束");

  svg.append("g")
    .selectAll("text")
    .data(routes)
    .join("text")
    .attr("x", margin.left - 12)
    .attr("y", (route) => (y(route.route_id) ?? 0) + y.bandwidth() / 2 + 4)
    .attr("text-anchor", "end")
    .attr("fill", palette.ink)
    .attr("font-size", 12)
    .attr("font-weight", 760)
    .text((route) => `${route.route_id} ${route.route_name}`);

  svg.append("g")
    .selectAll("text")
    .data(gates)
    .join("text")
    .attr("x", (gate) => (x(gate) ?? 0) + x.bandwidth() / 2)
    .attr("y", margin.top - 16)
    .attr("text-anchor", "middle")
    .attr("fill", palette.muted)
    .attr("font-size", 11)
    .attr("font-weight", 760)
    .text((gate) => gate.replace("P_", ""));

  const cells = routes.flatMap((route) => gates.map((gate) => ({route, gate, active: route.gates.includes(gate)})));
  svg.append("g")
    .selectAll("rect")
    .data(cells)
    .join("rect")
    .attr("x", (cell) => x(cell.gate))
    .attr("y", (cell) => y(cell.route.route_id))
    .attr("width", x.bandwidth())
    .attr("height", y.bandwidth())
    .attr("rx", 4)
    .attr("fill", (cell) => cell.active ? palette.green : palette.paper)
    .attr("stroke", palette.line);
}

function drawFlywheel(target, model) {
  const resources = ["时间", "注意力", "认知", "记忆", "AI", "资金", "社会支持", "环境"];
  const gates = ["P_notice", "P_understand", "P_access", "P_adopt", "P_persist", "P_recover", "P_calibrate"];
  const outputs = ["健康寿命", "有效时间", "技术窗口", "未来选择权"];
  const {svg, width, height} = createSvg(target, 460, "LEV 正向飞轮与负向反噬图");
  const markerId = `lev-arrow-${Math.round(width)}`;
  const columns = [
    {title: "资源层", values: resources},
    {title: "概率门", values: gates},
    {title: "输出层", values: outputs}
  ];
  const margin = {top: 74, right: 28, bottom: 42, left: 28};
  const columnWidth = (width - margin.left - margin.right - 48) / 3;

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

  svg.append("text")
    .attr("x", margin.left)
    .attr("y", 34)
    .attr("fill", palette.ink)
    .attr("font-size", 18)
    .attr("font-weight", 850)
    .text("二阶 / 多阶飞轮");

  svg.append("text")
    .attr("x", margin.left)
    .attr("y", 55)
    .attr("fill", palette.muted)
    .attr("font-size", 12)
    .text("资源不是外围条件，而是改变技术采用、恢复、校准和扩散的上游门槛");

  const positions = new Map();
  columns.forEach((column, columnIndex) => {
    const x = margin.left + columnIndex * (columnWidth + 24);
    svg.append("rect")
      .attr("x", x)
      .attr("y", margin.top)
      .attr("width", columnWidth)
      .attr("height", height - margin.top - margin.bottom)
      .attr("rx", 6)
      .attr("fill", palette.paper)
      .attr("stroke", palette.line);
    svg.append("text")
      .attr("x", x + 14)
      .attr("y", margin.top + 26)
      .attr("fill", palette.ink)
      .attr("font-size", 14)
      .attr("font-weight", 850)
      .text(column.title);

    column.values.forEach((value, valueIndex) => {
      const y = margin.top + 52 + valueIndex * 38;
      positions.set(value, {x: x + 12, y, w: columnWidth - 24, h: 26});
      svg.append("rect")
        .attr("x", x + 12)
        .attr("y", y)
        .attr("width", columnWidth - 24)
        .attr("height", 26)
        .attr("rx", 4)
        .attr("fill", value.startsWith("P_") ? "#eef3f6" : "#fbfcfd")
        .attr("stroke", value.startsWith("P_") ? palette.blue : palette.line);
      svg.append("text")
        .attr("x", x + 24)
        .attr("y", y + 18)
        .attr("fill", palette.ink)
        .attr("font-size", 12)
        .attr("font-weight", 760)
        .text(value);
    });
  });

  const links = [
    ["时间", "P_adopt"], ["注意力", "P_calibrate"], ["认知", "P_understand"], ["记忆", "P_persist"],
    ["AI", "P_notice"], ["资金", "P_access"], ["社会支持", "P_recover"], ["环境", "P_access"],
    ["P_notice", "技术窗口"], ["P_understand", "未来选择权"], ["P_access", "技术窗口"],
    ["P_adopt", "健康寿命"], ["P_recover", "有效时间"], ["P_calibrate", "未来选择权"]
  ];
  svg.append("g")
    .selectAll("path")
    .data(links)
    .join("path")
    .attr("d", ([from, to]) => {
      const a = positions.get(from);
      const b = positions.get(to);
      const x1 = a.x + a.w;
      const y1 = a.y + a.h / 2;
      const x2 = b.x;
      const y2 = b.y + b.h / 2;
      const mid = (x1 + x2) / 2;
      return `M${x1},${y1} C${mid},${y1} ${mid},${y2} ${x2},${y2}`;
    })
    .attr("fill", "none")
    .attr("stroke", palette.strong)
    .attr("stroke-width", 1.2)
    .attr("marker-end", `url(#${markerId})`);

  const warning = svg.append("g").attr("transform", `translate(${margin.left},${height - 30})`);
  warning.append("rect")
    .attr("width", width - margin.left - margin.right)
    .attr("height", 24)
    .attr("rx", 4)
    .attr("fill", "#fff6f6")
    .attr("stroke", "#d7b8b8");
  warning.append("text")
    .attr("x", 12)
    .attr("y", 16)
    .attr("fill", palette.red)
    .attr("font-size", 12)
    .attr("font-weight", 760)
    .text("负向飞轮同等重要：更多 AI / 资金 / 指标反馈也可能放大伪疗法、Goodhart、错误自动化和不平等。");
}

const model = readModel();
if (model) {
  for (const target of document.querySelectorAll("[data-lev-chart='gates']")) {
    drawGateChart(target, model);
  }
  for (const target of document.querySelectorAll("[data-lev-chart='matrix']")) {
    drawRouteGateMatrix(target, model);
  }
  for (const target of document.querySelectorAll("[data-lev-chart='flywheel']")) {
    drawFlywheel(target, model);
  }
}
