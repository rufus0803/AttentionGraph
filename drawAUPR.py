import torch
import matplotlib.pyplot as plt

# 加载数据
data1 = torch.load("/Volumes/Samsung/result/300_epoch_0.638/loss_bpCLaf.pt")
data2 = torch.load("/Volumes/Samsung/result/0.647/loss_bpCLaf.pt")  # 替换为第二个AUPR数据的文件路径
data3 = torch.load("/Volumes/Samsung/result/0.65/loss_bpCLaf.pt")   # 替换为第三个AUPR数据的文件路径

# 提取AUPR数据
val_aupr1 = data1["val_aupr"]
val_aupr2 = data2["val_aupr"]
val_aupr3 = data3["val_aupr"]

max_val_aupr1 = max(val_aupr1)
max_val_aupr2 = max(val_aupr2)
max_val_aupr3 = max(val_aupr3)

# 生成 x 轴坐标（例如，使用数据点的索引作为 x 值）
x1 = range(1, len(val_aupr1) + 1)
x2 = range(1, len(val_aupr2) + 1)
x3 = range(1, len(val_aupr3) + 1)

# 创建一个3x1的图表布局
plt.figure(figsize=(8, 12))  # 调整图表大小

# 第一个子图
plt.subplot(3, 1, 1)
plt.plot(x1, val_aupr1, label="AUPR 1")
plt.title("AUPR 1")
plt.xlabel("Epoch")
plt.ylabel("Val AUPR")
plt.hlines(max_val_aupr1, 1, len(val_aupr1), colors='r', linestyles='dashed', label=f"Max Val AUPR: {max_val_aupr1}")
plt.legend()

# 第二个子图
plt.subplot(3, 1, 2)
plt.plot(x2, val_aupr2, label="AUPR 2")
plt.title("AUPR 2")
plt.xlabel("Epoch")
plt.ylabel("Val AUPR")
plt.hlines(max_val_aupr2, 1, len(val_aupr2), colors='r', linestyles='dashed', label=f"Max Val AUPR: {max_val_aupr2}")
plt.legend()

# 第三个子图
plt.subplot(3, 1, 3)
plt.plot(x3, val_aupr3, label="AUPR 3")
plt.title("AUPR 3")
plt.xlabel("Epoch")
plt.ylabel("Val AUPR")
plt.hlines(max_val_aupr3, 1, len(val_aupr3), colors='r', linestyles='dashed', label=f"Max Val AUPR: {max_val_aupr3}")
plt.legend()

# 调整子图之间的垂直间距
plt.tight_layout()

# 显示图表
plt.show()
