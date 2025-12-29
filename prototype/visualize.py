#!/usr/bin/env python3
"""
湿件工程可视化模块
==================
用 matplotlib 绘制系统状态变化
"""

import matplotlib.pyplot as plt
from wetware_sim import BioRuntime, PowerModule, MetabolismModule, ComputeModule


def run_and_visualize():
    """运行模拟并可视化结果"""
    
    # 创建系统
    runtime = BioRuntime()
    
    power = PowerModule("power")
    metabolism = MetabolismModule("metabolism")
    compute = ComputeModule("compute")
    
    runtime.register(power)
    runtime.register(metabolism)
    runtime.register(compute)
    
    runtime.connect("power", "atp_out", "metabolism", "atp_in")
    runtime.connect("power", "atp_out", "compute", "atp_in")
    runtime.connect("power", "co2_out", "metabolism", "co2_in")
    runtime.connect("metabolism", "status_out", "compute", "status_in")
    
    # 设置输入
    power.ports["glucose_in"].value = 10.0
    power.ports["oxygen_in"].value = 60.0
    
    # 运行模拟
    duration = 20.0
    dt = 0.1
    steps = int(duration / dt)
    
    for _ in range(steps):
        runtime.tick(dt)
    
    # 提取数据
    times = [h["time"] for h in runtime.history]
    
    atp = [h["power"]["state"]["atp_reserve"] for h in runtime.history]
    temp = [h["power"]["state"]["temperature"] for h in runtime.history]
    ph = [h["metabolism"]["state"]["ph_level"] for h in runtime.history]
    toxin = [h["metabolism"]["state"]["toxin_level"] for h in runtime.history]
    proc_power = [h["compute"]["state"]["processing_power"] for h in runtime.history]
    
    # 绘图
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('湿件工程系统模拟 (Wetware Engineering Simulation)', fontsize=14)
    
    # ATP储备
    axes[0, 0].plot(times, atp, 'b-', linewidth=2)
    axes[0, 0].set_xlabel('时间 (s)')
    axes[0, 0].set_ylabel('ATP储备')
    axes[0, 0].set_title('供能模块 - ATP储备')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 温度
    axes[0, 1].plot(times, temp, 'r-', linewidth=2)
    axes[0, 1].axhline(y=37, color='g', linestyle='--', label='正常体温')
    axes[0, 1].set_xlabel('时间 (s)')
    axes[0, 1].set_ylabel('温度 (°C)')
    axes[0, 1].set_title('供能模块 - 温度')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # pH值
    axes[1, 0].plot(times, ph, 'g-', linewidth=2)
    axes[1, 0].axhline(y=7.4, color='b', linestyle='--', label='正常pH')
    axes[1, 0].axhline(y=7.35, color='orange', linestyle='--', label='酸中毒阈值')
    axes[1, 0].set_xlabel('时间 (s)')
    axes[1, 0].set_ylabel('pH值')
    axes[1, 0].set_title('代谢模块 - pH平衡')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # 计算能力
    axes[1, 1].plot(times, proc_power, 'm-', linewidth=2)
    axes[1, 1].set_xlabel('时间 (s)')
    axes[1, 1].set_ylabel('处理能力')
    axes[1, 1].set_title('计算模块 - 处理能力')
    axes[1, 1].set_ylim(0, 1.1)
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('simulation_result.png', dpi=150)
    print("图表已保存: simulation_result.png")
    plt.show()


if __name__ == "__main__":
    run_and_visualize()
