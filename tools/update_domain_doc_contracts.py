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
README_RESEARCH_START = "<!-- domain-research-skeleton:start -->"
README_RESEARCH_END = "<!-- domain-research-skeleton:end -->"
AGENTS_START = "<!-- domain-agent-contract:start -->"
AGENTS_END = "<!-- domain-agent-contract:end -->"
AGENTS_WORKFLOW_START = "<!-- domain-agent-workflow:start -->"
AGENTS_WORKFLOW_END = "<!-- domain-agent-workflow:end -->"

TIER_QUESTIONS = {
    "C1": "这个域如何直接改写主体持续性边界，例如寿命、死亡、时间差分、身份连续性或未来抵达能力？",
    "C2": "这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？",
    "C3": "这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？",
    "C4": "这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？",
    "C5": "这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？",
    "C6": "这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？",
}

TIER_CHECKLISTS = {
    "C1": [
        "界定本域直接改写的主体持续性边界：寿命、死亡、身份连续性、时间差分或未来抵达能力。",
        "说明主体连续性条件：身体、记忆、人格、行动能力或法律身份中哪些必须保持。",
        "列出不可越过的中止门槛：退出失败、连续性失败、尾部风险、不可逆损伤或治理失效。",
        "说明它如何改变有效寿命、有效时间、未来选择权或可能性空间。",
        "明确本域不能被宣传成现实永生、工程可行性或个体行动方案。",
    ],
    "C2": [
        "界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。",
        "说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。",
        "列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。",
        "记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。",
        "区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。",
    ],
    "C3": [
        "界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。",
        "说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。",
        "识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。",
        "记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。",
        "列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。",
    ],
    "C4": [
        "界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。",
        "说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。",
        "记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。",
        "识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。",
        "列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。",
    ],
    "C5": [
        "界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。",
        "说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。",
        "记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。",
        "识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。",
        "建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。",
    ],
    "C6": [
        "界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。",
        "说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。",
        "记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。",
        "明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。",
        "避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。",
    ],
}


def md_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def checklist_text(tier: str) -> str:
    return "\n".join(f"- {item}" for item in TIER_CHECKLISTS[tier])


def remove_generated_block(text: str, start: str, end: str) -> str:
    pattern = re.compile(r"\n*" + re.escape(start) + r".*?" + re.escape(end) + r"\n*", re.DOTALL)
    return pattern.sub("\n\n", text)


def insert_after_title(text: str, block: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        new_lines = lines[:1] + ["", block, ""] + lines[1:]
    else:
        new_lines = [block, ""] + lines
    return re.sub(r"\n{3,}", "\n\n", "\n".join(new_lines)).rstrip() + "\n"


def replace_generated_blocks(text: str, blocks: list[tuple[str, str, str]]) -> str:
    stripped = text
    for start, end, _block in blocks:
        stripped = remove_generated_block(stripped, start, end)
    return insert_after_title(stripped.strip(), "\n\n".join(block for _start, _end, block in blocks))


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


def research_skeleton_block(row: dict[str, str]) -> str:
    checklist = checklist_text(row["tier"])
    return f"""<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

{checklist}

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->"""


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


def agent_workflow_block(row: dict[str, str]) -> str:
    return f"""<!-- domain-agent-workflow:start -->
## 代理执行流程

1. 先读本目录 `README.md`，确认研究对象、分级理由、Human Infra 追问和使用边界。
2. 再读父级层目录的 `README.md` 与 `AGENTS.md`，确认 `{md_cell(row["tier"])}` 层的根本性标尺和同层相邻域。
3. 需要移动、拆分、合并或重命名本域时，先更新 `domains/_possibility-space-control/classification.tsv`，再运行 `python3 tools/update_domain_doc_contracts.py`。
4. 新增资料时先落到 Source Signals 或 Source Cards；只有完成证据边界复核后，才沉淀为稳定叙述。
5. 输出结论时必须同时写清：它影响什么变量、通过什么机制、证据等级是什么、不能推出什么。

## 补齐优先级

- P1 Source trail：补来源、日期、版本、作者、原始链接和本地路径。
- P2 Variable map：补输入变量、中间机制、状态变量、风险变量和输出指标。
- P3 Claim-Evidence Matrix：补主张、证据、适用范围、不确定性、反例和禁用外推。
- P4 Relation links：补上游依赖、下游输出、同层相邻域和可能的迁移路径。
- P5 Reader path：补新手入口、术语、最小阅读顺序和下一步研究任务。

## 验证要求

- 批量更新域文档后，必须运行 `python3 tools/update_domain_doc_contracts.py` 并确认第二次运行更新数为 0。
- 结构或链接变化后，必须运行 `make check`。
- 提交前必须运行 `git diff --check`，避免 Markdown 空白和格式错误。
- 不得把 `web/`、临时下载、个人资料或未核验论文缓存混入域文档提交。
<!-- domain-agent-workflow:end -->"""


def update_file(path: Path, blocks: list[tuple[str, str, str]]) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = replace_generated_blocks(original, blocks)
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
        if update_file(
            readme,
            [
                (README_START, README_END, readme_block(row)),
                (README_RESEARCH_START, README_RESEARCH_END, research_skeleton_block(row)),
            ],
        ):
            readme_updates += 1
        if update_file(
            agents,
            [
                (AGENTS_START, AGENTS_END, agents_block(row)),
                (AGENTS_WORKFLOW_START, AGENTS_WORKFLOW_END, agent_workflow_block(row)),
            ],
        ):
            agents_updates += 1

    print(f"updated README.md files: {readme_updates}")
    print(f"updated AGENTS.md files: {agents_updates}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
