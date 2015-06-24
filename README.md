##文件说明

原型系统代码总共包括4个文件夹，每个文件夹的内容如下：

1. Controller文件夹，包含原型系统的POX Controller端代码，包括FIFO/LRU的流表替换算法实现，以及Hard Timeout和Idle Timeout实验所需的Controller端代码

2. Plot文件夹，包含用于解析日志文件log.txt并绘制RTT曲线图的代码，其中Flowtable Capacity/Flowtable Usage两个实验的日志，采用capacity_usage_plot.py进行绘制，Hard Timeout/Idle Timeout两个实验的日志，采用timeout_plot.py进行绘制

3. Probe文件夹，包含原型系统的被动隐私探测代码，通过构建ICMP包并获取RTT，进行被动隐私探测

4. Topo文件夹，包含原型系统的网络拓扑构建代码

##使用方法

1. 将Controller文件夹下所有.py代码拷贝至POX的misc目录，然后通过python pox.py misc.xxxxx启动相应Controller，如启动FIFO代码，可执行python pox.py misc.fifo

2. 将Topo文件夹中的mytopo.py文件拷贝至Mininet根目录，启动Mininet并连接至POX，相应命令为sudo mn --custom mytopo.py --topo mytopo --controller=remote,ip=xxxx --mac --switch=ovsk,protocols=OpenFlow1.3

3. 在Mininet中执行相应的被动隐私探测代码，并将被动隐私探测代码的输出结果重定向至log.txt日志文件，相应命令为lh python xxxx.py > log.txt，如进行Flowtable Capacity探测，则执行lh python flow_table_capacity.py > log.txt

4. 执行完毕后，退出Mininet，将之前生成的log.txt文件拷贝至绘图代码所在文件夹，由于log.txt文件的第一行会有特殊字符使日志解析中断，因此需要删除log.txt的第一行，然后执行绘图代码python capacity_usage_plot.py或python timeout_plot.py

5. 根据绘制完成的RTT曲线图，即可对相应指标进行推断