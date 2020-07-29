import socket

host='localhost'
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print('server listening on port',port)
c,addr = s.accept()

print('connection from',str(addr))

c.send(b'Hello how are u')
c.send('bye'.encode())
c.close()