#coding:utf-8
# part 1 读文件——r只读
f = open('/Users/quyi/PycharmProjects/pythonLearn/test.txt', 'r')
s = f.read()
print '一下子全部读光：'
print s
if f:
    print 'closing IO'
    f.close()

f = open('/Users/quyi/PycharmProjects/pythonLearn/test.txt', 'r')
print '一行一行的读：'
for line in f.readlines():
    print line.strip()  #把末尾的'\n'删掉

# part 2 写文件——w可写
f = open('/Users/quyi/PycharmProjects/pythonLearn/test.txt', 'w')
f.write('Hello, world!\n')
f.close()

# part 3 写追加——a追加
f = open('/Users/quyi/PycharmProjects/pythonLearn/test.txt', 'a')
f.write('quyi, Hello, world!')
f.close()

# part 3——————在python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
with open('/Users/quyi/PycharmProjects/pythonLearn/test.txt', 'r') as f:
    for line in f.readlines():
        print line.strip()  # 把末尾的'\n'删掉

with open('/Users/quyi/PycharmProjects/pythonLearn/test.txt', 'w') as f:
    f.write('Hello, world!\n')