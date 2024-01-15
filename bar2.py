import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
x_name = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jly","Aug","Sep","Oct","Nov","Dec"]
y = [100,200,100,300,200,100,400,500,200,300,100,200]

color = []
for i in y:
    if i < 200:
        color.append("red")
    elif i >= 300:
        color.append("green")
    else:
        color.append("blue")



fig, ax = plt.subplots()

ax.bar(x, y,color=color ,width=0.8, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 13), ylim=(0, 700), yticks=np.arange(0, 700, 100))

#ax.set_xlim
#ax.set_ylim
ax.set_xticks(x,x_name)
#ax.set_yticks

plt.show()