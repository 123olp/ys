# 要素10：Human Connectome Project 参与路径

**创建时间**: 2025-10-18
**目标**: 为永生工程获取全脑连接组数据
**预计周期**: 6-24个月
**难度**: ⭐⭐⭐⭐ (需要学术/研究背景)

---

## 目标定义

### 什么是Human Connectome？
```yaml
连接组学 (Connectomics):
  定义: 绘制大脑所有神经元及其连接的完整图谱
  层次:
    - 宏观: fMRI功能连接 (HCP当前水平)
    - 介观: 神经束追踪 (DTI/DWI)
    - 微观: 突触级连接 (最终目标，需电镜)

人类连接组计划 (HCP):
  启动: 2009年
  资助: NIH $40M
  目标: 1200名健康成年人的脑连接图谱
  数据量: >1 PB
  状态: Phase II (2017-2027)
```

### 为什么对永生工程至关重要？
1. **大脑备份基础**: 没有连接组，无法完整备份大脑
2. **意识神经关联**: 理解意识如何从连接模式中涌现
3. **记忆定位**: 找到记忆存储的物理位置
4. **神经写入目标**: 确定BCI写入的精确目标区域

---

## 参与方式分级

### Level 0: 数据使用者（最简单）
**适合**: 任何人，无需机构背景
**成本**: 免费
**时间**: 1周内开始
**产出**: 下载并分析HCP公开数据

### Level 1: 研究合作者（中等）
**适合**: 有学术背景或与机构合作
**成本**: $0-$5,000
**时间**: 3-6个月
**产出**: 发表论文，引用HCP数据

### Level 2: 数据贡献者（困难）
**适合**: 成为HCP扫描对象
**成本**: 免费（但需符合条件）
**时间**: 招募中可能需要等待
**产出**: 你的大脑被绘制并入数据库

### Level 3: 核心成员（最难）
**适合**: 神经科学家、成像专家
**成本**: 需要研究职位
**时间**: 多年commitment
**产出**: 主导HCP子项目

---

## Level 0: 数据使用者 完全指南

### 步骤1-20：访问HCP数据

**1. 注册ConnectomeDB账号**
```
网址: https://db.humanconnectome.org/
要求: 接受数据使用协议 (DUA)
限制: 仅用于研究，不可商业化
时间: 10分钟
```

**2. 了解数据结构**
```yaml
HCP_1200数据集:
  被试数量: 1200
  年龄范围: 22-35岁
  性别: 均衡
  扫描模态:
    - 结构MRI (T1w, T2w)
    - 静息态fMRI (rfMRI)
    - 任务态fMRI (tfMRI, 7种任务)
    - 扩散MRI (dMRI, 270方向)
    - MEG/EEG (部分被试)
  行为数据: 认知测试、问卷
  基因数据: 部分被试的SNP数据

数据量:
  单个被试: ~15 GB
  全部1200人: ~18 TB
```

**3. 选择下载方式**

**方式A: AWS S3 (推荐)**
```bash
# 安装AWS CLI
pip install awscli

# 配置
aws configure  # 使用HCP提供的credentials

# 下载单个被试数据
aws s3 sync s3://hcp-openaccess/HCP_1200/100307/ ./HCP_data/100307/

# 预计时间: 15 GB @ 100 Mbps = 20分钟
```

**方式B: Aspera (最快)**
```bash
# 安装Aspera Connect
# 从HCP网站下载

# 下载
ascp -QT -l 300m -P33001 \
  -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh \
  hcpuser@aspera.humanconnectome.org:/HCP_1200/100307/ \
  ./HCP_data/100307/
```

**方式C: Web浏览器（最慢）**
- 直接从ConnectomeDB下载
- 适合小文件

**4. 理解文件命名规则**
```
100307_3T_Structural_preproc.zip
  └─ 被试ID: 100307
  └─ 扫描仪: 3T (特斯拉)
  └─ 数据类型: Structural (结构像)
  └─ 状态: preproc (预处理后)

100307_3T_rfMRI_REST1_preproc.zip
  └─ rfMRI: 静息态功能磁共振
  └─ REST1: 第一次静息态扫描
```

