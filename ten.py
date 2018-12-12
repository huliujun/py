# -*- coding: utf8 -*-
'''
学习一下
python 大法
'''
## 简单讲讲print（这是注释）
#
print '----------------简单讲讲print--------------------'
print 1234

print '你好，"世界" ！';
print "你好，'世界' ！"

print '''你好，

世界！'''

# 简单讲讲 变量
print '----------------简单讲讲变量--------------------'

a = 1
A = 1.1
b = 'b'

c, d, e = 1, 1.1, 'b'

print a, A, b
print type(a), type(A), type(b)
# 列表（可更新）、元组（不可更新）、字典（可更新）
List = [1, 2, 3, 4]
Tuple = (1, 2, 3, 4)
Dict = {'a': 1, 'b': 2, 'c': '3'}
List.append(5)
print List, List[0], Dict['b']

# 运算符略

# 条件语句
print '----------------简单讲讲条件语句--------------------'

if a == 1:
    print '条件正确'
else:
    print '不符合条件'
# 循环语句
print '----------------简单讲讲循环语句--------------------'

    # 循环列表
for i in List:
    print i
    # 循环字典
for key in Dict:
    print key + '->' + str(Dict[key])
    # while循环

while (a < 4):
    print 'The count is:', a
    a += 1
print "Good bye!"


# 函数
print '----------------简单讲讲函数--------------------'

def Print(str):
    print str

Print('函数就是这么简单')


# 方法
print '----------------简单讲讲方法--------------------'

class PRINT:
    def __init__(self, a=''):
        self.a = a

    def printlower(self, str):
        print self.a + str.lower()

    def printupper(self, str):
        print self.a + str.upper()


P = PRINT()
P.printlower('nihao shijie')
P.printupper('nihao shijie')

P2 = PRINT('print:')
P2.printlower('nihao shijie')
P2.printupper('nihao shijie')
