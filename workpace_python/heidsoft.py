# -*- coding: latin-1 -*-
__author__ = "Jake.liu (heidsoftg@gmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2013/10/21 $"
__copyright__ = "Copyright (c) 2013 heidsoft"
__license__ = "Python"

import sys

#将heidsoft.py 加入到系统python中
sys.path.append("D:\Documents\Githubpythoncode\workpace_python\heidsoft.py")

names=['zhansan','wangwu','zhaoliu','heidsoft']
ages=[12,23,44,23]


for i in range(len(names)):
    print names[i], 'is', ages[i],'years old'

print zip(names,ages)

for name,age in zip(names,ages):
    print name, 'is', age, 'years'

for n in range(2,10):
    for x in range(2,n):
        if n % x==0:
            print n,'equals',x,'*',n/x
            break
        else:
            #loop
            print n,'is a prime number'





print "The Python Path is",sys.path

def callSysArgv():
    for ARGV in sys.argv:
        print ARGV

def fib(n):
    print 'n=',n
    if n >1:
        return n*fib(n-1)
    else:
        print 'end of the line'
        return 1

def hello(tmp):
        print tmp

hello(123)

#转为小写
print 'AAABBB'.lower();

#f=open(r'D:\\Documents\\GitHub\\pythoncode\\workpace_python\\heidsoft_network_client.py')

f=open('writefile.txt','w')
f.write('aaaaaaaaa')


from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):#继承
    def __init__(self,html):
        print html
    def handle_starttag(self, tag, attrs):
        print "html start:",tag
    def handle_endtag(self, tag):
        print "html end:",tag
    def handle_data(self, data):
        print "html content:",data

parser=MyHTMLParser("haaaaaaaaaaaaaaaaaaaa")
parser.feed("<html><head><title>Test</title></head>"
            "<body><h1>Fock YOU</h1></body></html>")

def myFunction(functionName):
    print "this is my function %s"%functionName
myFunction('helloFunction')