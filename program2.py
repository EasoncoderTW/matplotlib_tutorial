import matplotlib.pyplot as plt

# 畫一條線
plt.figure() # 畫布

# 總共5個座標
y = [1,3,2,5,4]
x = [1,3,5,7,9]

plt.plot(x,y,'3-')  # 預設x從0開始，間隔為1

# 顯示
plt.show()
