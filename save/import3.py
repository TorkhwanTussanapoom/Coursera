import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))

mysocket.'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.1\r\nHost: www.pythonlearn.com\r\n\r\n'.encode()

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysocket.close()
