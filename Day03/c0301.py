# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
from random import random, randint

a, b = 0, 1
while b < 10:
    print(b, end=",")
    a, b = b, a + b
print()
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)

number = randint(0, 10)
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')


