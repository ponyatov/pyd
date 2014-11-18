import cfg
import socket

sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket', sockServer
print 'connect', sockServer.connect((cfg.SERVER, cfg.PORT))
Request = 'sockServer.close()'
print 'R:%s' % Request
sockServer.sendall(Request)
print 'A:%s' % sockServer.recv(0x10000)
sockServer.close()

raw_input('.')
