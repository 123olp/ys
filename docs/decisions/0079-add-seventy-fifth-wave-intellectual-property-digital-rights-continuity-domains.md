# 0079 Add Seventy-Fifth Wave Intellectual Property Digital Rights Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经有 `intellectual-property-technology-transfer-access/`，用于审查技术成熟到主体可及之间的制度转换；也有 `platform-account-suspension-appeals-continuity/` 和数字内容可信域，用于审查平台入口、来源凭据和内容裁决。

但主体持续性还需要更细的创造资产权利层：作品作者身份、版权记录、开放许可、开源许可证、商标身份、专利披露、版税元数据和 AI 训练数据权利，会决定主体的作品、代码、品牌、发明和知识资产能否继续产生声誉、收入、工具和协作机会。

这些域不是法律服务入口，而是先验追问链中的“创造资产能否持续归属、传播、复用、变现和防止被平台/模型/冒充系统吞噬”的条件层。

## Decision

Add eight research domains:

- `domains/copyright-authorship-registration-licensing-continuity/`
- `domains/dmca-notice-counter-notice-platform-removal-continuity/`
- `domains/creative-commons-open-content-license-continuity/`
- `domains/open-source-software-license-compliance-continuity/`
- `domains/trademark-brand-identity-rights-continuity/`
- `domains/patent-invention-disclosure-maintenance-continuity/`
- `domains/creator-royalty-rights-metadata-continuity/`
- `domains/ai-training-data-rights-opt-out-provenance-continuity/`

## Rationale

Human Infra 的终极目标是有效永生 / 主体持续性最大化。持续性不仅来自身体、认知、时间和环境，也来自主体持续创造和积累的资产是否能被识别、保护、传播、复用、授权和回流。

这一波把“创造资产权利连续性”拆成独立域，而不是继续塞进泛化 IP 或平台治理大桶：

- 版权处理作品作者身份、登记、许可和 AI 辅助创作边界。
- DMCA 处理网络平台上版权通知、移除、恢复和账号/收入后果。
- Creative Commons 处理开放内容复用、署名和公共知识传播。
- 开源软件许可证处理代码依赖、SPDX、OSI 和分发边界。
- 商标处理品牌身份、来源识别、混淆和冒充风险。
- 专利处理发明披露、公开、维护和技术可及性。
- 创作者版税处理权利元数据、标识符、分账和资源回流。
- AI 训练数据权利处理 dataset provenance、许可、opt-out 和模型开发披露。

## Boundaries

These domains do not provide legal advice, IP strategy, registration support, infringement analysis, takedown drafting, counter-notice drafting, fair-use evaluation, license selection, patent prosecution, trademark filing, royalty recovery, data scraping, model training, platform evasion or circumvention tactics.

They only maintain public-source research notes, mechanism chains, source signals, variable candidates, evidence boundaries and Human Infra relevance.

## Consequences

- `README.md`, `docs/`, `domains/` and `tools/check_repository.py` must include the new domains.
- Future work can build a Rights Continuity Card with fields for asset type, owner/author signal, registration or identifier, license, platform execution path, revenue/reputation dependency, AI/data-use exposure and recovery boundary.
- The existing `intellectual-property-technology-transfer-access/` remains the broad technology diffusion and access layer; these new domains handle finer-grained creative, software, brand, patent and AI-data rights continuity.
