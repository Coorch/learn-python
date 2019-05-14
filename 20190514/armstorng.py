'''
寻找水仙花数
三位数
各位的三次幂的和等于该数
'''

for i in range(100, 1000):
    m = i // 100 # 百位
    j = i % 10 # 个位
    n = int((i - 100 * m) / 10)
    if m*m*m + j*j*j + n*n*n == i:
        print('%d是水仙花数'%i)

'''
寻找0-9999间的完美数
真因子（不是本身的因子）之和等于本身的数
'''
import time
start = time.process_time()
for i in range(10000):
    sum = 0 # 记录真因子之和
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print('%d是完美数'%i)
end = time.process_time()
print('用时：%f'%(end-start))

from math import sqrt
start = time.process_time()
for i in range(10000):
    sum = 0 # 记录真因子之和
    for j in range(1, int(sqrt(i)) + 1):
        if i % j == 0 and i != j:
            sum += j
            if j > 1 and i / j != j:
                sum += i / j
    if sum == i:
        print('%d是完美数'%i)
end = time.process_time()
print('用时：%f秒'%(end-start))
# 可以发现下面的算法用时短得多，因为循环次数大大减少，循环次数越大，越占优势

# 百钱百鸡问题
for x in range(21):
    for y in range(101 - x):
        if (5 * x + 3 * y + (100 - x - y) / 3) == 100:
            print('鸡公%d，鸡婆%d，鸡雏%d'%(x, y, (100-x-y)))

# 斐波那契数列
a = 1
print(a)
b = 1
print(b)
while True:
    a = a + b
    b = a + b
    print(a)
    print(b)
    if b > 100:
        break

# craps赌博游戏