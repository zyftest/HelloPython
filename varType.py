# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print (counter)
print (miles)
print (name)
a = b = c = 1
print (a,b ,c)
a, b, c = 1, 2, "john"
print (a,b ,c)

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # 输出完整列表
print(list[0] ) # 输出列表的第一个元素
print(list[1:3] ) # 输出第二个至第三个元素
print(list[2:] ) # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2 ) # 输出列表两次
print(list + tinylist ) # 打印组合的列表
# 元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用


#  字典 = map ?
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
"""
print(int())  # int method default zero
print(int('13'))
print(oct(10))  # 8进制转换
print(ord('A')) # char  对于8位的ASCII字符串
print(hex(10))  # 16进制转换