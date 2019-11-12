"""
如何建立一个集合
如何向集合中添加元素
如何移除集合中的某个元素
如何查看集合中共有多少元素
如何知道某元素在没在集合中
"""
# set
set1 = set()
set1 = {1, 2, 3, 4, 'w'}
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

