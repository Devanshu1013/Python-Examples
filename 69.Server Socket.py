import socket

s = socket.socket()
print("Created")

s.bind(('localhost',9999))

s.listen(3)
print('waiting for client')

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()

    print("Connected",addr,name)

    c.send(bytes('welcome','utf-8'))

    c.close()