#!/usr/bin/env python
import matplotlib.pyplot as plt

plt.xlabel('Seq')
plt.ylabel('RTT')
plt.ylim(0, 0.2)
rtt = list()
seq = list()
with open('log.txt') as log:
    for line in log.readlines():
        rtt.append(line.split()[0].split(':')[1])
        seq.append(line.split()[-1].split(':')[-1])
plt.plot(seq, rtt)
plt.show()
