#coding:utf-8
import os
#path = os.getcwd()os.path.realpath(__file__)
path = os.path.dirname(os.path.realpath(__file__))
#path = raw_input('输入文件路径：')
import plistlib
listdir = os.listdir(path)
# print listdir
for dic in listdir:
    if os.path.splitext(dic)[1] == '.png' and os.path.splitext(dic)[0] != 'logo':
        print dic




