# coding=utf-8

'''
 客户端3,功能：计算数字 是否大于10
'''

# 导入包
import socket, time

# 接收服务器的数字
recv_num = ""
# 计算数字后，发送给服务器的消息
send_msg = ""
# 为了打印日志更好看
tag = "---------------------".encode()

# 创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器，9000为服务器端口号
sock.connect(("127.0.0.1", 9000))

# 循环发送接收消息，客户端先发消息
while True:
    if recv_num == "":
        send_msg = tag + "我是客户端3".encode();  # 客户端先发第一条消息通知服务器，准备接收消息
    else:
        print(recv_num)  # 打印服务器发送的数字
        if int(str(recv_num)) > 10:  # 接收到服务器的数字为偶数,发送给服务器的消息： 数字 False
            send_msg = tag + ">10 : False ".encode() + str(recv_num).encode()
        else:  # 接收到服务器的数字为偶数,发送给服务器的消息： 数字 True
            send_msg = tag + ">10 : True  ".encode() + str(recv_num).encode()
    sock.send(send_msg)  # 发送数据
    time.sleep(2)
    recv_num = sock.recv(521).decode()
# 关闭socket
sock.close()
