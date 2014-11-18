import cfg
import socket,time,sys

print time.localtime()[:6],sys.argv

sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print time.localtime()[:6],'socket', sockServer
print time.localtime()[:6],'bind', sockServer.bind((cfg.HOST, cfg.PORT))

sockServer.listen(1)
while 1:
    print
    sockClient, (ClientIP, ClientPort) = sockServer.accept()
    print time.localtime()[:6],ClientIP, ClientPort,
    if ClientIP in cfg.ALLOWED:
        print 'ALLOWED'
        Request = sockClient.recv(0x10000)
        print time.localtime()[:6],'R:%s'%Request
        try:
            Answer = str(eval(Request))
        except:
            Answer = str(Exception)
        print time.localtime()[:6],'A:%s'%Answer
        sockClient.sendall(Answer)
    else:
        print 'REJECTED'
        sockClient.sendall('REJECTED')
    sockClient.close() 

sockServer.close()

raw_input('.')
