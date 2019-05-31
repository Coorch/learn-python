'''
Author = corch
'''
# 用户身份验证
username = input('请输入用户名:')
import getpass
password = getpass.getpass('请输入用户名:')#使密码不在终端显示

if username == 'corch' and password == '123456':
    print('用户身份验证成功')
else:
    print('用户身份验证失败')

'''
分段函数求值
       3x - 5 (x > 1)
f(x) = x + 2  (-1 <= x <= 1)
       5x + 3 (x < -1)
'''
x = float(input('请输入x:'))
if x < -1:
    f = 5 * x + 3
    print('f(x)的值为：%d'%f)
elif x > 1:
    f = 3 * x - 5
    print('f(x)的值为: %d'%f)
else:
    f = x + 2
    print('f(x)的值为：%d'%f)

"""
英制单位英寸与公制单位厘米互换
1英寸=2.54厘米
"""
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.2f 英寸 = %.2f 厘米'%(value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f 厘米 = %.2f 英寸'%(value, value / 2.54))
else:
    print("请输入正确的单位")

'''
输入三角形的三条边求周长和面积
面积用海伦公式
'''
import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and b + c > a:
    print('周长为%f'%(a + b + c))
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积为%f'%S)
else:
    print('不能构成三角形')