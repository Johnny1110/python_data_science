import numpy as np

## NumPy 陣列屬性 ##

def arrays_attr():
    # 指定種子，確保 random 產生的亂數值統一。
    np.random.seed(0)

    a1 = np.random.randint(10, size=6)  # 一維陣列 6 個
    a2 = np.random.randint(10, size=(3, 4))  # 二維陣列 3 * 4
    a3 = np.random.randint(10, size=(3, 4, 5))  # 三維陣列 3 * 4 * 5

    print(a1)
    print('-----------------------')
    print(a2)
    print('-----------------------')
    print(a3)

    # 陣列的屬性 ： ndim(維度數量)，shape(每一個維度的大小)，size(整個陣列的總大小)，dtype(陣列資料形態)
    #            itemsize(陣列元素大小/bytes)，nbytes(整個陣列大小)。
    print("a3.ndim : ", a3.ndim)
    print("a3.shape : ", a3.shape)
    print("a3.size : ", a3.size)
    print("a3.dtype", a3.dtype)
    print("a3.itemsize : ", a3.itemsize, " bytes")
    print("a3.nbytes", a3.nbytes, " bytes")

if __name__ == '__main__':
    arrays_attr()