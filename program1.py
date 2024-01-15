import matplotlib.pyplot as plt

# 畫一條線
plt.figure() # 畫布

# 總共5個座標
x = [1,2,3,5,5]
y = [2,4,3,1,2]

plt.plot(x,y,'o-') # 'o' 點, '-' 線

# 顯示
plt.show()
