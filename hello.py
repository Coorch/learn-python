"""
第一个Python程序 - hello,world！
向伟大的Dennis M.Ritchie先生致敬

version：0.1
Author：蔡金航
"""

import sys

print(sys.version)
print(sys.version_info)

print("hello,world!")
print('你好', '世界')
print('hello', 'world', sep=', ', end='!')
print('goodbye, world', end='!\n')

import this

import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()