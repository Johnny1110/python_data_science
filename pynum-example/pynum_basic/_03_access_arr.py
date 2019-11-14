import numpy as np


## 一維陣列存取 ##

a1 = np.array((1, 2, 3, 4, 5))

# 正常取值操作
print("first elem", a1[0])

# 使用負號逆向取值
print("last elem", a1[-1])


## 多維陣列存取 ##

a2 = np.array(
    [[0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]]
)

print(a2[0, 0])




