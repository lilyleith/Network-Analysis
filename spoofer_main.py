from scapy.all import *
import sys

# The send packet function should create a spoofed UDP packet with the payload and send it over to
# the destination IP and port specified

def send_packet(src_ip, dst_ip, dst_port, payload):
    if len(payload) > 150:
        return
    packet = IP(src = src_ip, dst = dst_ip) / UDP(dport = dst_port) / Raw(load = payload)
    send(packet)
    return packet

if __name__ == "__main__":
    
    if len(sys.argv) != 5:
        print("Incorrect number of command line arguments. Usage: sudo python3 spoofer.py <src_ip> <dst_ip> <dst_port> <payload>")
        exit(0)
    src_ip = sys.argv[1]
    dst_ip = sys.argv[2]
    dst_port = int(sys.argv[3])
    payload = sys.argv[4]
    payload_bytes = payload.encode("utf-8")
    if len(payload_bytes) > 150:
        print("Payload is too long!")
        exit(0)
    
    send_packet(src_ip, dst_ip, dst_port, payload_bytes).show()


