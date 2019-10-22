
# 一行注释 注意缩进
if True:
    print("python的缩进很关键")
else:
    print \
        (r"python的一条语句跨行时使用\反斜杠放在行尾来实现")


"""
多行注释
方式一

注意安装GIT
准备github账号密码
pycharm中VCS-import into version control-share project on github 
VCS中的commit和update是和本地git交互的
VCS中Git-Pull Push是和远程github交互的
"""

'''
多行注释
方式二
'''

import keyword
print("\npython保留字 ", keyword.kwlist)

print("\npython的数字类型有四个 \nint 1 2 3\nbool True False\nfloat 1.23 3E-2\ncomplex 1+2j 1.1+2.2j")

