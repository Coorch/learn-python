# 求排列组合Cmn
def factorial(num): #阶乘
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

# 最大公约数
def gcd(x, y):
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if y % i == 0 and x % i == 0:
            return i
print(gcd(27, 18))

# 最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)
print(lcm(27, 18))

# 判断是否为回文数
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10
    if total == num:
        print('%d是回文数'%num)
    else:
        print('%d不是回文数'%num)
is_palindrome(989)

def foo():
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    
    bar()
    # print(c) # NameError:name'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b) #NameError:name'b' is not defined
    foo()