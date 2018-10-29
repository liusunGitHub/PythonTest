#coding=utf-8

#导入包
import socket,time,random,threading

numCount = 30;#用来计算的随机数的总数

#列表需要(31)随机数用来接收第30个元素的计算消息
random_list = [random.randrange(1, 1000) for i in range(numCount+1)]

#接受或者发送信息的函数
def setResponse(sock,addresss):
    for i in random_list:
        recv_msg = sock.recv(521).decode()
        print(recv_msg)
        #向客户端发送信息
        sock.send(str(i).encode())
        time.sleep(2)

#创建套接字
_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_sock.bind(('',9000))
_sock.listen(5)
#死循环，开启线程
while True:
    client,address =_sock.accept()
    t = threading.Thread(target=setResponse,args=(client,address))
    t.start()
#关闭套接字
_sock.close()





