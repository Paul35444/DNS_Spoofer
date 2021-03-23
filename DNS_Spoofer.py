#!/usr.bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet():
#get_payload method shows contents of packet
    scapy_packet = scapy.IP(packet.get_payload())
#DNSRR is DNS request response
    if scapy_packet.hasLayer(scapy.DNSRR):
#qname from DNS Question Record is website
        qname = scapy_packet[scapy.DNSQR].qname
#.show method shows all layers of packet
        print(scapy_packet.show())
#allow packet to its dest 
    packet.accept()

#create instace of queue 
queue = netfilterqueue.NetfilterQueue()
#bind queue to queue number 0 and callback to func process_packet
queue.bind(0, process_packet)
queue.run

