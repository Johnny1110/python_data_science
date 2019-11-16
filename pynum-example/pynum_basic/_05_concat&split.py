import numpy as np

## numpy 串接陣列

# np.concatenate 串接多個一維陣列
a1 = np.array([1, 2, 3])
a2 = np.array([3, 2, 1])
a3 = np.array([2, 2, 2])
a4 = np.concatenate([a1, a2, a3])
print(a4)

# 使用 np.concatenate 串接多個二維陣列

a5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

a6 = np.array([
    [4, 5, 6],
    [7, 8, 9]
])

# 依列串接(往下接)
a7 = np.concatenate([a5, a6])
print(a7)

# 依欄串接(往右接)
a8 = np.concatenate([a5, a6], axis=1)
print(a8)



# 使用 np.vstack 與 np.hstack 串接不同維度陣列
x = np.array([1, 2, 3])

y = np.array([
    [9],
    [9]
])

grid = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

## vstack 垂直堆疊
print(np.vstack([x, grid]))

## hstack 水平堆疊
print(np.hstack([grid, y]))


#########################################################################
#-----------------------------------------------------------------------#
#########################################################################


## numpy 分割陣列

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x1, x2, x3 = np.split(x, [2, 7])
print(x1, x2, x3)


grid = np.arange(16).reshape((4, 4))
# 切割多維陣列(腰斬)
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

# 切割多維陣列(劈開)
left, right = np.hsplit(grid, [2])
print(left)
print(right)


