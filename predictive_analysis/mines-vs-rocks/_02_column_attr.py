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

## 這裏歷遍每一欄的資料，把 float 放到 type[0]，string 放到 type[1]，其他放到 type[2]
type = [0]*3
colCounts = []
for col in range(num_of_col):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0] * 3


## 印出結果
print("Col#" + '\t' + "Number" + '\t' + "Strings" + '\t ' + "Other\n")
iCol = 0
for types in colCounts:
    print(str(iCol) + '\t\t' + str(types[0]) + '\t\t' + str(types[1]) + '\t\t' + str(types[2]) + "\n")
    iCol += 1