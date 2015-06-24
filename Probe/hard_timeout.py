#!/usr/bin/env python
from scapy.all import *
import time

def ping(dst_ip, count = 2000):
        start = time.time()
	hard_timeout = [0]
	for x in range(count):
	        packet = Ether()/IP(dst=dst_ip)/ICMP()
		ans, unans = srp(packet, filter='icmp', verbose=0)
		rx = ans[0][1]
		tx = ans[0][0]
		rtt = rx.time - tx.sent_time
                interval = time.time() - start
		print "RTT:%s Time:%s" % (rtt, interval)
		#if rtt > 0.02:
			#hard_timeout.append(interval)
			#print "Hard Timeout:%f" % (hard_timeout[-1] - hard_timeout[-2])
			#print "Hard Timeout:%s" % time.time() - start
			#break

if __name__=='__main__':
	ping('10.1.1.2')