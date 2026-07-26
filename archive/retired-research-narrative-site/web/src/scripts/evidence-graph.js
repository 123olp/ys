import * as d3 from "d3";

const palette = {
  ink: "#1f2933",
  muted: "#59636f",
  faint: "#7f8a99",
  panel: "#ffffff",
  soft: "#f6f8fb",
  line: "#c8d1dc",
  high: "#1f7a5a",
  medium: "#2f5f8f",
  low: "#8a6a22",
  risk: "#9b3a32",
  method: "#5a4f8f"
};

const variableLabels = {
  T: ["主体持续时间", "存在窗口"],
  E: ["有效时间", "可行动时间"],
  R: ["学习轮次", "试错复盘"],
  C: ["积累资本", "能力资源网络"],
  A: ["技术采用", "接触整合"],
  Q: ["行动质量", "创造密度"],
  O: ["可能性空间", "未来选择权"]
};

function readEvidenceData() {
  const element = document.getElementById("effective-immortality-evidence-data");
  if (!element?.textContent) return null;
  try {
    return JSON.parse(element.textContent);
  } catch (error) {
    console.warn("Evidence graph data parse failed.", error);
    return null;
  }
}

function edgeColor(row) {
  if (row.edge.includes("risk")) return palette.risk;
  if (row.edge.includes("causal")) return palette.method;
  if (row.confidence.includes("High")) return palette.high;
  if (row.confidence.includes("Low")) return palette.low;
  return palette.medium;
}

function tooltipText(row) {
  return [
    row.edge,
    `问题：${row.question}`,
    `证据入口：${row.sources.join("；")}`,
    `置信：${row.confidence}`,
    `断点：${row.breakpoint}`,
    `模型任务：${row.modelTask}`
  ].join("\n");
}

function appendArrow(defs, id, color) {
  defs.append("marker")
    .attr("id", id)
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 10)
    .attr("refY", 0)
    .attr("markerWidth", 7)
    .attr("markerHeight", 7)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M0,-4L10,0L0,4")
    .attr("fill", color);
}

function drawNode(svg, node, index) {
  const group = svg.append("g")
    .attr("class", "evidence-node")
    .attr("transform", `translate(${node.x},${node.y})`);

  group.append("rect")
    .attr("x", -54)
    .attr("y", -38)
    .attr("width", 108)
    .attr("height", 76)
    .attr("rx", 4)
    .attr("fill", palette.panel)
    .attr("stroke", palette.line)
    .attr("stroke-width", 1.3);

  group.append("text")
    .attr("y", -12)
    .attr("fill", palette.ink)
    .attr("font-size", 19)
    .attr("font-weight", 850)
    .attr("text-anchor", "middle")
    .text(node.id);

  group.append("text")
    .attr("y", 10)
    .attr("fill", palette.ink)
    .attr("font-size", 13)
    .attr("font-weight", 780)
    .attr("text-anchor", "middle")
    .text(node.label[0]);

  group.append("text")
    .attr("y", 29)
    .attr("fill", palette.faint)
    .attr("font-size", 11.5)
    .attr("font-weight", 650)
    .attr("text-anchor", "middle")
    .text(node.label[1]);

  group.append("title").text(`${node.id}：${node.label.join(" / ")}，链路位置 ${index + 1}`);
}

function drawMainEdge(svg, markerId, row, from, to) {
  const color = edgeColor(row);
  const y = from.y;
  svg.append("line")
    .attr("class", "evidence-edge evidence-edge-main")
    .attr("x1", from.x + 56)
    .attr("y1", y)
    .attr("x2", to.x - 62)
    .attr("y2", y)
    .attr("stroke", color)
    .attr("stroke-width", row.confidence.includes("High") ? 2.5 : 2)
    .attr("marker-end", `url(#${markerId})`)
    .append("title")
    .text(tooltipText(row));

  svg.append("text")
    .attr("x", (from.x + to.x) / 2)
    .attr("y", y - 32)
    .attr("fill", color)
    .attr("font-size", 11)
    .attr("font-weight", 760)
    .attr("text-anchor", "middle")
    .text(row.edge);

  svg.append("text")
    .attr("x", (from.x + to.x) / 2)
    .attr("y", y + 43)
    .attr("fill", palette.faint)
    .attr("font-size", 10.5)
    .attr("font-weight", 650)
    .attr("text-anchor", "middle")
    .text(row.confidence);
}

