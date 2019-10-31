"""
多变量赋值
如何查看一个变量的类型
如何判断一个变量是一个类型或者他的子类型
删除一个变量
什么是可改变类型 什么是不可改变类型
了解try
常见的数学运算
"""

# 多变量赋值
a = b = c = "python中"
d, e, f, g = 3, [5.5, 'a', 6], "可变数据", '不'
print(a, '有', d, '个', f)
print(type(e), type(dict()), type(set()))
print(a, '有', d, '个', g, f)
print(type(d), type(a), type(tuple()))

'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
print(type(1) == int)
print(isinstance(1, int))

# 删除一个变量
del b

'''
加+
减-
乘*
除/
整除//  这个返回时候取最精确值 7//2=3  7.0//2=3.5
取余%
乘方**
'''
# 字符串不可改变
try:
    "qwe"[1] = "r"
except Exception:
    print("字符串不可改变")


