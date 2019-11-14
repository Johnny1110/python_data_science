import matplotlib.pyplot as plt
import scipy.stats as stats
import urllib.request

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)


#arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
    row = line.decode().strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

#使用第三欄資料做範例
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

# 檢視異常值，在尾部有一些值異常(quartile 大很多)
stats.probplot(colData, dist="norm", plot=plt)
plt.show()