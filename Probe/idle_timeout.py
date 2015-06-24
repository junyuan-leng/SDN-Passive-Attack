#!/usr/bin/env python
from scapy.all import *
import time

start = time.time()
span = 1
for x in range(10):
	packet = Ether()/IP(dst='10.1.1.2')/ICMP()
	ans, unans = srp(packet, filter='icmp', verbose=0)
	rx = ans[0][1]
	tx = ans[0][0]
	rtt = rx.time - tx.sent_time
	interval = time.time() - start
	print "RTT:%s Time:%s" % (rtt, interval)
	time.sleep(span)
	span += 1