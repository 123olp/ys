#!/usr/bin/env python3
"""
湿件工程模拟器 (Wetware Engineering Simulator)
================================================
将生物体视为可组合的功能模块系统

核心模块：
- 供能模块 (Power Module)
- 代谢循环模块 (Metabolism Module)  
- 计算决策模块 (Compute Module)

运行: python wetware_sim.py
"""

import time
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable
from enum import Enum
from abc import ABC, abstractmethod


# ============================================================
# 第一层：标准接口定义 (Bio-Interface)
# ============================================================

class InterfaceType(Enum):
    """接口类型 - 类似 USB/PCIe 的标准化"""
    POWER = "power"           # 能量传输
    SIGNAL = "signal"         # 信号传输
    METABOLITE = "metabolite" # 代谢物传输
    MECHANICAL = "mechanical" # 机械连接


@dataclass
class Port:
    """标准端口 - 组件的输入/输出接口"""
    name: str
    interface_type: InterfaceType
    direction: str  # "in" | "out"
    value: float = 0.0
    
    def compatible_with(self, other: 'Port') -> bool:
        """检查接口兼容性"""
        return (self.interface_type == other.interface_type and 
                self.direction != other.direction)


@dataclass 
class Connection:
    """组件间连接"""
    source_component: str
    source_port: str
    target_component: str
    target_port: str


# ============================================================
# 第二层：生物组件基类 (Bio-Component)
# ============================================================

class BioComponent(ABC):
    """生物组件基类 - 所有功能模块的父类"""
    
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.ports: Dict[str, Port] = {}
        self.state: Dict[str, float] = {}
        self.active = True
        self._setup_ports()
        self._init_state()
    
    @abstractmethod
    def _setup_ports(self):
        """定义组件的输入/输出端口"""
        pass
    
    @abstractmethod
    def _init_state(self):
        """初始化内部状态"""
        pass
    
    @abstractmethod
    def tick(self, dt: float):
        """执行一个时间步的计算"""
        pass
    
    def get_port(self, name: str) -> Optional[Port]:
        return self.ports.get(name)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}@{self.version})"


# ============================================================
# 第三层：三大核心功能模块实现
# ============================================================

class PowerModule(BioComponent):
    """
    供能模块 - 能量输入、转化、供应
    模拟：线粒体 / 人工ATP合成器 / 生物燃料电池
    """
    
    def _setup_ports(self):
        self.ports = {
            "glucose_in": Port("glucose_in", InterfaceType.METABOLITE, "in"),
            "oxygen_in": Port("oxygen_in", InterfaceType.METABOLITE, "in"),
            "atp_out": Port("atp_out", InterfaceType.POWER, "out"),
            "heat_out": Port("heat_out", InterfaceType.POWER, "out"),
            "co2_out": Port("co2_out", InterfaceType.METABOLITE, "out"),
        }
    
    def _init_state(self):
        self.state = {
            "efficiency": 0.4,      # ATP转化效率
            "atp_reserve": 100.0,   # ATP储备
            "temperature": 37.0,    # 温度
        }
    
    def tick(self, dt: float):
        if not self.active:
            return
            
        # 读取输入
        glucose = self.ports["glucose_in"].value
        oxygen = self.ports["oxygen_in"].value
        
        # 计算ATP产出 (简化的代谢方程)
        # C6H12O6 + 6O2 → 6CO2 + 6H2O + 38ATP
        reaction_rate = min(glucose, oxygen / 6) * self.state["efficiency"]
        atp_produced = reaction_rate * 38 * dt
        co2_produced = reaction_rate * 6 * dt
        heat_produced = reaction_rate * (1 - self.state["efficiency"]) * dt
        
        # 更新状态
        self.state["atp_reserve"] += atp_produced
        self.state["temperature"] += heat_produced * 0.1
        
        # 设置输出
        self.ports["atp_out"].value = min(self.state["atp_reserve"], 50.0)  # 限流
        self.ports["co2_out"].value = co2_produced
        self.ports["heat_out"].value = heat_produced
        
        # 消耗储备
        self.state["atp_reserve"] -= self.ports["atp_out"].value * dt


