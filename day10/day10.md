# 20190531
python默认的GUI开发模块是tkinter
但是不是最新和最好的选择，也没有功能特别强大的GUI空间
开发GUI的话，wxPython、PyQt、PyGTK等模块都是不错的选择

## tkinter
需要5步
1. 导入tkinter模块中我们需要的东西。
2. 创建一个顶层窗口对象并用它来承载整个GUI应用。
3. 在顶层窗口对象上添加GUI组件。
4. 通过代码将这些GUI组件的功能组织起来。
5. 进入主事件循环(main loop)。

不要用tkinter作为文件名啊。。。不然会报错：module 'tkinter' has no attribute 'messagebox'