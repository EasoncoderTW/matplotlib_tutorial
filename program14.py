import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,sharey=True) # 共用X軸標籤
fig.suptitle('Vertically stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y/2)
ax3.plot(x, y*2)

plt.show()