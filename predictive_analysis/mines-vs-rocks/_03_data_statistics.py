import urllib.request
import numpy as np

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:

    row = line.decode().strip().split(",")
    xList.append(row)

num_of_row = len(xList)
num_of_col = len(xList[1])

type = [0]*3
colCounts = []

# 產生第三欄的資料陣列
col3Data = []
for row in xList:
    col3Data.append(float(row[3]))

colArray = np.array(col3Data) # 使用 numpy 裝填陣列
colMean = np.mean(colArray) # 求平均值
colsd = np.std(colArray) # 求標準差
print('Mean(平均值) = ', colMean, '\t\t', 'Standard Deviation(標準差) = ', colsd, "\n")

# 計算第三欄的資料陣列分位界限
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, (i*100)/ntiles)) # 分位值爲 < 0%, 25%, 50%, 75%, 100% >
print("percentBdry = ", percentBdry)

# 統計魚雷跟岩石數量(col 60)
col = 60
col60Data = []
for row in xList:
    col60Data.append(row[col])

unique = set(col60Data) #把 col60Data 中不重複的值放入
print('col 60 中的資料含有 ： ', unique)

# 建立 unique 的字典，初始值爲 ： {'R': 0, 'M': 0}
catDict = dict(zip(unique, [0]*len(unique)))

# 統計岩石跟魚雷總數放入 catDict 中
for el in col60Data:
    temp = catDict.get(el) + 1
    catDict.update(dict({el: temp}))
print(catDict)

