"""
列表是什么
反转列表怎么操作
列表与字符串和元组的异同
"""
print("列表是使用比较频繁的数据结构")
# 列表的切分
# 列表的+运算和*运算
# 都和str一样

# 列表中的元素可以改变


def reverse_list(inlist):
    inlist.reverse()
    return inlist


l1 = [1, 2, 3, 4]
l2 = reverse_list(l1)
print(l2)


def reverse_str(instr):
    inwords = instr.split(" ")
    inwords = inwords[-1::-1]
    ans = " ".join(inwords)
    return ans


s1 = "q w e r"
s2 = reverse_str(s1)
print(s2)

# 元组
t1 = (1, 'q', 3, 'w')
print(t1[:2])
