import matplotlib.pyplot as plt

## marker
y = [
    11149139,
    12628348,
    14994823,
    16223089,
    17543067,
    18790538,
    19954397,
    20995416
]
y2 = [
    1149139,
    2628348,
    4994823,
    6223089,
    7543067,
    8790538,
    9954397,
    10995416
]
x = [1961,1965,1971,1975,1979,1983,1988,1993]

# fmt = [marker][line][color]
r = 72
g = 98
b = 219
# 轉算成 16 進制 (Hex)
color = "#{:02X}{:02X}{:02X}".format(r,g,b)
print(color)

plt.plot(
    x,
    y,
    'o-.g',
    ms = 20,
    mfc= 'w',
    color=color,
    linewidth = 3
)
plt.plot(x,y2, '+-.r')
plt.show()