import matplotlib.pyplot as plt
import numpy as np

# figzise 比例
# dpi (dot per inch) 解析度
plt.figure(num = 2,figsize=(8,5),dpi=100)

# 產生一串數字(List), 從-3 ~ 3 之間固定間隔產生共50個數字
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1 + np.random.random_sample(len(x))
y2 = x**2+ np.random.random_sample(len(x))
plt.plot(x,y1,label = "line 1")
plt.plot(x,y2,label = "line 2")

# 中文字型載入
import matplotlib
filename = r"E:\Eason\家教\python\matplotlib_tutorial\Noto_Sans_TC\NotoSansTC-Thin.otf"
font = matplotlib.font_manager.FontProperties(fname = filename) # 載入字體

# 加上 Xlabel, Ylabel (中文)
plt.xlabel("X 標籤", loc = "right",fontproperties = font) # loc: location 位置(left/center/right)
plt.ylabel("Y 標籤", loc = "top",fontproperties = font) # loc: location 位置(top/center/bottom)

# 加上圖表標題 (中文)
plt.title("這是中文標題",fontproperties = font)

# 加上 grid(只有Y軸,藍色,虛線,寬度0.8)
plt.grid(True, axis='y', color = 'b',linestyle = ':', linewidth = 2)

# 加上邊界限制
plt.ylim((-6,12))
plt.xlim((-4,4))

# 加上刻度資訊
plt.xticks(np.linspace(-4,4,17))
plt.yticks(np.linspace(-6,12,7),["A","B","C","D","E","F","G"])

# 設定邊框顯示或隱藏
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.spines['bottom'].set_visible(False)


plt.tight_layout() #排擠一點，不要讓東西超出邊界
plt.show()