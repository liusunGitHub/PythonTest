import socket,time,random,threading

#将接受或者发送信息封装到一个函数中。
def setResponse(sock,address):
    print('%s:%s is connecte'%(address))
    random_list = [random.randrange(1,1000) for i in range(5)]
    for i in random_list:
        recv = sock.recv(521).decode()
        print(recv)
        #向客户端发送信息
        sock.send(str(i).encode())
        time.sleep(2)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',9000))
sock.listen(5)
#死循环，开启线程
while True:
    client,address =sock.accept()
    t = threading.Thread(target=setResponse,args=(client,address))
    t.start()
#关闭套接字
sock.close()





