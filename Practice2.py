import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 中文字型載入
import matplotlib
filename = r".\Noto_Sans_TC\NotoSansTC-Thin.otf"
font = matplotlib.font_manager.FontProperties(fname = filename) # 載入字體

# 讀檔
dataframe = pd.read_csv("./chart.csv")
print(dataframe)

# 排除異物
dataframe = dataframe.dropna() #丟掉含有 NaN(Not a Number) 的資料
print(dataframe.columns)

# 獲得label名稱
labels = list(dataframe.columns)
x_label = labels[0]
y_labels = labels[1:]
print(x_label)
print(y_labels)

# 繪圖 (把每個label的資料plot上去)
plt.figure(figsize=(12,5),dpi = 100) # 1200 x 500
for label in y_labels:
    x = dataframe[x_label]
    y = dataframe[label]
    plt.plot(x, y, label = label)

plt.title("全國及各區近兩年每周急診類流感就診率趨勢圖",font = font)
plt.ylabel("就診比率(%)",font = font)
plt.xlabel("就診年週",font = font)

# 設定邊框顯示或隱藏
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.legend(prop = font) # 圖例
plt.tight_layout()
plt.show()

