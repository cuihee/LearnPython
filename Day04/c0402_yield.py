
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)
 
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        pass

# 像是 yield a是a进栈的操作
# list_a = []
# list_a.append(a)
