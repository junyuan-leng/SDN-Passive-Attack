#!/usr/bin/env python
from scapy.all import *
import time

def macgen():
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

def ping(dst_ip):
	seq = 1
	packet = Ether(src=macgen())/IP(dst=dst_ip)/ICMP()
	ans, unans = srp(packet, filter='icmp', verbose=0)
	rx = ans[0][1]
	tx = ans[0][0]
	rtt = rx.time - tx.sent_time
	print "RTT:%s Flow Entry:%s" % (rtt, seq)
	for i in range(1300):
	        packet = Ether(src=macgen())/IP(dst=dst_ip)/ICMP()
		ans, unans = srp(packet, filter='icmp', verbose=0)
		rx = ans[0][1]
		tx = ans[0][0]
		rtt = rx.time - tx.sent_time
		print "RTT:%s Flow Entry:%s" % (rtt, seq)
                '''
		if rtt > 0.08 and rtt < 1.0:
			print "Flow table capacity:%d" % seq
			break
                '''
		seq += 1

if __name__=='__main__':
	ping('10.1.1.2')