class MetabolismModule(BioComponent):
    """
    代谢循环模块 - 废物处理、资源回收、内环境稳态
    模拟：肝脏 + 肾脏 + 淋巴系统
    """
    
    def _setup_ports(self):
        self.ports = {
            "waste_in": Port("waste_in", InterfaceType.METABOLITE, "in"),
            "co2_in": Port("co2_in", InterfaceType.METABOLITE, "in"),
            "atp_in": Port("atp_in", InterfaceType.POWER, "in"),
            "recycled_out": Port("recycled_out", InterfaceType.METABOLITE, "out"),
            "status_out": Port("status_out", InterfaceType.SIGNAL, "out"),
        }
    
    def _init_state(self):
        self.state = {
            "toxin_level": 0.0,     # 毒素水平
            "ph_level": 7.4,        # pH值
            "filter_capacity": 1.0, # 过滤能力
        }
    
    def tick(self, dt: float):
        if not self.active:
            return
            
        waste = self.ports["waste_in"].value
        co2 = self.ports["co2_in"].value
        atp = self.ports["atp_in"].value
        
        # 需要ATP来驱动代谢
        if atp < 5:
            self.state["filter_capacity"] *= 0.9  # 能量不足，能力下降
        else:
            self.state["filter_capacity"] = min(1.0, self.state["filter_capacity"] + 0.1 * dt)
        
        # 处理废物
        processed = (waste + co2) * self.state["filter_capacity"] * dt
        self.state["toxin_level"] += (waste - processed) * 0.1
        self.state["toxin_level"] = max(0, self.state["toxin_level"] - 0.05 * dt)
        
        # pH调节 (CO2影响酸碱平衡)
        self.state["ph_level"] -= co2 * 0.01 * dt
        self.state["ph_level"] += (7.4 - self.state["ph_level"]) * 0.1 * dt
        
        # 输出
        self.ports["recycled_out"].value = processed * 0.3  # 30%可回收
        # 健康状态信号 (0-1)
        health = 1.0 - self.state["toxin_level"] / 10.0
        health *= 1.0 - abs(self.state["ph_level"] - 7.4) * 2
        self.ports["status_out"].value = max(0, min(1, health))


class ComputeModule(BioComponent):
    """
    计算决策模块 - 信息处理、感知、控制
    模拟：神经网络 / 类器官 / 生物计算机
    """
    
    def _setup_ports(self):
        self.ports = {
            "sensor_in": Port("sensor_in", InterfaceType.SIGNAL, "in"),
            "status_in": Port("status_in", InterfaceType.SIGNAL, "in"),
            "atp_in": Port("atp_in", InterfaceType.POWER, "in"),
            "control_out": Port("control_out", InterfaceType.SIGNAL, "out"),
            "decision_out": Port("decision_out", InterfaceType.SIGNAL, "out"),
        }
    
    def _init_state(self):
        self.state = {
            "processing_power": 1.0,  # 计算能力
            "memory": [],             # 短期记忆
            "threshold": 0.5,         # 决策阈值
        }
    
    def tick(self, dt: float):
        if not self.active:
            return
            
        sensor = self.ports["sensor_in"].value
        status = self.ports["status_in"].value
        atp = self.ports["atp_in"].value
        
        # 计算能力依赖能量
        self.state["processing_power"] = min(1.0, atp / 20.0)
        
        # 简单决策逻辑
        # 记忆最近的状态
        self.state["memory"].append(status)
        if len(self.state["memory"]) > 10:
            self.state["memory"].pop(0)
        
        # 计算趋势
        if len(self.state["memory"]) >= 2:
            trend = self.state["memory"][-1] - self.state["memory"][0]
        else:
            trend = 0
        
        # 决策输出
        # 如果状态下降，增加控制信号
        if status < self.state["threshold"] or trend < -0.1:
            control = (self.state["threshold"] - status) * self.state["processing_power"]
        else:
            control = 0.1  # 维持信号
        
        self.ports["control_out"].value = max(0, min(1, control))
        self.ports["decision_out"].value = 1.0 if control > 0.3 else 0.0


