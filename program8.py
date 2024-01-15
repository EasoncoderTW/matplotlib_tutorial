import matplotlib.pyplot as plt
import numpy as np

# style 設定
plt.style.use('fivethirtyeight')

# figzise 比例
# dpi (dot per inch) 解析度
plt.figure(num = 2,figsize=(8,5),dpi=100)

# 產生一串數字(List), 從-3 ~ 3 之間固定間隔產生共50個數字
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1 + np.random.random_sample(len(x))
y2 = x**2+ np.random.random_sample(len(x))
plt.plot(x,y1)
plt.plot(x,y2)

# 加上 Xlabel, Ylabel
plt.xlabel("Xlabel", loc = "right") # loc: location 位置(left/center/right)
plt.ylabel("Ylabel", loc = "top") # loc: location 位置(top/center/bottom)

# 加上圖表標題
plt.title("This is a Graph")
#plt.title("這是一個圖表")

plt.tight_layout() #排擠一點，不要讓東西超出邊界
plt.show()