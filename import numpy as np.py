import numpy as np
import matplotlib.pyplot as plt


# 生成余弦信号
def cosine_signal(t, frequency=1):
    return np.cos(2 * np.pi * frequency * t)


# 生成阶跃信号
def step_signal(t, step_time=0):
    return np.where(t >= step_time, 1, 0)


# 设置时间范围
t = np.linspace(-2, 2, 1000)

# 计算信号值
cosine = cosine_signal(t)
step = step_signal(t)

# 创建图形和子图
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# 绘制余弦信号
axes[0].plot(t, cosine)
axes[0].set_title('余弦信号')
axes[0].set_xlabel('时间')
axes[0].set_ylabel('振幅')
axes[0].grid(True)

# 绘制阶跃信号
import numpy as np
import matplotlib.pyplot as plt


# 生成余弦信号
def cosine_signal(t, frequency=1):
    return np.cos(2 * np.pi * frequency * t)


# 生成阶跃信号
def step_signal(t, step_time=0):
    return np.where(t >= step_time, 1, 0)


# 设置时间范围
t = np.linspace(-2, 2, 1000)
# 为了离散化，选择较少的点
t_discrete = np.linspace(-2, 2, 20)

# 计算信号值
cosine = cosine_signal(t)
step = step_signal(t_discrete)

# 创建图形和子图
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# 绘制余弦信号
axes[0].plot(t, cosine)
axes[0].set_title('余弦信号')
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
    