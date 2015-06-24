#!/usr/bin/env python
import matplotlib.pyplot as plt

plt.xlabel('Time')
plt.ylabel('RTT')
plt.ylim(0, 0.05)
rtt = list()
time = list()
with open('log.txt') as log:
    for line in log.readlines():
        rtt.append(line.split()[0].split(':')[1])
        time.append(line.split()[1].split(':')[1])
plt.plot(time, rtt)
plt.show()
