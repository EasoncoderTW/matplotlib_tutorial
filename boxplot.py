import matplotlib.pyplot as plt
import numpy as np

#資料
D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))

fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[2, 4, 6], widths=1.2, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.8}, # 中位數標線
                boxprops={"facecolor": "C0", "edgecolor": "white", # 盒狀參數
                          "linewidth": 0.8},
                whiskerprops={"color": "C0", "linewidth": 1.5}, # 直桿參數
                capprops={"color": "C0", "linewidth": 1.5}) # 橫桿參數

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()