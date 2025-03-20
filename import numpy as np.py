import numpy as np
import matplotlib.pyplot as plt

# 生成离散余弦信号
def discrete_cosine_signal(t, frequency=1):
    return np.cos(2 * np.pi * frequency * t)

# 生成离散阶跃信号
def discrete_step_signal(t, step_time=0):
    return np.where(t >= step_time, 1, 0)

# 设置离散时间范围
t_discrete = np.linspace(-2, 2, 20)

# 计算离散信号值
cosine = discrete_cosine_signal(t_discrete)
step = discrete_step_signal(t_discrete)

# 创建图形和子图
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# 绘制离散余弦信号
axes[0].stem(t_discrete, cosine)
axes[0].set_title('离散余弦信号')
axes[0].set_xlabel('时间')
axes[0].set_ylabel('振幅')
axes[0].grid(True)

# 绘制离散阶跃信号
axes[1].stem(t_discrete, step)
axes[1].set_title('离散阶跃信号')
axes[1].set_xlabel('时间')
axes[1].set_ylabel('振幅')
axes[1].grid(True)

# 调整子图布局
plt.tight_layout()

# 显示图形
plt.show()
    