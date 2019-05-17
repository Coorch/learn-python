import sys

def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1) # [1,3,5,7,100]
    list2 = ['hello'] * 5
    print(list2) #['hello','hello','hello','hello','hello']
    # 计算列表长度，即元素个数
    print(len(list1))#5
    # 下标索引
    print(list1[0])#1
    print(list1[-1])# 100
    print(list1[4])# 100
    print(list1[-3]) # 5
    # print(list1[5]) # IndexError:list index out of range
    list1[2] = 300
    print(list1) #[1,3,300,7,100]
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

    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表
    for fruit in fruits:
        print(fruit.title(), end=' ')#Grape Apple Strawberry Waxberry Pitaya Pear Mango
    print()
    # 列表切片
    fruits2 = fruits[1:4] #['apple', 'strawberry', 'waxberry']
    print(fruits2)
    #fruit3 = fruits  # 没有复制列表只创建了新的引用
    #fruits.append(1)
    #print(fruit3)#['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango', 1]
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1] #['pitaya', 'pear']
    print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)

    # 排序
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)# ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    print(list2)# ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
    print(list3)# ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
    print(list4)# ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True) #reverse为True表示从大到小排序
    print(list1)# ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']        

    # 列表生成表达式
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 10)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 10))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


if __name__ == '__main__':
    main()
