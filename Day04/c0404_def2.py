# 不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 不定长部分是元组
printinfo( 70, 60, 50 )


def printinfo2( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 不定长部分是字典
printinfo2(1, a=2,b=3)


def f(a,b,*,c):
    return a+b+c
# 星号 * 后的参数必须用关键字传入
print(f(1,2,c=3))


sum = lambda arg1, arg2: arg1 + arg2
# 调用lambda函数
print ("arg1 + arg2 =", sum( 10, 20 ))

# return 语句用于退出函数