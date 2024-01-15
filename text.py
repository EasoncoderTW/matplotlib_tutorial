import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,200)
y = np.random.normal(0,15,200)

max_y = max(y)
max_x = x[y.argmax()] # argmax : 最大值的index

min_y = min(y)
min_x = x[y.argmin()] # argmax : 最大值的index

fig, ax = plt.subplots()

ax.plot(x,y)
ax.text(max_x,max_y+1,"Max",fontdict=dict(color = "red"))
ax.text(min_x,min_y-1,"Min",fontdict={"color":"green"})


plt.savefig("./text.jpg")
plt.show()
