"""
如何接收键盘输入
调整print函数默认的结束符
如何导入包
如何获得运行参数
"""
input_s = input('输入任何内容后回车\n')
print('输入的内容为\n', input_s, sep='')

print('在一行中', end=''); print('输入多个语句');

import sys
print('\n导入包演示\n', '一些关键路径', sys.path)
print('运行参数：')
for i in sys.argv:
    print(i)
