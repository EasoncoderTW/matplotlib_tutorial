import matplotlib.pyplot as plt
import numpy as np

# x: 比例
x = [20,30,5,45] # [4,6,1,9]
labels = ["A","B","C","D"]
colors = plt.get_cmap('coolwarm')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x,labels = labels, colors=colors, radius=3, center=(5, 5),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 10), yticks=np.arange(1, 10))

plt.show()