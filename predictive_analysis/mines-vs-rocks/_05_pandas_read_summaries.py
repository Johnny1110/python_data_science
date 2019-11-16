import pandas as pd

# 透過 url 使用 pandas 讀取 csv 檔
rocksVMines = pd.read_csv("./sonar.all-data", header=None, prefix="V")


print(rocksVMines.head()) # 印出頭幾筆資料
print(rocksVMines.tail()) # 印出尾幾筆資料

# 印出資料總攬
summary = rocksVMines.describe()
print(summary)