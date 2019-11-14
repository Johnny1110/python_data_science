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

num_of_row = len(xList)
num_of_col = len(xList[1])

print("資料量總數 ： ", num_of_row)
print("可分析欄位數量 ： ", num_of_col)