**5-10. 安装分析工具**

**必需软件**:
```bash
# FSL (fMRI分析)
wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
python fslinstaller.py

# Workbench (HCP专用可视化)
# 下载: https://www.humanconnectome.org/software/connectome-workbench

# FreeSurfer (皮层重建)
wget https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/

# Python环境
conda create -n hcp python=3.10
conda activate hcp
pip install nibabel nilearn numpy scipy matplotlib
```

**11. 加载你的第一个连接组**

Python示例：
```python
import nibabel as nib
import numpy as np
from nilearn import plotting

# 加载预处理的T1结构像
t1 = nib.load('100307/T1w/T1w_acpc_dc_restore_brain.nii.gz')

# 可视化
plotting.plot_anat(t1)
plotting.show()

# 加载连接矩阵 (ROI-to-ROI)
conn_matrix = np.load('100307/rfMRI_REST1_connectivity.npy')
# conn_matrix.shape = (360, 360)  # 360个脑区 × 360个脑区

# 可视化连接矩阵
import matplotlib.pyplot as plt
plt.imshow(conn_matrix, cmap='hot', vmin=-0.5, vmax=0.5)
plt.colorbar()
plt.title('Functional Connectivity Matrix')
plt.show()
```

**12. 运行预处理流程（如果需要原始数据）**
```bash
# 使用HCP Pipeline
# 文档: https://github.com/Washington-University/HCPpipelines

# 结构像处理
./PreFreeSurfer.sh --subject=100307 --t1=T1w.nii.gz --t2=T2w.nii.gz

# 功能像处理
./fMRIVolume.sh --subject=100307 --fmriname=rfMRI_REST1

# 扩散像处理
./DiffPreprocPipeline.sh --subject=100307
```

**13-15. 提取个人关心的指标**

示例分析：
```python
# 计算全脑网络属性
import networkx as nx

# 将连接矩阵转为图
threshold = 0.3  # 只保留相关系数>0.3的连接
adj_matrix = (conn_matrix > threshold).astype(int)
G = nx.from_numpy_array(adj_matrix)

# 计算网络指标
metrics = {
    'clustering_coefficient': nx.average_clustering(G),
    'path_length': nx.average_shortest_path_length(G),
    'modularity': nx.algorithms.community.modularity(
        G, nx.algorithms.community.greedy_modularity_communities(G)
    ),
    'small_worldness': ...  # 需要随机网络对照
}

print(metrics)
```

**16-20. 应用到永生工程**
- 分析你自己的大脑扫描（如果有）与HCP对照
- 识别"关键节点"（hub regions）用于BCI植入
- 建立个人连接组基线，未来跟踪变化

---

## Level 1: 研究合作者 路径

### 步骤21-50：发表基于HCP的研究

**21. 确定研究方向**

高影响力方向：
1. **意识神经关联**: 从连接模式预测意识状态
2. **记忆engram定位**: 连接组与记忆能力关联
3. **衰老追踪**: 对比HCP-Aging数据集
4. **BCI靶点优化**: 找到信息流最密集的节点
5. **疾病预测**: 从连接模式预测神经退行性风险

**22. 文献综述**

必读论文：
- Van Essen et al. (2013) "The WU-Minn HCP Consortium"
- Glasser et al. (2016) "A multi-modal parcellation of human cerebral cortex"
- Smith et al. (2013) "Resting-state fMRI in HCP"

**23. 选择分析方法**

**方法A: 图论分析**
```python
# 使用Brain Connectivity Toolbox (BCT)
import bct

# 计算模块化
modules = bct.community_louvain(conn_matrix)

# 计算中心性
betweenness = bct.betweenness_wei(conn_matrix)
eigenvector = bct.eigenvector_centrality_und(conn_matrix)
```

**方法B: 机器学习预测**
```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# 用连接组预测行为
X = conn_matrices  # (n_subjects, 360, 360)
y = cognitive_scores  # (n_subjects,)

# 展平连接矩阵
X_flat = X.reshape(X.shape[0], -1)

# 训练模型
model = Ridge(alpha=1.0)
scores = cross_val_score(model, X_flat, y, cv=5)
print(f'Prediction R² = {scores.mean():.3f}')
```

