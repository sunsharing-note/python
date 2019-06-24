* 编码 
* python2有两种数据类型编码：str: bytes unicode:unicode unicode和明文直接对应
* python2特点：内部可以转换
* python3两种数据类型编码：bytes str 自己转，内部不转换了
* utf8 一个占3个 gbk 一个占2个
* 进程 多进程 通信通过queue与pipes
* manager 供养数据
* 协程 单线程 轻量级线程
* 协程的好处：无需线程上下文切换的开销 无需原子操作锁定以及铜鼓的开销
* 方便切换控制流，简化编程模型 高并发+高扩展性+低成本
* 协程的缺点: 无法利用多核资源 进行阻塞操作会阻塞掉整个程序
* yield来实现协程
* gevent模块 第三方库 并发效果