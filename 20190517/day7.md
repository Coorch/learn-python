# 20190517
昨天太浪了，忘记这个项目了。。。
今天出了长门，255抽怼出来了

## day7 字符串和常用数据结构

### 使用字符串
Python表示文本信息的方式就是字符串类型，由零个或多个字符组成的有限序列
#### 基本操作
```Python
# 通过len函数计算字符串的长度
print(len(str1)) #13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))

str3 = '   jackfrued@126.com '
print(str3)
# 裁剪空格
print(str3.strip())#'jackfrued@126.com'

str2 = 'abc123456'
# 从字符串中取出指定位置的字符（下标计算）
print(str2[2]) # c
# 检查字符串是否以数字构成
print(str2.isdigit()) # False
# 检查字符串是否以字母构成
print(str2.isalpha()) # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum()) # True
# 字符串切片（从指定的开始索引到指定的结束索引）
```
#### 正则相关操作，查找特定字符
```Python
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1即不存在该子串
# 与find类似但找不到子串时会引发异常
print(str1.index('or')) # 8
#print(str1.index('shit')) # substring not found
# 检查字符串是否以指定的子串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
```
#### 切片
```Python
str2 = 'abc123456'   
print(str2[2:5]) #c12
print(str2[2:])# c123456
print(str2[2::2])# c246
print(str2[::2])# ac246
print(str2[::-1])# 654321cba
print(str2[-3:-1])# 45
```
- 第一个数字表示start，包含该位置处的字符
- 位置从0开始计算
- 如果下标是负数，考虑第一个字符是0，则最后一个字符是-1，倒数第二个字符就是-2，以此类推
- 如果在::后接数字，代表step步长；
- 如果是:后接数字，则代表end，但是不包含end位置处的字符

### 使用列表
字符串可以看作是特殊的列表
#### 基本操作
```Python
# 添加元素
list1.append(200)#[1,3,300,7,100,200]
list1.insert(1, 400)#[1,400,3,300,7,100,200]
list1 += [1000, 2000] #[1,400,3,300,7,100,200,1000,2000]
print(list1)
print(len(list1))#9
#删除元素
list1.remove(3)#[1,400,300,7,100,200,1000,2000]
del list1[0] #[400,300,7,100,200,1000,2000]
print(list1)
#清空
list1.clear()
print(list1)

list2 = ['hello'] * 5
print(list2) #['hello','hello','hello','hello','hello']
```
- list可以相加，也可以乘以1个正整数

#### 切片和复制
切片与字符串完全相同
##### 复制
```Python
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
#fruit3 = fruits  # 没有复制列表只创建了新的引用
#fruits.append(1)
#print(fruit3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango', 1]
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)
```
- 直接列表等于列表似乎只是把地址交出去了，浅拷贝
- 利用完整切片来复制就是深拷贝

#### 排序
可用sorted(list)函数以及list.sort()
前者不改变list，后者则会改变list，二者参数相同
- reverse=True 从大到小排序，默认为False，即从小到大
- key = len 指定排序规则为字符串长度，默认是首字母在字母表的顺序

#### 生成表达式
```Python
    # 列表生成表达式
    f = [x for x in range(1, 10)]
    print(f) # [1,2,3,4,5,6,7,8,9]
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f) #[A1,A2,A3,A4..,B1,B2 ...,E6,E7]
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 10)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数192
    print(f)#[1,4,9,16,25,36,49,64,81]
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 10))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间120
    print(f)#<generator object main.<locals>.<genexpr> at 0x000002AB0B794480>
    for val in f:
        print(val)
```
- 表达式用小括号，得到的是一个生成器
- 生成器占用内存更小,但是取其中数据没有中括号方便

### 元组
- 与列表类似，只是元组的元素一经定义便不能修改
- 在多线程环境中可能更喜欢使用那些不变对象
- 元组在创建时间和占用的空间上面都优于列表

### 集合
与数学上的集合一致，不允许有重复元素，并且可以进行交集、并集、差集等运算
定义的时候出现重复元素会自动剔除
```Python
set1 = {1, 2, 3, 3, 3, 2}
print(set1)#{1,2,3}重复元素被剔除
```

### 字典
类似字典，可以存储任意类型对象，每个元素都是由一个键和一个值组成的键值对
，键和值通过冒号分开
```Python
def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
```