**方法C: 动力学建模**
```python
# 使用The Virtual Brain (TVB)
from tvb.simulator.lab import *

# 加载HCP连接矩阵作为结构连接
conn = connectivity.Connectivity.from_file("HCP_connectivity.zip")

# 定义神经团模型
oscillator = models.Generic2dOscillator()

# 运行模拟
sim = simulator.Simulator(
    model=oscillator,
    connectivity=conn,
    coupling=coupling.Linear(a=0.0152),
    simulation_length=10000.0,  # ms
)
sim.configure()
(time, data), = sim.run()

# 对比模拟fMRI与真实fMRI
```

**24-30. 撰写论文**
（标准学术流程，此处省略）

**31-40. 寻找合作者**

平台：
- **ResearchGate**: 发布项目寻找合作
- **HCP邮件列表**: hcp-users@humanconnectome.org
- **Twitter/X学术圈**: #Connectomics #HCP
- **会议**: OHBM (人脑图谱组织年会)

**41-50. 建立长期研究计划**
- 每年分析HCP新释放的数据
- 跟踪HCP-Aging, HCP-Development, HCP-Disease项目
- 建立自己的"连接组数据库"整合多来源数据

---

## Level 2: 数据贡献者（成为HCP被试）

### 步骤51-70：让你的大脑被绘制

**51. 检查资格**

HCP标准入组标准（2009-2017年，已结束招募）：
```yaml
年龄: 22-35岁
健康状态: 无神经/精神疾病史
MRI兼容: 无金属植入物
居住地: 美国境内（原HCP）
语言: 英语流利
承诺: 2-3次访问，每次4-8小时
补偿: $500-$800
```

**52. 当前机会：HCP衍生项目**

**HCP-Aging** (65-100岁)
- 招募地: St. Louis, MO
- 联系: https://www.humanconnectome.org/study/hcp-lifespan-aging

**HCP-Development** (5-21岁)
- 如果你有符合年龄的家人

**HCP-Disease** (特定疾病)
- 精神分裂症、阿尔茨海默病等

**国际HCP项目**:
- UK Biobank Imaging (英国, 100,000人)
- ABCD Study (美国青少年)
- Chinese Human Connectome Project (中国)

**53. 申请Chinese HCP (如果在中国)**

联系机构：
- 北京师范大学 认知神经科学与学习国家重点实验室
- 网址: http://ccnl.bnu.edu.cn/
- 可能仍在招募

**54-60. 扫描流程**

如果被接受，你将经历：
```
Day 1 (4小时):
  - 知情同意
  - 认知测试电池 (2小时)
  - 问卷调查 (1小时)
  - 血液采样 (可选，用于基因分型)

Day 2 (3小时):
  - MRI扫描 Session 1
    - 结构像 (T1, T2): 30min
    - 静息态fMRI: 30min
    - 任务态fMRI (工作记忆, 情绪识别等): 60min
    - 扩散像 (dMRI): 60min

Day 3 (2小时):
  - MRI扫描 Session 2 (重复部分扫描)
  - MEG/EEG (可选): 60min
```

**61. 获取你自己的数据**

HCP政策：
- 被试可以请求获取自己的数据
- 但需要等待数据处理完成（6-12个月）
- 可能需要签署额外协议

**62-70. 长期追踪**
- 如果项目允许，每隔几年重新扫描
- 建立个人"连接组演化"档案
- 这是永生工程的核心数据！

---

## Level 3: 核心成员（研究者路径）

### 步骤71-90：成为连接组学专家

**71-75. 教育背景建立**
```
本科: 神经科学、认知科学、计算机科学、物理学
硕士: 神经成像、计算神经科学
博士: 专注连接组学
博后: 在HCP核心机构 (WashU, UMinn, Oxford)
```

**76-80. 加入核心机构**

HCP主导机构：
- Washington University in St. Louis (WashU)
- University of Minnesota (UMinn)
- Oxford University (UK)
- MGH Harvard (波士顿)

