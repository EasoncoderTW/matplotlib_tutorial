import matplotlib.pyplot as plt

# 中文字型載入
import matplotlib
filename = r"E:\Eason\家教\python\matplotlib_tutorial\Noto_Sans_TC\NotoSansTC-Bold.otf"
font = matplotlib.font_manager.FontProperties(fname = filename) # 載入字體

y1 = [29.4,34.2,32.1,36.4,35.6,35.4,37.6,36.5,34.2,34.7,33.8]
y2 = [35.4,27.5,26.8,27.7,24.3,25.6,24.2,29.5,26.0,27.4,28.3]
y3 = [23.2,16.9,21.4,23.1,28.8,24.2,24.3,22.9,24.1,25.5,26.1]

plt.style.use('seaborn-v0_8-dark')
plt.figure(figsize=(8,3),dpi=100)

plt.plot(y1,marker='s', ms=5, color = "g", lw = 2,label = "DPP")
plt.plot(y2,marker='o', ms=5, color = "b", lw = 2,label = "KMT")
plt.plot(y3,marker='^', ms=5, color = "c", lw = 2,label = "TPP")

plt.ylabel("%",loc="top")

plt.title("2024大選民調",fontproperties = font)

plt.legend() #show the label

plt.grid(True,which="major",axis="y",color = "b",linestyle = ":", linewidth = 0.8)

ax = plt.gca()
ax.spines['left'].set_visible(True)
ax.spines['left'].set_linewidth(2)
ax.spines['left'].set_color('r')
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_linewidth(2)
ax.spines['bottom'].set_color('r')

plt.show()