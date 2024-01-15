import matplotlib.pyplot as plt
import numpy as np

# 中文字型載入
import matplotlib
filename = r".\Noto_Sans_TC\NotoSansTC-Thin.otf"
font = matplotlib.font_manager.FontProperties(fname = filename) # 載入字體

# x: 比例
money = [60,100,40,80,30]
labels = ["早餐","午餐","下午茶","晚餐","點心"]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(money)))

arg_max = 0
for i in range(len(money)):
    if money[i] > money[arg_max]:
        arg_max = i

explode = [0,0,0,0,0] # 向外抽出
explode[arg_max] = 0.5

# plot
fig, ax = plt.subplots()
#_,c,_= ax.pie(money,labels = labels, explode=explode, colors=colors, radius=3, center=(5, 5),
#    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True,
#    autopct="%1.1f%%") # "%1.1f" -> 小數(小數點以下一位), %% -> "%""

# 客製化的打印資料
def func(pct, data):
    percent = pct/sum(data)*100
    value = int(pct)

    return f"{percent:.1f}%\n${value:d}"


_,c,_= ax.pie(money,labels = labels, explode=explode, colors=colors, radius=3, center=(5, 5),
    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True,
    autopct=lambda pct: func(pct, money)) # "%1.1f" -> 小數(小數點以下一位), %% -> "%""

for i in c:
    i.set_fontproperties(font) # 對每一個label都設定font

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 10), yticks=np.arange(1, 10))

plt.show()