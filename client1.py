import socket

HOST = 'chitturi'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('chitturi', 50007))
s.sendall('Hi good morning')
data = s.recv(200)
s.close()
print 'Received', str(data)
