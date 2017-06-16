#coding:utf-8
import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    #assert的意思是，表达式n!=0应该是true，否则后面的代码就会出错
    #如果断言失败，assert语句本身就会抛出AssertionError
    assert n!=0, 'n is zero'
    return 10 / n

def foo2(s):
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print 10 / n

if __name__ == '__main__':
    foo2('0')