#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

import sys

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

print("按下 enter 键退出，其他任意键显示...\n")

print (sys.argv)
days = ['Monday', 'Tuesday', 'Wednesday',  #数组
        'Thursday', 'Friday']

s = 'ilovepython'
print (s[1:5] * 2)
x="a"
y="b"
# 换行输出
print('---------')
print (x)
print (y)

if 1 > 2 :
    print ("Answer"),
    print("true")
else :
    print ("Answer")

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。

包含了多个语句"""