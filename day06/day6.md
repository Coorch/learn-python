# 20190515
没什么动力写毕业论文啊。沉迷于王牌进化无法自拔

## day6
函数与模块的使用

### 函数的作用
解决重复代码的问题

### 定义函数
def关键字

### 用模块管理函数
解决命名冲突问题。如在同一个py文件中定义了两个同名函数，Python中没有函数重载的概念，则后面定义会覆盖之前的定义
```Python
def foo():
    print('hello, world')
def foo():
    print('goodbye, world')
foo()
```
结果输出的是goodbye, world
#### Python中每个文件就代表了一个模块(module)，不同的模块中可以用同名函数，在使用函数的时候需要import关键字导入指定的模块
module1.py
```python
def foo():
    print('hello, world')
```
module2.py
```Python
def foo():
    print('goodbye, world')
```
test.py
```Python
from module1 import foo
foo()
from module2 import foo
foo()
```
也可以这样区分
test.py
```Python
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()
```

- 作用域
```python
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
```
上面代码能够顺利执行，且打印出1--和“hello”
a是全局变量，属于全局作用域；b是定义在函数中的局部变量，属于局部作用域，在函数外并不能访问到它；但是对于foo内部的函数bar来说，b输入嵌套作用域，在bar函数中可以访问；而内置作用域则是Python内置的隐含标识符min、len等等