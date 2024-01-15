import numpy as np
import matplotlib.pyplot as plt

# 底圖大小
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# 資料
recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe] # 數值
ingredients = [x.split()[-1] for x in recipe] #　名稱

# 自己寫一個打印比例的function
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

# 畫pie
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

# 圖例
ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="upper center",
          bbox_to_anchor=(1, 0, 0.5, 1))
# 設定字型
plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()