# Scientific Instrumentation Sensor Calibration Maintenance

`scientific-instrumentation-sensor-calibration-maintenance/` 研究科研仪器、传感器、校准、维护、漂移、测量不确定性、参考材料和设备生命周期，如何影响 Human Infra 的测量、实验和模型输入。

> 核心问题：主体持续性研究依赖可穿戴、实验仪器、影像设备、传感器、测序平台和环境监测。若仪器漂移、校准失效或维护缺失，模型会把设备误差当成生命路径信号。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要把身体、环境、技术和风险状态转化为可靠测量
  -> 可靠测量依赖仪器校准、维护、参考标准、漂移监测和不确定性声明
  -> 仪器失准和传感器漂移会把反馈系统变成误判系统
  -> 因此科研仪器与传感器校准维护是测量反馈的硬件可信域
```

## 关注对象

- 科研仪器、传感器、可穿戴设备、实验平台、测序/影像/质谱设备和环境监测设备。
- 校准、维护、漂移、参考材料、测量不确定性、互校、设备生命周期和质量控制。
- 仪器误差如何影响生物标志物、组学、连续监测、环境暴露、模型校准和图表解释。
- 与 `standards-metrology-quality-infrastructure/` 的边界：标准计量域关注社会技术底座；本域关注具体科研仪器和传感器运行可靠性。
- 与 `wearables-continuous-sensing-personal-informatics/` 的边界：可穿戴域关注个人连续观测和反馈；本域关注传感器校准、漂移和测量质量。

## Human Infra 模型链路

```text
科研仪器与传感器校准维护 T
  -> 改变设备校准、漂移、维护、参考标准、测量不确定性和质量控制变量 X
  -> 改变实验数据、连续监测数据和环境观测数据的可信状态 S
  -> 改变假信号、漏检、不可比结果和模型误校准风险 λ(t)
  -> 影响反馈准确性、证据复现性、技术采用判断和主体持续性模型安全性
```

## 非目标

- 不提供规避校准、伪造检测、篡改设备、绕过监管或医疗器械改装策略。
- 不把仪器读数写成个人诊断、治疗建议或寿命预测。
- 不替代实验室认证、医疗器械监管、工程安全或计量机构服务。

## Source Signals

- NIST Calibration Services: https://www.nist.gov/calibrations
- NIST Metrology: https://www.nist.gov/metrology
- NIST Standard Reference Materials: https://www.nist.gov/srm
- ISO/IEC 17025: https://www.iso.org/standard/66912.html
- BIPM: https://www.bipm.org/

## 下一步

- 建立仪器可信变量表：校准日期、参考材料、漂移、维护记录、检测范围、不确定性和设备版本。
- 与 `measurement-feedback/`、`clinical-laboratory-diagnostic-quality/`、`wearables-continuous-sensing-personal-informatics/` 和 `uncertainty-quantification-model-calibration/` 建立接口。
