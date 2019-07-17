# python中的*号

传递实参和定义形参的时候，可以使用两个特殊的语法：'*''**'

- 实参：调用函数时传入的参数

- 形参：定义函数时传入的参数

1. 传递实参时使用

   

   ```python
   test(*args)
   ```

    *的作用其实就是把序列args中的每个元素，当作位置参数传进去。如果

   ```python
   args = (1,2,3)
   ```

   则上述代码等价于

   ```python
   test(1,2,3)
   ```

   ```python
   test(**kwargs)
   ```

   **的作用是把字典kwargs变成关键字参数传递。如果

   ```python
   **kwargs = {'a':1,'b':2,'c',3}
   ```

   则以上代码等价于

   ```python
   test(a=1,b=2,c=3)
   ```

   

2. 定义形参时使用

   

   ```python
   def test(*args):
   ```

   在上述代码中，表示将之后传进来的实参都装在元组args中，在函数中调用的话，直接

   ```python
   arg[i]
   ```

   同理，如果是

   ```python
   def test(**kwargs):
   ```

   表示之后传进来的实参都装在字典kwargs中

   案例：

   ```python
   def test(**kwargs):
       print(kwargs)
       for i in kwargs.keys():
           print(i)
   test(a=1, b=2)
   ```

   运行结果是

   ```
   {'a': 1, 'b': 2}
   a
   b
   ```

   

