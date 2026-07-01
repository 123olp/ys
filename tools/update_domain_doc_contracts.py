#!/usr/bin/env python3
"""Update standard README/AGENTS contracts for every formal research domain."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION = ROOT / "domains" / "_possibility-space-control" / "classification.tsv"

README_START = "<!-- domain-standard:start -->"
README_END = "<!-- domain-standard:end -->"
AGENTS_START = "<!-- domain-agent-contract:start -->"
AGENTS_END = "<!-- domain-agent-contract:end -->"

TIER_QUESTIONS = {
    "C1": "这个域如何直接改写主体持续性边界，例如寿命、死亡、时间差分、身份连续性或未来抵达能力？",
    "C2": "这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？",
    "C3": "这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？",
    "C4": "这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？",
    "C5": "这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？",
    "C6": "这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？",
}


def md_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def replace_or_insert(text: str, start: str, end: str, block: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(block, text)

    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        new_lines = lines[:1] + ["", block, ""] + lines[1:]
    else:
        new_lines = [block, ""] + lines
    return "\n".join(new_lines).rstrip() + "\n"


def read_rows() -> list[dict[str, str]]:
    with CLASSIFICATION.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def readme_block(row: dict[str, str]) -> str:
    question = TIER_QUESTIONS[row["tier"]]
    return f"""<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `{md_cell(row["physical_path"])}` |
| 分级 | `{md_cell(row["tier"])}` - {md_cell(row["tier_name"])} |
| 控制轴 | {md_cell(row["control_axis"])} |
| 分级理由 | {md_cell(row["rationale"])} |
| 复核状态 | `{md_cell(row["review_status"])}` |

### Human Infra 追问

{question}

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->"""


def agents_block(row: dict[str, str]) -> str:
    tier_dir = str(Path(row["physical_path"]).parent)
    return f"""<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `{md_cell(row["physical_path"])}` |
| 所属层级 | `{md_cell(row["tier"])}` - {md_cell(row["tier_name"])} |
| 父级容器 | `{md_cell(tier_dir)}` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `{md_cell(row["review_status"])}` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->"""


def update_file(path: Path, block: str, start: str, end: str) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = replace_or_insert(original, start, end, block)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    readme_updates = 0
    agents_updates = 0
    for row in read_rows():
        domain_dir = ROOT / row["physical_path"]
        readme = domain_dir / "README.md"
        agents = domain_dir / "AGENTS.md"
        if not readme.is_file() or not agents.is_file():
            raise SystemExit(f"missing README.md or AGENTS.md under {domain_dir}")
        if update_file(readme, readme_block(row), README_START, README_END):
            readme_updates += 1
        if update_file(agents, agents_block(row), AGENTS_START, AGENTS_END):
            agents_updates += 1

    print(f"updated README.md files: {readme_updates}")
    print(f"updated AGENTS.md files: {agents_updates}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
