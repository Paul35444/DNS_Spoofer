#!/usr.bin/env python

import netfilterqueue

def process_packet():
    print(packet)

#create instace of queue 
queue = netfilterqueue.NetfilterQueue()
#bind queue to queue number 0 and callback to func process_packet
queue.bind(0, process_packet)
queue.run