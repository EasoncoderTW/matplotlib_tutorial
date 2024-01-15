# 直方圖
# 級距統計(多少到多少數字之間有多少人)

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
score = np.random.normal(75,25,200) # 常態分布(0~50)共200筆資料
score = [s for s in score if s <= 100 and s >= 0] # 把超出範圍的分數去掉

# 畫histgram
fig, ax = plt.subplots()
ax.hist(score, bins = 10, linewidth = 0.5, edgecolor ="white")

ax.set(xlim = (0,100), xticks = np.arange(0,100,10),
       ylim = (0,50), yticks = np.arange(0,50,10))

ax.text(0.1,45,"Hello")
ax.text(10,45,"Hello",fontsize = 14, 
        bbox = dict(boxstyle = 'round', facecolor = 'wheat', alpha = 0.5))

plt.show()