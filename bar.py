import numpy as np
import matplotlib.pyplot as plt

x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

fig, ax = plt.subplots()

ax.bar(x, y, width=0.8, edgecolor="white", linewidth=0.7)
#ax.barh(x, y, height=0.8, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()