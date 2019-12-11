import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("###############################################################\n\
#              写python代码之前需要做什么准备工作？              \n\
###############################################################")
print("环境配置可以参考 https://www.runoob.com/python3/python3-install.html")
print("也可以上官网看如何开始 https://www.python.org/ 不过需要好一点的网络环境不然会无法访问\n")

print("###############################################################\n\
#              在哪里写python代码？              \n\
###############################################################")
print("一般来讲，你正常下载了python解释器后。\n\
在开始菜单 Python 3.7中有一个IDLE(python 3.7 64bit) \n\
打开后是一个python 3.7.2 shell命令行 \n\
在这个命令行就可以写下python代码啦！\n\
这个命令行使用起来有一个明显的缺点——>难以保存代码。\n\
我们希望一个类似于记事本的编辑器。\n\
嘿嘿，还是这个命令行程序，左上角File按钮中New File就可以打开一个类似于记事本的编辑器了\n")

print("###############################################################\n\
#              如何运行自己的python代码？              \n\
###############################################################")
print("如果是在python命令行中写的代码，那么敲一个回车就可以运行啦，结果直接在命令行。\
    如果是使用命令行的new file写的代码，点击Run-run module（第一次需要保存文件）就可以运行啦，结果在命令行显示。\n")

print("###############################################################\n\
#              （可选的）学习了1+1=2如何快速进阶？              \n\
###############################################################")
print("菜鸟python3教程 https://www.runoob.com/python3/python3-tutorial.html ")
print("官方中文python3.8教程 https://docs.python.org/zh-cn/3.8/tutorial/index.html")
print("菜鸟Numpy教程 https://www.runoob.com/numpy/numpy-tutorial.html")
print("官方中文Numpy教程 https://www.numpy.org.cn/")
print("PyTorch中文手册 https://github.com/zergtant/pytorch-handbook")
print("PyTorch官方中文文档 https://pytorch-cn.readthedocs.io/zh/latest/ \n")

print("###############################################################\n\
#              学习完本节内容，应该知道哪些东西？              \n\
###############################################################")
print("1 代码中前3行代码是为了保证汉字的正常显示 ")
print("2 猜测print单词的含义，猜测\"的含义，猜测()的含义 ")
print("3 print中要打印的内容太长如何换行 ")
print("4 print中要打印换行符该怎么办 ")
