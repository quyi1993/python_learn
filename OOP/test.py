class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


quyi = Student("quyi",12,100)
print quyi.name,quyi.age,quyi.score


dict = {"quyi" : None, "bob":19, "mary":"great"}
value = dict.get("quyi")
print value
for k,v in dict.items():
    print k,v