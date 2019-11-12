"""
集合与其他类型的异同
集合的成员测试是什么意思
新建一个集合
集合的六种常见运算
"""
# set

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素Tom被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# 新建集合
a = set('ab')
b = set('bc')

# set可以进行集合运算
print("a=", a)
print("b=", b)
print("a-b=", a - b)  # a 和 b 的差集
print("a|b=", a | b)  # a 和 b 的并集
print("a&b=", a & b)  # a 和 b 的交集
print("a^b=", a ^ b)  # a 和 b 中不同时存在的元素
