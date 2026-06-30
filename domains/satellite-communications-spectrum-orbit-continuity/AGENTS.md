# satellite-communications-spectrum-orbit-continuity 目录说明

本目录维护卫星通信、频谱与轨道连续性资料。它关注连接基础设施的空间层和灾害/偏远场景备用路径。

## 目录结构

```text
satellite-communications-spectrum-orbit-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义卫星通信、频谱、地面站、轨道资源和空间天气如何影响主体持续性。
- 本目录不保存干扰、入侵、规避监管、轨道操作、军事用途或敏感设施资料。

## 上下游关系

- 上游来自 FCC、ITU、NTIA、NOAA 和公开卫星通信治理资料。
- 下游服务偏远医疗、灾害通信、移动连接、边缘数据回传和全球协作。
- 不替代 `geospatial-navigation-location-infrastructure/`；本目录关注通信而不是 PNT 主体。

## 维护规则

- 必须区分通信、定位、遥感、地面站和频谱治理。
- 涉及攻击、干扰或敏感空间操作的内容不得进入本目录。
