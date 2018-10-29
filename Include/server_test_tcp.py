# coding=utf-8

# 导入包
import socket, time, random, threading

numCount = 30;  # 用来计算的随机数的总数

# 通过推导式，生产31个随机数，其中前30个数字发送给客户端，并返回30计算后的数字，最后一个只是用来显示第30个数的计算结果
random_list = [random.randrange(1, 1000) for i in range(numCount + 1)]


# 接受或者发送信息的函数
def msgResponse(sock, addresss):
    print('%s:%s is connected' % (addresss))
    # 循环31次给客户端发31个数，最后一个数不会返回服务器，--因为客户端要先发个消息，第一次接收的消息不是计算的数字
    for i in random_list:
        recv_msg = sock.recv(521).decode()  # 服务器先接收客户端的会话
        print(recv_msg)  # 显示客户端发的消息
        # 向客户端发送数字，字符串的形式，encode()
        sock.send(str(i).encode())
        time.sleep(2)


# 创建套接字
_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
_sock.bind(('', 9000))

# 监听端口
_sock.listen(5)

# 死循环，开启线程
while True:
    client, address = _sock.accept()
    t = threading.Thread(target=msgResponse, args=(client, address))
    t.start()

# 关闭套接字
_sock.close()
