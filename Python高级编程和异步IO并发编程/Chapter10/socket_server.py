import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024).decode('utf8')
        if data == 'break':
            print('over')
            break
        print(data)
        re_data = input()
        sock.send(re_data.encode('utf8'))


while True:
    sock, addr = server.accept()

    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024).decode('utf8')
    # if data == 'break':
    #     print('over')
    #     break
    # print(data)
    # re_data = input()
    # sock.send(re_data.encode('utf8'))
sock.close()
server.close()