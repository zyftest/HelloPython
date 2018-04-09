"""

def 关键词开头，

 后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式]
结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回
None。
"""

def addFunction(a,b):
   "函数_文档字符串"
   print('in function,param:%s + %s' %(a,b))
   return a+b


def printme(str):
   "打印传入的字符串到标准显示设备上"
   print(str)
   return


printme(addFunction(1,2))