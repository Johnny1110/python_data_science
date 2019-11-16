import numpy as np

## 一維陣列切片 ##

# 說明： 陣列切片使用 '：' 隔開，標準切割格式如下
#       x[start:stop:step]

a1 = np.arange(10)

# 切出索引 5 以前個元素
print(a1[:5])

# 切出索引 5 以後的元素
print(a1[5:])

# 切出索引 between 4~7 的元素
print(a1[4:7])

# 間隔 2 的所有元素
print(a1[::2])

# 反轉所有元素 (start 與 stop 互換)
print(a1[::-1])

# 從索引 5 開始反轉向前切，以 2 爲 step
print(a1[5::-2])

## ------------------------------------------------------- ##

## 多維陣列切片 ##

a2 = np.array(
    [[0, 1, 2, 3],
     [4, 5, 6, 7],
     [8, 9, 10, 11]]
)

# 切 2 列 3 欄
print(a2[:2, :3])

# 所有奇數數列
print(a2[:3, ::2])

# 反轉陣列
print(a2[::-1, ::-1])

# 取第一列
print(a2[:, 0])

# 取第一欄
print(a2[0, :])

# !注意 : numpy 的陣列切片結果是傳址，並不是傳值。
sub_arr = a2[:2, :2]
sub_arr[0, 0] = 100
print(sub_arr)
print(a2)

# 若不想使用 numpy 傳址特性，可以使用 copy() 函式取得物件
sub_arr2 = a2[:2, :2].copy()
sub_arr2[0, 0] = 99
print(sub_arr2)
print(a2)

## ------------------------------------------------------- ##

## 陣列 reshape ##

# 把 1~9 放到一個 3*3 的陣列中。
# 若給定的資料不能剛好放完，會報錯。
a3 = np.arange(1, 10).reshape((3, 3))
print(a3)

a4 = np.array([1, 2, 3])
# reshape 建立列向量
print(a4.reshape(1, 3))
# reshape 建立欄向量
print(a4.reshape(3, 1))