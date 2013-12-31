__author__ = 'hadoop'

import socket

s=socket.socket()

host=socket.gethostname()
print host
port=1234

s.bind((host,port))
s.listen(5)
i=1
print 'i=',i

while True:
    (c,addr) = s.accept()
    print 'get connection from',addr
    c.send("Thank you for connection")
    c.close()
    print i+1
    if i==10 :
        break