# ============================================================
# 第四层：Bio-Runtime 运行时系统
# ============================================================

class BioRuntime:
    """
    生物运行时 - 组件编排、资源调度、状态监控
    类似 Kubernetes 对容器的管理
    """
    
    def __init__(self):
        self.components: Dict[str, BioComponent] = {}
        self.connections: List[Connection] = []
        self.time = 0.0
        self.history: List[Dict] = []
    
    def register(self, component: BioComponent):
        """注册组件"""
        self.components[component.name] = component
        print(f"[Registry] 注册组件: {component}")
    
    def connect(self, src_comp: str, src_port: str, tgt_comp: str, tgt_port: str):
        """连接组件端口"""
        src = self.components.get(src_comp)
        tgt = self.components.get(tgt_comp)
        
        if not src or not tgt:
            raise ValueError(f"组件不存在: {src_comp} 或 {tgt_comp}")
        
        src_p = src.get_port(src_port)
        tgt_p = tgt.get_port(tgt_port)
        
        if not src_p or not tgt_p:
            raise ValueError(f"端口不存在")
        
        if not src_p.compatible_with(tgt_p):
            raise ValueError(f"接口不兼容: {src_p.interface_type} vs {tgt_p.interface_type}")
        
        self.connections.append(Connection(src_comp, src_port, tgt_comp, tgt_port))
        print(f"[Connect] {src_comp}.{src_port} -> {tgt_comp}.{tgt_port}")
    
    def _propagate_signals(self):
        """传播信号 - 将输出端口的值传递到连接的输入端口"""
        for conn in self.connections:
            src = self.components[conn.source_component]
            tgt = self.components[conn.target_component]
            value = src.ports[conn.source_port].value
            tgt.ports[conn.target_port].value = value
    
    def tick(self, dt: float = 0.1):
        """执行一个时间步"""
        # 1. 传播信号
        self._propagate_signals()
        
        # 2. 各组件计算
        for comp in self.components.values():
            comp.tick(dt)
        
        # 3. 记录状态
        self.time += dt
        self._record_state()
    
    def _record_state(self):
        """记录系统状态用于监控"""
        snapshot = {"time": self.time}
        for name, comp in self.components.items():
            snapshot[name] = {
                "state": comp.state.copy(),
                "outputs": {p: port.value for p, port in comp.ports.items() if port.direction == "out"}
            }
        self.history.append(snapshot)
    
    def run(self, duration: float, dt: float = 0.1, realtime: bool = False):
        """运行模拟"""
        steps = int(duration / dt)
        print(f"\n[Runtime] 开始模拟: {duration}s, {steps}步")
        print("=" * 60)
        
        for i in range(steps):
            self.tick(dt)
            
            if i % 10 == 0:  # 每10步输出一次
                self._print_status()
            
            if realtime:
                time.sleep(dt)
        
        print("=" * 60)
        print(f"[Runtime] 模拟完成: {self.time:.1f}s")
    
    def _print_status(self):
        """打印当前状态"""
        print(f"\n[T={self.time:.1f}s]")
        for name, comp in self.components.items():
            key_state = [(k, v) for k, v in list(comp.state.items())[:3] if isinstance(v, (int, float))]
            state_str = ", ".join(f"{k}={v:.2f}" for k, v in key_state)
            print(f"  {name}: {state_str}")


# ============================================================
# 第五层：Bio-DSL 解析器 (简化版)
# ============================================================

