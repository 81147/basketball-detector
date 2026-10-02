# \# 篮球检测项目

# 

# 基于 Ultralytics YOLOv8n 微调的篮球单类检测器。输入统一验收视频，输出带检测框、标签、置信度、运动轨迹和中心坐标的结果视频。

# 

# \## 环境要求

# 

# \- 操作系统：Windows 10/11

# \- Python：3.11

# \- GPU：NVIDIA（本项目在 RTX 5080 Laptop，CUDA 12.8 上验证）

# 

# \## 安装依赖

# 

# python -m venv .venv

# .venv\\Scripts\\activate

# pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

# pip install -r requirements.txt

# 

# \## 数据

# 

# dataset/包含YOLO格式的单类篮球检测数据：

# 训练集：600张图，669个标注框

# 验证集：100张图，106个标注框

# 类别：0=basketball

# 配置：dataset/data.yaml

# 

# \## 训练

# 

# python train.py

# 参数：YOLOv8n 预训练权重，epochs=40，imgsz=640，batch=16，device=0。

# 训练结果保存在 runs/basketball\_yolov8n-5/weights/best.pt。

# 验证集指标：Precision 0.934，Recall 0.887，mAP50 0.929。

# 

# \## 推理

# 

# python detect\_video.py

# 输入：evaluation/basketball\_dribble\_evaluation.mp4

# 模型：model/best.pt

# 输出：result.mp4

# 

# \## 预期输出

# 

# result.mp4 中：

# 篮球周围的检测框

# 标签 basketball 和置信度

# 篮球运动轨迹（黄色连线）

# 画面左上角显示当前帧篮球中心坐标

# 

# \## 误检案例

# 

# 刚开始输出视频会把操场识别为篮球，不过置信度只有0.53，调整置信度阈值为0.6就解决了。# 篮球检测项目

# 

# 基于 Ultralytics YOLOv8n 微调的篮球单类检测器。输入统一验收视频，输出带检测框、标签、置信度、运动轨迹和中心坐标的结果视频。

# 

# \## 环境要求

# 

# \- 操作系统：Windows 10/11

# \- Python：3.11

# \- GPU：NVIDIA（本项目在 RTX 5080 Laptop，CUDA 12.8 上验证）

# 

# \## 安装依赖

# 

# python -m venv .venv

# .venv\\Scripts\\activate

# pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

# pip install -r requirements.txt

# 

# \## 数据

# 

# dataset/包含YOLO格式的单类篮球检测数据：

# 训练集：600张图，669个标注框

# 验证集：100张图，106个标注框

# 类别：0=basketball

# 配置：dataset/data.yaml

# 

# \## 训练

# 

# python train.py

# 参数：YOLOv8n 预训练权重，epochs=40，imgsz=640，batch=16，device=0。

# 训练结果保存在 runs/basketball\_yolov8n-5/weights/best.pt。

# 验证集指标：Precision 0.934，Recall 0.887，mAP50 0.929。

# 

# \## 推理

# 

# python detect\_video.py

# 输入：evaluation/basketball\_dribble\_evaluation.mp4

# 模型：model/best.pt

# 输出：result.mp4

# 

# \## 预期输出

# 

# result.mp4 中：

# 篮球周围的检测框

# 标签 basketball 和置信度

# 篮球运动轨迹（黄色连线）

# 画面左上角显示当前帧篮球中心坐标

# 

# \## 误检案例

# 

# 刚开始输出视频会把操场识别为篮球，取了前几帧，看看误检的和实际的框置信度在什么区间，调整置信度阈值为0.6就解决了。

