# set
set1 = set()
set1 = {1,2,3,4,'w'}
# 空字典建立是{}，所以不能使用{}表示空集合
'''
一些运算 - | & ^
'''
set1.add(5)
set1.update(6)
# 都可以
set1.remove(6)  # 会引发KeyError的错误
set1.discard(6)  # 不会引发错误
set1.pop()  # 随机删除一个 返回删除的元素

len(set1)
set1.clear()
2 in set1
# 等等

