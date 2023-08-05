# Author   :   atg
# coding=utf-8
# Time     ：2023/8/3 10:40

import socket

def client():
    # 创建套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket = ('127.0.0.1', 12345)
    client_data = input('请输入：')
    client_socket.sendto(client_data.encode('utf-8'),server_socket)

    print('发送成功')
    client_socket.close()


client()