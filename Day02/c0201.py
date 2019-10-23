# 字典
d = {'key1' : 'value1', 'key2' : 2 }
# key必须是固定的，值可以是可变的
print(d['key1'])
d['key1']=[3]
print('', d['key1'])
# del a key
del d['key1']
# clear dic
d.clear()
# del dic
del d
# 如果同一个键被赋值两次，后一个值会被记住