关键实验室：
- David Van Essen Lab (WashU)
- Kamil Ugurbil Lab (UMinn)
- Stephen Smith Lab (Oxford)

**81-85. 掌握核心技术**
- 7T MRI操作与维护
- HCP Pipeline开发
- Workbench软件开发
- 大规模数据管理 (XNAT, COINS)

**86-90. 主导子项目**
- 申请NIH R01基金
- 领导HCP Phase III某个任务
- 发表Nature/Science级别论文

---

## 替代路径：DIY Connectome（个人方案）

如果无法参与官方HCP，可以自建mini连接组：

### 步骤91-100：个人大脑扫描

**91. 找到愿意扫描你的机构**

选项A: 医院体检MRI
- 成本: $500-2000
- 局限: 通常只有T1/T2结构像，无fMRI/dMRI
- 用途: 基线形态学

选项B: 研究型MRI中心
- 联系当地大学神经科学系
- 询问是否接受"被试"（付费或志愿）
- 成本: $200-500/小时

选项C: 商业脑成像公司
- 美国: **Prenuvo** (全身+大脑MRI, $2500)
- 中国: 部分高端体检中心

**92. 定制扫描序列**

理想HCP-like扫描：
```yaml
结构像:
  - T1w MPRAGE (1mm各向同性)
  - T2w SPACE (1mm)

功能像:
  - rfMRI (TR=720ms, 15min × 2 sessions)

扩散像:
  - dMRI (b=1000, 2000, 3000; 90方向)

预计总时间: 90分钟
成本: $1000-3000
```

**93. 自行处理数据**
```bash
# 使用HCP Pipeline (开源)
git clone https://github.com/Washington-University/HCPpipelines.git
cd HCPpipelines

# 运行PreFreeSurfer
./PreFreeSurfer/PreFreeSurferPipeline.sh \
  --subject="MYSELF" \
  --t1="/path/to/T1w.nii.gz" \
  --t2="/path/to/T2w.nii.gz"

# 运行FreeSurfer
./FreeSurfer/FreeSurferPipeline.sh --subject="MYSELF"

# 运行PostFreeSurfer
./PostFreeSurfer/PostFreeSurferPipeline.sh --subject="MYSELF"
```

**94. 提取你的连接矩阵**
```python
from nilearn import input_data, datasets

# 使用Schaefer脑图谱 (400 ROIs)
atlas = datasets.fetch_atlas_schaefer_2018(n_rois=400)

# 提取时间序列
masker = input_data.NiftiLabelsMasker(labels_img=atlas.maps)
time_series = masker.fit_transform('rfMRI.nii.gz')

# 计算连接矩阵
from nilearn.connectome import ConnectivityMeasure
conn_measure = ConnectivityMeasure(kind='correlation')
conn_matrix = conn_measure.fit_transform([time_series])[0]

# conn_matrix.shape = (400, 400)
np.save('MY_connectome.npy', conn_matrix)
```

**95. 对比HCP平均值**
```python
# 下载HCP group average
hcp_avg = np.load('HCP_1200_group_average_400.npy')

# 计算你的z-score
diff = (conn_matrix - hcp_avg.mean(axis=0)) / hcp_avg.std(axis=0)

# 可视化异常连接
import matplotlib.pyplot as plt
plt.imshow(diff, cmap='RdBu_r', vmin=-3, vmax=3)
plt.title('My Connectome vs HCP (z-scores)')
plt.colorbar()
plt.show()
```

**96. 每年重复扫描**
```
建立个人连接组库:
  - 2025: Baseline
  - 2027: +2 years
  - 2030: +5 years
  - 2035: +10 years
  - ...

追踪指标:
  - 整体连接强度变化
  - 关键hub区域稳定性
  - 与认知功能关联
```

**97. 建立个人数字孪生**
```python
# 使用TVB建立你大脑的计算模型
from tvb.simulator.lab import *

# 加载你的结构连接
my_conn = connectivity.Connectivity(
    weights=my_structural_conn,  # 从dMRI得到
    tract_lengths=my_tract_lengths,
    region_labels=atlas_labels
)

# 校准参数，使模拟fMRI匹配真实fMRI
# (这是一个优化问题，需要数小时计算)

# 保存个人模型
my_conn.save('MY_BRAIN_MODEL.zip')
```

