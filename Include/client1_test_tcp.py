'''
客户端,计算奇偶性
'''
import socket, time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 9000))

recv_num = ""#接收服务器的数字
send_msg = ""#计算数字后，发送给服务器的消息
while True:
    if recv_num == "":
        send_msg = "我是客户端1".encode();
    else:
        print("服务器发过来的数字：" + str(recv_num))
        if int(str(recv_num)) % 2 == 0 :#数字为偶数,返回False
            send_msg = str(recv_num).encode()+" False".encode();
        else:#奇数返回True
            send_msg = str(recv_num).encode()+" True".encode();
    sock.send(send_msg)
    time.sleep(2)
    print(send_msg)
    recv_num = sock.recv(521).decode()

sock.close()
