import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
cmd = 'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
PARAMS = {'address':location}
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
