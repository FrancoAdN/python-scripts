import socket

def main():
    site = 'dlptest.com'
    port = 21
    try:
        sock = socket.socket()
        sock.connect((site, port))
        banner = sock.recv(1024)
        print(banner)
    except:
        print('Could not connect to socket')

if __name__ == "__main__":
    main()