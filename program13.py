import matplotlib.pyplot as plt
import numpy as np

# 處理小圖的設定
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False) # 不要有刻度

# 切網格需要
from matplotlib.gridspec import GridSpec

fig = plt.figure()

gs = GridSpec(3,3,figure=fig)

#     0  1  2
#   +----------
# 0 | 1  1  2
# 1 | 3  4  4
# 2 | 5  4  4
#   +----------

ax1 = fig.add_subplot(gs[0,0:2])
ax2 = fig.add_subplot(gs[0,2])
ax3 = fig.add_subplot(gs[1,0])
ax4 = fig.add_subplot(gs[1:,1:])
ax5 = fig.add_subplot(gs[2,0])


fig.suptitle("GirdSpec")
format_axes(fig)

plt.show()