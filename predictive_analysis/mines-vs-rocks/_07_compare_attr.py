import pandas as pd
import matplotlib.pyplot as plot

rocksVMines = pd.read_csv("./sonar.all-data", header=None, prefix="V")
## 資料欄是聲納的脈衝週期，共 60 個，脈衝頻率由低到高。
## 比較第 2 列與第 3 列資料的值差

# 讀取第 2 列資料
dataRow2 = rocksVMines.iloc[1, 0:60]
# 讀取第 3 列資料
dataRow3 = rocksVMines.iloc[2, 0:60]

# 畫出 2 筆資料的值分布圖 x, y
plot.scatter(dataRow2, dataRow3)

# 因為第二列資料與第三列資料是聲納前後緊跟著的兩個時間內所回傳的時間(聲納頻率沒差很多)，所以 x 與 y 基本不會差太多。
plot.xlabel("第二個脈衝週期")
plot.ylabel(("第三個脈衝週期"))
plot.show()

#####################################################
# ------------------------------------------------- #
#####################################################

## 比較第 2 列與第 21 列資料的值差

dataRow21 = rocksVMines.iloc[20, 0:60]

# 畫出 2 筆資料的值分布圖 x, y
plot.scatter(dataRow2, dataRow21)

# 這次比較的是第 2 列與第 3 列資料的差，因為前後時間差很多(聲納頻率差很多)，所以 x 與 y 的值可以看到明顯差異
plot.xlabel("第二個脈衝週期")
plot.ylabel(("第二十一個脈衝週期"))
plot.show()
