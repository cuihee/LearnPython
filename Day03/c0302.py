
l1 = ['123', 456, [789]]
for i in l1:
    if isinstance(i, int):
        print(i)
        break
    print(i)

for i in range(10):
    print(i)


for i in range(10, 20, 3):
    print(i, end=",")

# 也可以是负数 开始 结束 步长

print()
print(list(range(5)))

# 循环中的else 是循环条件为false时运行，break时不运行哦
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
