"""
猜数字游戏
计算机给出一个1~100间的随机数让人猜
计算机根据猜的数字给出提示，大一点还是小一点

"""
import random
'''
answer = random.randint(1, 100)
guess = int(input('请输入1-100的整数'))
count = 0 # 用于计数猜的次数，按照折半查找的思想，只需log(2)100次即可猜出，即小于7次
while guess != answer:
    count += 1
    if guess < answer:
        guess = int(input('请输入大一点的数：'))
    else:
        guess = int(input('请输入小一点的数：'))
print('恭喜你，猜对了！')
if count > 7:
    print('你的智商已欠费')

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d'%(j, i, i * j), end='\t')
    print('')


# 输入一个数判断是否是素数
import math

n = int(input('请输入自然数：'))
end = int(math.sqrt(n))
flag = True
for i in range(2, end + 1):
    if n % i == 0:
        flag = False
        
        break
if flag and n != 1:
    print('%d是素数'%n)
else:
    print('%d不是素数'%n)

# 输入两个正整数，计算最大公约数和最小公倍数

x = int(input('请输入正整数：'))
y = int(input("请输入正整数："))
m = 1 #最大公约数
n = x * y #最小公倍数
for i in range(1, x + 1):
    if i > y:
        break
    if x % i == 0 and y % i ==0:
        m = i
n = n / m
print('最大公约数%d'%m)
print('最下公倍数%d'%n)
'''
# 打印三角形图案
n = int(input('请输入行数：'))
for i in range(n):
    for j in range(i + 1):
        print('*', end= '')
    print()

for i in range(n):
    for j in range(n-1, -1, -1):
        #print(j)
        if j > i:
            print(' ', end = '')
        else:
            print('*', end = '')
    print("")

for i in range(n):
    for j in range(1, 2 * n):
        if (n - i - 1) < j and j < (n + i + 1):
            print('*', end='')
        else:
            print(' ', end='')
    print() 