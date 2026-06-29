# biostasis-cryopreservation 目录说明

`domains/biostasis-cryopreservation/` 保存生物停滞与冷冻保存研究域。它关注如何降低损耗、保存结构并等待未来修复。

## 目录结构

```text
biostasis-cryopreservation/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责冷冻保存、生物停滞、低温医学、休眠和保存到未来路径。
- 本域与 `future-waiting/` 共享“等待未来”问题，但不共享机制。
- 本域不提供灌流、冷冻、复温、给药、保护剂或人体保存操作步骤。

## 维护规则

- 任何保存主张必须区分结构保存、功能可逆、未来修复依赖和主体连续性。
- 任何“复活”或“永生”表述必须降级为条件性假设。
- 新增文件或子目录时，同步更新本文件。
