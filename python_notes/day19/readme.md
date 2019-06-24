* join会把线程给挺住，造成串行，失去了线程的意义
* 加同步锁
* GIL作用：对于一个解释器，只能有一个thread在执行bytecode
* 所以每时每刻只有一条bytecode在被执行一个thread
* 死锁 递归锁
* RLock 递归锁
* 信号量：控制线程并发数的
* 条件变量 其实是一把锁 需要满足条件才能执行 wait notify notifyAll 
* event 同步条件
* 多线程利器 队列(queue)