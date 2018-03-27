# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 例：elif用法

num = 5
if num == 3:  # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print('roadman')  # 条件均不成立时输出

flag = False
name = 'luren'
if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print('welcome boss')  # 并输出欢迎信息
else:
    print(name)  # 条件不成立时输出变量名称

# 短路计算 代码bu报错：
a = 0
b = 1
if (a > 0) and (b / a > 2):
    print("yes")
else:
    print("no")

# 而下面的代码就会报错：

a = 1
b = 3
if (a > 1) or (b / 1 > 2):
    print("yes")
else:
    print("no")

# 一个简单的条件循环语句实现汉诺塔问题

def my_print(args):
    print(args)


def move(n, a, b, c):
    my_print((a, '-->', c)) if n == 1 else (move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))


move(3, 'a', 'b', 'c')


