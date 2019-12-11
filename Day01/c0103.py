"""
一些特殊的字符 单引号 双引号 斜杠 等的用法
字符串前面的r是什么意思
反斜杠的意思
字符串的+ *运算
字符串的切片操作

"""
print('python中单引号\'和双引号\"使用完全相同，\\是转义符，三引号表示多行字符串')
print(r'使用前置的r可以显示原字符串，不转义\\反斜杠')
print('字符串' '可以有' '简单的运算' '级联')
print('字符串'+'用+号连接')
print(' 字符串'*3, '用*号重复')
print('字符串不可改变'+'字符串可以截取'[-4:]+r' 变量[头下标:尾下标:步长] 负数为倒数')

if True:
    print("python的缩进很关键")
else:
    print \
        (r"python的一条语句跨行时使用\反斜杠放在行尾来实现")


import keyword
print("\npython保留字 ", keyword.kwlist)

print("\npython的数字类型有四个 \nint 1 2 3\nbool True False\nfloat 1.23 3E-2\ncomplex 1+2j 1.1+2.2j")

'''

注意安装GIT
准备github账号密码
pycharm中VCS-import into version control-share project on github 
VCS中的commit和update是和本地git交互的
VCS中Git-Pull Push是和远程github交互的
'''