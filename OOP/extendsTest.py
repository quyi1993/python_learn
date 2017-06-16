#-*- coding:utf-8 -*-
class Animal(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        print 'created instance for:',self.name
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    #重写__init__不会自动调用基类的__init__
    def __init__(self,name,sex,kind):
        #调用基类的方法1
        Animal.__init__(self,name,sex)
        #调用基类的方法2
        #使用super的好处在于：不需要明确给出任何基类名称.
        #如果改变了类继承关系，我们只需要改一行代码(class语句本身)而不必在大量代码中去查找所有被修改的那个类的名字。
        super(Dog, self).__init__(name,sex)
        self.kind = kind

    def run(self):
        Animal.run(self)
        super(Dog, self).run()
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog("wangcai",'male','tugou')
dog.run()
print dir(dog)
print "类的属性",Dog.__dict__
print "类的名字:",Dog.__name__,"类定义所在的模块：",Dog.__module__
print type(dog)