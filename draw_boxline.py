import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 生成两组箱线图数据
np.random.seed(42)  # 为了保持随机性一致性，设置随机种子

# 设置箱线图的横坐标位置
positions_group1 = [30, 45, 70, 81]
positions_group2 = [22, 52, 64, 85]
positions_group3 = [35, 48, 73, 91]
positions_group4 = [40, 58, 78, 95]

# 生成两组数据，每组有五个箱线
data_group1 = [[0.28620943, 0.23054463, 0.08749416, 0.25886295, 0.11058355],
               [0.29697277, 0.28429029, 0.25192312, 0.38147974, 0.38555463],
               [0.23660004, 0.48190888, 0.4556064 , 0.32992719, 0.4723933 ],
               [0.34940479, 0.31737194, 0.50264895, 0.37716632, 0.49346724]]

data_group2 = [[0.2511499, 0.2025898 , 0.35919249, 0.16102231, 0.23559444],
               [0.30398685, 0.38711895, 0.2732603 , 0.36388695, 0.33000712],
               [0.42168935, 0.45879627, 0.46997925, 0.52178676, 0.48537807],
               [0.4309611 , 0.52656222, 0.44254574, 0.5394071 , 0.59351097]]

data_group3 = [[0.12523292, 0.41356524, 0.23542244, 0.31878744, 0.46864105],
               [0.33143538, 0.39151649, 0.45793981, 0.45784942, 0.52958691],
               [0.49363451, 0.57517251, 0.6984833 , 0.62658194, 0.68024936],
               [0.76437674, 0.62072476, 0.74184292, 0.82312519, 0.79416544]]

data_group4 = [[0.38888332, 0.45876387, 0.46313562, 0.35137475, 0.53430383],
               [0.62010347, 0.55144374, 0.56115267, 0.45917624, 0.65568288],
               [0.74125986, 0.71815191, 0.61721354, 0.782224644, 0.82522591],
               [0.87316317, 0.73262697, 0.92578036, 0.8973051 , 0.95287138]]

fig, ax = plt.subplots()
ax.boxplot(data_group1, positions=positions_group1, widths=2, patch_artist=True, boxprops=dict(facecolor='#32CD32'))
ax.boxplot(data_group2, positions=positions_group2, widths=2, patch_artist=True, boxprops=dict(facecolor='#FF6347'))
ax.boxplot(data_group3, positions=positions_group3, widths=2, patch_artist=True, boxprops=dict(facecolor='#008080'))
ax.boxplot(data_group4, positions=positions_group4, widths=2, patch_artist=True, boxprops=dict(facecolor='#DAA520'))

# 添加背景颜色
ax.axvspan(20, 42, facecolor='#FADADD', alpha=0.5)
ax.axvspan(42, 60, facecolor='#FEF9D9', alpha=0.5)
ax.axvspan(60, 80, facecolor='#D8F5FF', alpha=0.5)
ax.axvspan(80, 100, facecolor='#E9FAD0', alpha=0.5)

# 设置图例
legend_patches = [
    Patch(color='#32CD32', label='DeepFRI'),
    Patch(color='#FF6347', label='HEAL'),
    Patch(color='#008080', label='Struct2GO'),
    Patch(color='#DAA520', label='SEA-GO')
]
ax.legend(handles=legend_patches)

# 设置图表标题和标签
ax.set_title('Robustness evaluation (MF-GO)')
ax.set_xlabel('Maximum sequence identity to training set(%)')
ax.set_ylabel('Fmax')

# 设置横坐标和纵坐标的范围
ax.set_xlim(20, 100)
ax.set_ylim(0, 1.0)

# 设置横坐标刻度
ax.set_xticks([20, 40, 60, 80, 100])
ax.set_xticklabels(['20', '40', '60', '80', '100'])

plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

plt.savefig('/Users/rufus/Downloads/Fig3.png', dpi=500)
# 显示图表
plt.show()