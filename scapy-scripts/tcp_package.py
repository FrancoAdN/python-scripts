from scapy.all import *


def main():
    ip_layer = IP(dst="192.168.0.11", src="172.217.172.78")
    tcp_layer = TCP()
    message = Raw(load="Package message")
    final = [ip_layer/tcp_layer/message for x in range(0, 1000)]
    send(final, verbose=False)
    print("Message sent")


if __name__ == "__main__":
    main()