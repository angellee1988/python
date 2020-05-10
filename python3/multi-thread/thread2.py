#!/usr/bin/python3

import threading
import time

exitFlag = 0


class mythread(threading.Thread):
    def __init__(self, threadid, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadid
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadname, delay, counter):
    while counter:
        if exitFlag:
            threadname.exit()
        time.sleep(delay)
        print("%s: %s" % (threadname, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = mythread(1, "Thread-1", 1)
thread2 = mythread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
