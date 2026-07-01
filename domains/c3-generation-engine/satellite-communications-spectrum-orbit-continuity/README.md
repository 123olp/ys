# Satellite Communications Spectrum Orbit Continuity

`satellite-communications-spectrum-orbit-continuity/` 研究卫星通信、频谱、轨道资源、地面站、空间天气、星座拥塞、服务覆盖和监管如何支撑偏远地区、灾害场景、移动通信和全球连接连续性。

> 核心问题：地面网络不是所有地方、所有灾害、所有移动场景都可靠。卫星通信为主体提供第二连接层，但它依赖频谱、轨道、地面站和空间环境治理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要在偏远、移动、灾害和地面网络中断场景保持通信和数据可达
  -> 卫星通信提供覆盖、回传、定位和应急连接的候选路径
  -> 频谱冲突、轨道拥塞、地面站失效和空间天气会降低可用性
  -> 因此卫星通信频谱轨道是连接连续性的空间层约束域
```

## 关注对象

- Satellite broadband、GNSS augmentation、direct-to-device、ground station、spectrum allocation、orbital debris、space weather、coverage、latency 和 regulatory coordination。
- 灾害通信、偏远医疗、海空移动、科研站点、物联网、农业、航运、应急服务和边缘数据回传。
- 与 `geospatial-navigation-location-infrastructure/` 的边界：定位域关注 PNT；本域关注通信和频谱轨道资源。
- 与 `telecommunications-network-resilience-continuity/` 的关系：电信韧性域是总域；本域专门拆出卫星层。

## Human Infra 模型链路

```text
卫星通信频谱轨道 T
  -> 改变覆盖、延迟、带宽、频谱可用性、轨道安全和地面站冗余变量 X
  -> 改变灾害通信、偏远服务、移动连接和边缘数据回传状态 S
  -> 改变通信中断、地理排斥、应急协调失败和服务退化风险 λ(t)
  -> 影响主体在地面网络不足时的求助、协作、导航和数字服务可达性
```

## 非目标

- 不提供卫星攻击、干扰、规避频谱监管、地面站入侵、轨道操作或军事用途建议。
- 不把卫星网络写成地面网络的万能替代。
- 不替代空间天气、定位导航、电信韧性或网络安全域。

## Source Signals

- FCC Space Bureau: https://www.fcc.gov/space
- ITU Radiocommunication Space Services: https://www.itu.int/en/ITU-R/space/Pages/default.aspx
- NTIA National Spectrum Strategy: https://www.ntia.gov/issues/national-spectrum-strategy
- NOAA Space Weather Prediction Center: https://www.swpc.noaa.gov/

## 下一步

- 建立 Satellite Connectivity Card：service type, coverage, latency, spectrum dependency, ground segment, orbital risk, space weather exposure, emergency role。
