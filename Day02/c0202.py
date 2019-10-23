# set
set1 = set()
set1 = {1,2,3,4,'w'}
# 建立空集合不能用{}
'''
集合的运算 - | & ^
'''
set1.add(5)
set1.update(6)

set1.remove(6)  # 会引发KeyError错误
set1.discard(6)  # 不会引发错误
set1.pop()  # 随机删除一个元素并返回

len(set1)
set1.clear()
2 in set1
#

