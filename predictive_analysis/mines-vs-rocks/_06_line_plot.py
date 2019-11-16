import pandas as pd
import matplotlib.pyplot as plot

# 使用 pandas 讀取資料
rocksVMines = pd.read_csv("./sonar.all-data", header=None, prefix="V")

for i in range(208):
    # 根據第 60 欄的資料 'M' or 'R' 指定顏色
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"

    # 如果有一系列資料，畫出每列資料
    dataRow = rocksVMines.iloc[i,0:60]
    dataRow.plot(color=pcolor, alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()