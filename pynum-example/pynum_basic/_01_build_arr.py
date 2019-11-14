import numpy as np

## 使用 numpy 建立陣列 ##
# ！ 注意 ： numpy 跟標準 python 陣列不一樣，numpy 的陣列元素形態必須統一，
#          如果在一個整數陣列中插入一個 float，會悄悄轉型成 int。

# 常態宣告一維陣列
a0 = np.array((1, 2, 3, 4, 5))


# 建立一個長度爲 10 內容皆為 0 的 int 陣列
a1 = np.zeros(10, dtype=int)

# 建立一個內容皆為 1 的 3*5 float 陣列
a2 = np.ones((3, 5), dtype=float)

# 建立一個內容皆為 3.14 的 3*5 陣列
a3 = np.full((3, 5), 3.14)

# 建立一個依序填滿的陣列 0~20(exclude 20) 以 2 為間隔
a4 = np.arange(0, 20 ,2)

# 建立一個五個值陣列，在 0~1 之間平均分佈
a5 = np.linspace(0, 1, 5, dtype=float)

# 建立一個平均分佈的 3*3 陣列，在 0~1 之間。
a6 = np.random.random((3, 3))

# 建立一個 3*3 陣列，常態分佈亂數，平均值爲 1，標準差爲 0
a7 = np.random.normal(0, 1, (3, 3))

# 建立一個 3*3 陣列，內容介於 0~10 之間
a8 = np.random.randint(0, 10, (3, 3))

# 建立一個 3*3 的單位矩陣
a9 = np.eye(3)

# 建立一個長度爲 3 的未初始化陣列，其值爲原記憶體位址中的值
a10 = np.empty(3)
