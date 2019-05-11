'''
使用变量保存数据并进行算术运算

Version:0.1
Author:corch
'''

a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(bool(a))
print(complex(a))
print(str(a))

'''
使用input输入
使用int（）进行类型转换
用占位符格式化输出的字符串
'''

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))

#用type检查变量的类型
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''
运算符的使用
'''
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 1 > 2
flag2 = 1 < 2
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print('flag1:', flag1)
print('flag2:', flag2)
print('flag1 and flag2', flag3)
print('flag1 or flag2', flag4)
print('not flag1:'+str(flag5))

'''
将华氏温度转换为摄氏温度
F = 1.8C + 32
'''
C = float(input('请输入华氏温度：'))
F = 1.8 * C + 32
print('%.1f华氏度 = %.1f摄氏度'%(C,F))

'''
输入半径求圆的周长和面积
'''
import math
r = float(input('请输入圆的半径：'))
S = math.pi * r * r
L = 2 * math.pi * r
print('圆的周长为%f'%L)
print('圆的面积为%f'%S)

'''
判断输入年份是不是闰年
闰年能被4整除，不能被100整除，或者被400整除
'''
year = int(input('请输入年份：'))
run = (year % 4 == 0 and year % 100 != 0 
       or year % 400 == 0)
if run:
    print('%d年是闰年'%year)
else:
    print('%d年不是闰年'%year) 