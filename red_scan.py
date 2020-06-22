import nmap

def main():
    nm = nmap.PortScanner()
    ip = '127.0.0.1'
    nm.scan(hosts=ip, arguments='--top-ports 1000 -sV --version-intensity 3')
    print('Command: {}'.format(nm.command_line()))
    print('Used protocols: {}'.format(nm[ip].all_protocols()))
    print('Machine state: {}'.format(nm[ip].state()))

    tcp = nm[ip]['tcp']
    for port in tcp.keys():
        print('\')
        print(port)
        for data in tcp[port]:
            print('{}: {}'.format(data, tcp[port][data]))



if __name__ == '__main__':
    main()
    