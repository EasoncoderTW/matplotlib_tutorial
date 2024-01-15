import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(-10,10,200)
noise = np.random.uniform(-5,5,len(x))
y = (x)**2 + noise
sizes = np.random.uniform(5,50,len(x))
colors = np.random.uniform(5,50,len(x))

fig = plt.figure()
plt.scatter(x,y,marker='o',s=sizes, c=colors)
plt.show()