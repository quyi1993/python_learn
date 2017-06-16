#coding:utf-8

import os
import os.path
#part 1 获取一些系统信息
print os.name   #操作系统名字
print os.uname()    #详细的系统信息
print os.environ    #环境变量
print os.getenv('PATH')     #某个环境变量的值

#part 2 操作文件和目录
currentDir =  os.path.abspath('.')
targetDir = 'testDir'
absPathOfDir = os.path.join(currentDir, targetDir)
if(os.path.isdir(absPathOfDir) or os.path.exists(absPathOfDir)):
    os.rmdir(absPathOfDir)
os.mkdir(absPathOfDir)
os.rmdir(absPathOfDir)