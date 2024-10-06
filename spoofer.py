from scapy.all import *

# sends a UDP packet with the specified arguments
def send_packet(src_ip, dst_ip, dst_port, payload):
    if len(payload) > 150:
        return
    packet = IP(src = src_ip, dst = dst_ip) / UDP(dport = dst_port) / Raw(load = payload)
    send(packet)
    return



