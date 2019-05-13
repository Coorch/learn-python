# 20190513
下午刚回本部宿舍，住了3年的宿舍确实是舒服的

## day4
循环结构
轻松控制某件事或者某些事重复发生
### for-in循环
计算从1加到100
```python
sum = 0
for i in range(101):
    sum = sum + i
```
range可以用来产生一个不变的数值序列，且这个序列通常用于循环
- range(101)产生0-100的整数序列
- range(1,100)产生1-99的整数数列
- range(1, 100, 2)产生1-99的奇数数列，2是步长
- range(start, end, step)产生的数列包含start，但是不包含end，比如range(5, 0, -1)产生的是5,4,3,2,1

### while循环
如果要构造不知道具体循环次数的循环结构，使用while循环。其通过一个能够产生或转换出bool值得表达式来控制循环，表达式为FALSE时循环才结束
```python
"""
猜数字游戏
计算机给出一个1~100间的随机数让人猜
计算机根据猜的数字给出提示，大一点还是小一点

"""
import random

answer = random.randint(1, 100)
guess = int(input('请输入1-100的整数'))
while guess != answer:
    if guess < answer:
        guess = int(input('请输入大一点的数：'))
    else:
        guess = int(input('请输入小一点的数：'))
print('恭喜你，猜对了！')
```
- break关键字可以提前终止循环
- continue关键字这是放弃执行本次循环的后续代码，直接进入下一轮循环
循环也可以嵌套