function drawFeedbackEdge(svg, markerId, row, from, to) {
  const color = edgeColor(row);
  const path = `M${from.x + 52},${from.y - 38} C${from.x + 70},48 ${to.x - 70},48 ${to.x},${to.y - 40}`;
  svg.append("path")
    .attr("class", "evidence-edge evidence-edge-feedback")
    .attr("d", path)
    .attr("fill", "none")
    .attr("stroke", color)
    .attr("stroke-width", 2.2)
    .attr("marker-end", `url(#${markerId})`)
    .append("title")
    .text(tooltipText(row));

  svg.append("text")
    .attr("x", 560)
    .attr("y", 51)
    .attr("fill", color)
    .attr("font-size", 12)
    .attr("font-weight", 800)
    .attr("text-anchor", "middle")
    .text("O -> T/E：资源、恢复、照护和技术窗口反哺主体持续性");
}

function drawGate(svg, markerId, row, sourceNodes, gate) {
  const color = edgeColor(row);
  sourceNodes.forEach((source) => {
    svg.append("path")
      .attr("class", "evidence-edge evidence-edge-gate")
      .attr("d", `M${source.x},${source.y + 40} C${source.x},${source.y + 95} ${gate.x},${gate.y - 58} ${gate.x},${gate.y - 35}`)
      .attr("fill", "none")
      .attr("stroke", color)
      .attr("stroke-width", 1.8)
      .attr("stroke-dasharray", "5 4")
      .attr("marker-end", `url(#${markerId})`)
      .append("title")
      .text(tooltipText(row));
  });

  const group = svg.append("g")
    .attr("transform", `translate(${gate.x},${gate.y})`);

  group.append("rect")
    .attr("x", -112)
    .attr("y", -34)
    .attr("width", 224)
    .attr("height", 68)
    .attr("rx", 4)
    .attr("fill", palette.panel)
    .attr("stroke", color)
    .attr("stroke-width", 1.5);

  group.append("text")
    .attr("y", -8)
    .attr("fill", color)
    .attr("font-size", 13)
    .attr("font-weight", 850)
    .attr("text-anchor", "middle")
    .text(gate.title);

  group.append("text")
    .attr("y", 15)
    .attr("fill", palette.muted)
    .attr("font-size", 11.5)
    .attr("font-weight", 650)
    .attr("text-anchor", "middle")
    .text(gate.note);

  group.append("title").text(tooltipText(row));
}

function drawLegend(svg) {
  const items = [
    ["中等证据", palette.medium],
    ["中高证据", palette.high],
    ["低置信边", palette.low],
    ["风险通道", palette.risk],
    ["方法门禁", palette.method]
  ];
  const startX = 92;
  const y = 492;

  svg.append("text")
    .attr("x", startX)
    .attr("y", y)
    .attr("fill", palette.muted)
    .attr("font-size", 12)
    .attr("font-weight", 800)
    .text("图例");

  items.forEach(([label, color], index) => {
    const x = startX + 54 + index * 142;
    svg.append("line")
      .attr("x1", x)
      .attr("y1", y - 4)
      .attr("x2", x + 28)
      .attr("y2", y - 4)
      .attr("stroke", color)
      .attr("stroke-width", 3);
    svg.append("text")
      .attr("x", x + 36)
      .attr("y", y)
      .attr("fill", palette.muted)
      .attr("font-size", 11.5)
      .attr("font-weight", 680)
      .text(label);
  });
}

