import numpy as np

## 使用 ufuncs 達到更有效率的進行陣列用算，不僅在寫法上精簡，而且在底層演算上也是最有效率的做法。
## 在 python 中不能以 algor-like(C/C++ or java) 語言的思維去寫算法，盡量多習慣去用 ufuncs。

# 生成一個陣列
np.random.seed(0)
values = np.random.randint(1, 10, size=5)
print(values)

# 算出陣列的倒數 (陣列 vs 純量)
print(1.0 / values)

# 陣列互除
print(np.arange(5)/np.arange(1, 6))

# 2 的 x 次方
x = np.arange(9).reshape([3, 3])
print(2 ** x)
