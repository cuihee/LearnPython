# str
print('\x0a')

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

# list
l1 = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", l1)
del l1[2]
print("删除第三个元素 : ", l1)

# 嵌套
l2 = [1, l1]
print(l2[1][0])

# 元组
t1 = (10,)  # 不加逗号视括号为运算符，所以没有逗号的t1是int
t2 = 'a',
print(type(t1), type(t2))
# 访问和列表一样 用切片
# 删除只能删除整个元组不能删除其中的一个元素
# 元组的内置函数 len() min() max()