**98. 用于BCI规划**
```python
# 识别最佳BCI植入位点
# 标准: 最大化信息流

import bct

# 计算节点重要性
participation = bct.participation_coef(conn_matrix, modules)
diversity = bct.diversity_coef_sign(conn_matrix, modules)

# 排序节点
importance_score = participation * diversity
top_10_nodes = np.argsort(importance_score)[-10:]

# 映射到大脑坐标
from nilearn import plotting
coords = plotting.find_parcellation_cut_coords(atlas.maps)
top_coords = coords[top_10_nodes]

print("推荐BCI植入坐标:")
for i, coord in enumerate(top_coords):
    print(f"Node {top_10_nodes[i]}: {coord}")
```

**99. 整合到永生计划**
```
你的连接组数据用于:
  ✅ 要素10: 连接组测绘 (已完成)
  ✅ 要素11: BCI植入规划
  ✅ 要素12: 记忆engram定位
  ✅ 要素13: 意识NCC识别
  ✅ 要素16: 大脑备份蓝图
```

**100. 分享到社区**
```bash
# 匿名化你的连接组数据
python anonymize_connectome.py MY_connectome.npy

# 上传到OpenNeuro
# https://openneuro.org/

# 为永生工程贡献第一个"个人追踪"数据集
```

---

## 关键资源汇总

### 官方网站
- HCP主站: https://www.humanconnectome.org/
- ConnectomeDB: https://db.humanconnectome.org/
- WU-Minn Consortium: https://www.humanconnectome.org/study/hcp-young-adult

### 软件工具
- Connectome Workbench: https://www.humanconnectome.org/software/connectome-workbench
- HCP Pipelines: https://github.com/Washington-University/HCPpipelines
- FSL: https://fsl.fmrib.ox.ac.uk/
- FreeSurfer: https://surfer.nmr.mgh.harvard.edu/
- The Virtual Brain: https://www.thevirtualbrain.org/

### 数据集
- HCP-YA (1200人, 22-35岁): AWS S3, 免费
- HCP-Aging (>1000人, 36-100+岁): 申请访问
- HCP-Development (>1500人, 5-21岁): 申请访问
- UK Biobank: https://www.ukbiobank.ac.uk/

### 学习资源
- HCP Course (免费在线): https://store.humanconnectome.org/courses/
- Neurohackademy: https://neurohackademy.org/
- OHBM Educational Courses: https://www.humanbrainmapping.org/

### 社区
- HCP Users邮件列表: hcp-users@humanconnectome.org
- NeuroStars论坛: https://neurostars.org/
- Reddit: r/neuroscience, r/neuroimaging

---

## 成功里程碑

完成本路径后，你应该：

### Level 0 达成
- ✅ 下载并可视化HCP数据
- ✅ 计算基本连接组指标
- ✅ 理解大脑网络拓扑

### Level 1 达成
- ✅ 发表1篇基于HCP的论文
- ✅ 建立研究合作网络
- ✅ 掌握高级分析技术

### Level 2 达成
- ✅ 你的大脑被完整绘制
- ✅ 获得个人连接组数据
- ✅ 建立长期追踪计划

### Level 3 达成
- ✅ 成为连接组学领域专家
- ✅ 主导大型研究项目
- ✅ 推动永生工程的神经科学基础

---

## 与其他要素的协同

```
要素10 (连接组) 是基础设施，服务于:

→ 要素11 (BCI读取): 知道从哪里读
→ 要素12 (记忆编解码): 知道记忆在哪
→ 要素13 (意识NCC): 知道意识的物理基础
→ 要素16 (大脑备份): 知道需要备份什么
→ 要素17 (神经写入): 知道往哪里写
→ 要素18 (连续性验证): 知道身份的物理载体
```

**连接组是"大脑的蓝图"，没有它，永生工程的神经层面无法推进。**

---

**最后更新**: 2025-10-18
**下次审查**: 2026-01-18 (HCP Phase III可能有新数据发布)
**维护者**: 永生工程项目组
