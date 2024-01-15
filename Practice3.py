import  matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filepath = ".\ParisHousing.csv"

dataframe = pd.read_csv(filepath)

print(dataframe.head()) # 只印出開頭幾個

squareMeters = dataframe['squareMeters'] # 房子面積
price = dataframe['price'] # 價錢

# plt.plot 畫線
# 散點圖
plt.scatter(squareMeters, price, marker='o')
plt.xlabel('square Meters')
plt.ylabel('price')
plt.title("Compare")

plt.tight_layout()
plt.show()