def parse_biodsl(code: str, runtime: BioRuntime):
    """
    简化的 Bio-DSL 解析器
    
    语法:
        COMPONENT <name> FROM <type>
        CONNECT <comp>.<port> TO <comp>.<port>
        SET <comp>.<port> = <value>
    """
    component_types = {
        "power": PowerModule,
        "metabolism": MetabolismModule,
        "compute": ComputeModule,
    }
    
    for line in code.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        
        tokens = line.split()
        
        if tokens[0] == "COMPONENT":
            # COMPONENT power1 FROM power
            name = tokens[1]
            comp_type = tokens[3].lower()
            if comp_type in component_types:
                runtime.register(component_types[comp_type](name))
        
        elif tokens[0] == "CONNECT":
            # CONNECT power1.atp_out TO compute1.atp_in
            src = tokens[1].split(".")
            tgt = tokens[3].split(".")
            runtime.connect(src[0], src[1], tgt[0], tgt[1])
        
        elif tokens[0] == "SET":
            # SET power1.glucose_in = 10
            target = tokens[1].split(".")
            value = float(tokens[3])
            comp = runtime.components.get(target[0])
            if comp and target[1] in comp.ports:
                comp.ports[target[1]].value = value


# ============================================================
# 主程序：演示完整的湿件工程系统
# ============================================================

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║           湿件工程模拟器 (Wetware Engineering Simulator)       ║
║                                                              ║
║   供能模块 ←→ 代谢模块 ←→ 计算模块                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # 方式1：编程式创建
    print("\n[方式1] 编程式创建系统")
    print("-" * 40)
    
    runtime = BioRuntime()
    
    # 创建三大模块
    power = PowerModule("power1")
    metabolism = MetabolismModule("metabolism1")
    compute = ComputeModule("compute1")
    
    # 注册到运行时
    runtime.register(power)
    runtime.register(metabolism)
    runtime.register(compute)
    
    # 建立连接 (标准接口)
    runtime.connect("power1", "atp_out", "metabolism1", "atp_in")
    runtime.connect("power1", "atp_out", "compute1", "atp_in")
    runtime.connect("power1", "co2_out", "metabolism1", "co2_in")
    runtime.connect("metabolism1", "status_out", "compute1", "status_in")
    
    # 设置外部输入 (模拟营养供给)
    power.ports["glucose_in"].value = 10.0
    power.ports["oxygen_in"].value = 60.0
    
    # 运行模拟
    runtime.run(duration=5.0, dt=0.1)
    
    # 方式2：Bio-DSL 声明式创建
    print("\n\n[方式2] Bio-DSL 声明式创建")
    print("-" * 40)
    
    dsl_code = """
    // 湿件系统定义
    COMPONENT power2 FROM power
    COMPONENT meta2 FROM metabolism
    COMPONENT brain2 FROM compute
    
    // 连接组件
    CONNECT power2.atp_out TO meta2.atp_in
    CONNECT power2.atp_out TO brain2.atp_in
    CONNECT power2.co2_out TO meta2.co2_in
    CONNECT meta2.status_out TO brain2.status_in
    
    // 设置输入
    SET power2.glucose_in = 15
    SET power2.oxygen_in = 90
    """
    
    runtime2 = BioRuntime()
    parse_biodsl(dsl_code, runtime2)
    runtime2.run(duration=3.0, dt=0.1)
    
    # 输出系统拓扑
    print("\n\n[系统拓扑]")
    print("-" * 40)
    print("""
    ┌─────────────┐     ATP      ┌──────────────┐
    │             │─────────────→│              │
    │  供能模块    │              │  代谢模块     │
    │  (Power)    │─────────────→│ (Metabolism) │
    │             │     CO2      │              │
    └─────────────┘              └──────────────┘
          │                            │
          │ ATP                        │ Status
          ↓                            ↓
    ┌─────────────────────────────────────────┐
    │              计算决策模块                 │
    │              (Compute)                  │
    └─────────────────────────────────────────┘
    """)


if __name__ == "__main__":
    main()
