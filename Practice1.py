import matplotlib.pyplot as plt
import numpy as np

#定義資料格式
dt = np.dtype( # 總共四格資料
    [
        ('Administrative Area','S20'), #地區名稱(20個字的string)
        ('class','S15'),               #地區分類(15的字的string)
        ('area',np.float32),           #面積(32bits 的 float)
        ('population',np.int64),       #人口數(64 bits 的 float)
    ]
)

data = np.array(
    [
        ('New Taipei City','municipality', 2052.5667, 3_974_683),
        ('Taichung City','municipality', 2214.8968, 2_800_981),
        ('Kaohsiung City','municipality', 2951.8524, 2_722_904),
        ('Taipei City','municipality', 271.7997, 2_464_452),
        ('Taoyuan City','municipality', 1220.9540, 2_266_824),
        ('Tainan City','municipality', 2191.6531, 1_850_735),
        ('Changhua County','County', 1074.3960, 1_246_924),
        ('Pingtung County','County', 2775.6003, 800_138),
        ('Yunlin County','County', 1290.8326, 665_750),
        ('Hsinchu County','County', 1427.5369, 577_026),
        ('Miaoli County','County', 1820.3149, 535_221),
        ('Chiayi County','County', 1903.6367, 489_814),
        ('Nantou County','County', 4106.4360, 480_890),
        ('Hsinchu City','City', 104.1526, 450_655),
        ('Yilan County','County', 2143.6251, 448_971),
        ('Keelung City','City', 132.7589, 361_082),
        ('Hualien County','County', 4628.5714, 319_095),
        ('Chiayi City','City', 60.0256, 262_659),
        ('Taitung County','County', 3515.2526, 212_891),
        ('Kinmen County','County', 151.6560, 140_229),
        ('Penghu County','County', 126.8641, 106_221),
        ('Lienchiang County','County', 28.8000, 13_889)
    ],
    dtype = dt # 設定格式
)

index = np.arange(data.size)
height = 0.25 # 偏移

## bar
plt.style.use('ggplot') # 套用style
plt.title("Taiwan populations in each City")
plt.barh(index+height, data['population'],height=height, label='population')
plt.barh(index-height, data['area'],height=height, label='area')
plt.yticks(index,[a.decode("utf-8")  for a in data['Administrative Area']])
plt.grid('both')
plt.legend()
plt.tight_layout()
plt.show()