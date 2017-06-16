#coding:utf-8
# 导入:
from sqlalchemy import Column, String, create_engine, INTEGER, Enum, TEXT, BOOLEAN, DATETIME
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import *

Base = declarative_base()
class student(Base):
    __tablename__ = 'student'
    stu_no = Column(INTEGER, primary_key=True)
    stu_name = Column(String(50), nullable=False)
    sex = Column(String(3), nullable=False)
    time = Column(DATETIME)
    isLegal =  Column(INTEGER)
    info = Column(TEXT)

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
session.query(student).filter(student.stu_no == 123456).delete()
session.commit()
new_stu = student(stu_no=123456, stu_name='Bob', sex='男', time=datetime.today(), isLegal = 1, info = 'info info info')
session.add(new_stu)
session.query(student).filter(student.stu_no == 1).delete()
session.commit()
new_stu = student(stu_no=1, stu_name='Mary', sex='女', time=datetime.today(), isLegal = 1, info = 'info info info')
session.add(new_stu)
session.query(student).filter(student.stu_no == 2).delete()
session.commit()
new_stu = student(stu_no=2, stu_name='john', sex='男', time=datetime.today(), isLegal = 1, info = 'info info info')
session.add(new_stu)
session.query(student).filter(student.stu_no == 3).delete()
session.commit()
new_stu = student(stu_no=3, stu_name='lily', sex='女', time=datetime.today(), isLegal = 0, info = 'info info info')
session.query(student).filter(student.stu_no == 4).delete()
session.add(new_stu)
session.commit()
new_stu = student(stu_no=4, stu_name='david', sex='男', time=datetime.today(), isLegal = 0, info = 'info info info')
session.add(new_stu)
session.commit()


for stu in session.query(student).filter(student.sex=='女', student.isLegal==1).all():
    print stu.stu_no, stu.stu_name

# 关闭session:
session.close()