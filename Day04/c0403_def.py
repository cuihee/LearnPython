def area(width, height):
    return width * height

print(area(1.5, 3))
print(area([1,2,3], 2))

'''
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。
可变类型：类似 c++ 的引用传递，如 列表，字典。
'''
# 不可变类型
def changeInt(a):
    a=10
a = 2
changeInt(a)
print('a =', a)
# 可变类型 关键字参数 默认参数
def changeList(list_a=[0]):
    list_a[-1] = 0
a = [1,2,3]
changeList(list_a=a)
print('a =', a)
