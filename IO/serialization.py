#coding:utf-8
try:
    import cPickle as pickle
except ImportError:
    import pickle
import json

d = dict(name='Bob', age=20, score=88)
#python语言特定的序列化模块是pickle和cpickle，
# 但是如果想要把序列化搞得通用，更符合web标准，就可以使用json模块
#方法一 cPickle和pickle
pickle.dumps(d)

with open('dump.txt','wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print d

#方法二 JSON
json_str = json.dumps(d)
d = json.loads(json_str)
print isinstance(json_str, str), isinstance(d, dict)

#方法三 JSON进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
stu_str = json.dumps(s, default=student2dict)
stu_dict = json.loads(stu_str)
for k,v in stu_dict.items():
    print k, v

def dict2stuent(d):
    return Student(d['name'], d['age'], d['score'])

stu = dict2stuent(stu_dict)
print stu.score, stu.age, stu.score