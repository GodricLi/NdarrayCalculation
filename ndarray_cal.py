# _*_ coding=utf-8 _*_


import numpy as np

"""ndarray运算
区别：
    列表乘以标量，列表内元素个数增加[1,2]*2=[1,2,1,2]
    列表与int类型不能加减除
"""
a = np.array([1,2])
b = np.array([3,4])

# 数组与标量之间的运算
print(a + 1)
print(a *3)
print(a /3)
print(3/a)
print(a **2)
print(a > 5)

# 数组之间的运算
print(a+b)
print(a/b)
print(a*b)
print(a**b)
print(a%b)
print(a==b)
print(a>b)