function drawEvidenceGraph(target, data) {
  target.textContent = "";

  const width = 1120;
  const height = 520;
  const markerBase = `evidence-arrow-${Date.now().toString(36)}`;
  const nodeY = 176;
  const nodes = data.variables.map((id, index) => ({
    id,
    label: variableLabels[id] ?? [id, ""],
    x: 92 + index * 156,
    y: nodeY
  }));
  const nodeMap = new Map(nodes.map((node) => [node.id, node]));
  const rowMap = new Map(data.evidenceEdges.map((row) => [row.edge, row]));
  const svg = d3.select(target)
    .append("svg")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("role", "img")
    .attr("aria-labelledby", "evidence-graph-title evidence-graph-desc")
    .style("max-width", "100%")
    .style("height", "auto");

  svg.append("title")
    .attr("id", "evidence-graph-title")
    .text("有效永生飞轮 Evidence Matrix 证据链图");

  svg.append("desc")
    .attr("id", "evidence-graph-desc")
    .text("图中展示 T/E/R/C/A/Q/O 七变量主链、可能性空间反哺、技术风险通道和因果主张门禁。");

  svg.append("rect")
    .attr("width", width)
    .attr("height", height)
    .attr("rx", 4)
    .attr("fill", palette.soft);

  svg.append("text")
    .attr("x", 48)
    .attr("y", 36)
    .attr("fill", palette.ink)
    .attr("font-size", 19)
    .attr("font-weight", 880)
    .text("Evidence Matrix：从主体持续时间到可能性空间");

  svg.append("text")
    .attr("x", width - 48)
    .attr("y", 36)
    .attr("fill", palette.muted)
    .attr("font-size", 12)
    .attr("font-weight", 760)
    .attr("text-anchor", "end")
    .text(`schema ${data.schemaVersion} / ${data.updated}`);

  const defs = svg.append("defs");
  appendArrow(defs, `${markerBase}-medium`, palette.medium);
  appendArrow(defs, `${markerBase}-high`, palette.high);
  appendArrow(defs, `${markerBase}-low`, palette.low);
  appendArrow(defs, `${markerBase}-risk`, palette.risk);
  appendArrow(defs, `${markerBase}-method`, palette.method);

  const markerFor = (row) => {
    if (row.edge.includes("risk")) return `${markerBase}-risk`;
    if (row.edge.includes("causal")) return `${markerBase}-method`;
    if (row.confidence.includes("High")) return `${markerBase}-high`;
    if (row.confidence.includes("Low")) return `${markerBase}-low`;
    return `${markerBase}-medium`;
  };

  nodes.forEach((node, index) => drawNode(svg, node, index));

  ["T -> E", "E -> R", "R -> C", "C -> A", "A -> Q", "Q -> O"].forEach((edge) => {
    const [fromId, toId] = edge.split(" -> ");
    const row = rowMap.get(edge);
    if (row) drawMainEdge(svg, markerFor(row), row, nodeMap.get(fromId), nodeMap.get(toId));
  });

  const feedback = rowMap.get("O -> T/E");
  if (feedback) {
    drawFeedbackEdge(svg, markerFor(feedback), feedback, nodeMap.get("O"), nodeMap.get("T"));
  }

  const riskGate = rowMap.get("A/Q -> risk");
  if (riskGate) {
    drawGate(svg, markerFor(riskGate), riskGate, [nodeMap.get("A"), nodeMap.get("Q")], {
      x: 780,
      y: 322,
      title: "副作用与尾部风险",
      note: "误用、依赖、监控、QA 成本"
    });
  }

  const methodGate = rowMap.get("U_t -> causal claim");
  if (methodGate) {
    drawGate(svg, markerFor(methodGate), methodGate, [nodeMap.get("A")], {
      x: 512,
      y: 410,
      title: "因果主张门禁",
      note: "人群、比较组、time zero、结局"
    });
  }

  drawLegend(svg);
}

const data = readEvidenceData();
const target = document.getElementById("evidence-graph");
if (data && target) {
  drawEvidenceGraph(target, data);
}
