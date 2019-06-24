#! /usr/bin/python
# -*- coding: utf-8 -*-


import psutil
import time
import sys
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-t", "--time", dest="time",
                  help="可查看当前下载带宽,-t是测试时间", metavar="10")
parser.add_option("-d", "--deamon", action="store_false", dest="deamon", default=True,
                  help="后台运行")
def Sysinfo():
    Boot_Start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time()))
    time.sleep(1)
    Cpu_usage = psutil.cpu_percent()
    RAM = int(psutil.virtual_memory().total/(1024*1024))
    RAM_percent = psutil.virtual_memory().percent
    Swap = int(psutil.swap_memory().total/(1024*1024))
    Swap_percent = psutil.swap_memory().percent
    Net_sent = (psutil.net_io_counters().bytes_sent) / 1024 / 1024
    Net_recv = (psutil.net_io_counters().bytes_recv) / 1024 / 1024
    Net_spkg = psutil.net_io_counters().packets_sent
    Net_rpkg = psutil.net_io_counters().packets_recv
    BFH = r'%'
    print("\033[1;32m开机时间：%s\033[1;m"  % Boot_Start)
    print("\033[1;32m当前CPU使用率：%s%s\033[1;m" % (Cpu_usage, BFH))
    print("\033[1;32m物理内存：%dM\t使用率：%s%s\033[1;m" % (RAM, RAM_percent, BFH))
    print("\033[1;32mSwap内存：%dM\t使用率：%s%s\033[1;m" % (Swap, Swap_percent, BFH))
    print("\033[1;32m发送：%d M\t发送包数：%d个\033[1;m" % (Net_sent, Net_spkg))
    print("\033[1;32m接收：%d M\t接收包数：%d个\033[1;m" % (Net_recv, Net_rpkg))
    for i in psutil.disk_partitions():
        print(" \033[1;32m盘符: %s 挂载点: %s 使用率: %s%s\033[1;m" % (i[0], i[1], psutil.disk_usage(i[1])[3], BFH))
def Net_io(s):
    x = 0
    sum = 0
    while true:
        if x >= s:
            break
        r1 = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        r2 = psutil.net_io_counters().bytes_recv
        y = r2 - r1
        print("%.2f Kb/s" % (y / 1024.0))
        sum += y
        x += 1
    result = sum / x
    print("\033[1;32m%s秒内平均速度：%.2f Kb/s \033[1;m" % (x, result / 1024.0))
if __name__ == "__main__":
    (options, args) = parser.parse_args()
    if options.time:
        Net_io(int(options.time))
    else:
        Sysinfo()
