"""
字典的特点
字典的key和value是什么
新建一个字典
"""

# 字典
# 相对于列表，字典的key不仅仅是有序的下标

dict1 = {'one': "我的下标是 one", 2: "我的下标是 2"}
print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值
print('输出所有下标', type(dict1.keys()), dict1.keys())

# 另一种构建方式
dict2 = dict([(1, 2), ('2a', 3), ('3b', 'ff')])
print('第二种构建方式', dict2)

