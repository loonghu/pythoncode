# -*- coding: latin-1 -*-
__author__ = "Jake.liu (heidsoftg@gmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2013/10/21 $"
__copyright__ = "Copyright (c) 2013 heidsoft"
__license__ = "Python"


import sys

#将heidsoft.py 加入到系统python中
sys.path.append("D:\Documents\Github\pythoncode\workpace_python\heidsoft.py")

import heidsoft

print heidsoft.fib(123)

print __name__

if __name__=='__main__':
    print 'this is main programe'

print heidsoft.__name__

