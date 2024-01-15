import matplotlib.pyplot as plt
import numpy as np

# figzise 比例
# dpi (dot per inch) 解析度
plt.figure(num = 2,figsize=(8,5),dpi=100)

# 產生一串數字(List), 從-3 ~ 3 之間固定間隔產生共50個數字
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1 + np.random.random_sample(len(x))
y2 = x**2+ np.random.random_sample(len(x))
plt.plot(x,y1)
plt.show()
# 新的畫面
plt.figure(num = 3,figsize=(8,5),dpi=100)
plt.plot(x,y2)
plt.show()