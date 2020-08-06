from scapy.all import *
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-r', '--range', help='IP Range')
parse = parse.parse_args()

def ip_scan(ip):
    range_ip = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    final_pack = broadcast/range_ip
    res = srp(final_pack, timeout=2, verbose=False)[0]
    for n in res:
        print("[+]HOST: {}\t MAC: {}".format(n[1].psrc, n[1].hwsrc))
def main():
    if parse.range:
        ip_scan(parse.range)
    else:
        print('Especify range')
    

if __name__ == "__main__":
    main()