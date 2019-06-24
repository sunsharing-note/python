```
参考：https://blog.csdn.net/u011798443/article/details/80825817
1.安装依赖
yum install zlib zlib-devel gcc -y
2.下载源码包
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
3.安装
tar -zxvf Python-3.6.3.tgz
cd python-3.6.3
mkdir /usr/local/python3
./configure --prefix=/usr/local/python3
make all && make install
4.确认
/usr/local/python3/bin/python3.6 -V

5.备份之前的python
mv /usr/bin/python /usr/bin/python2.7.5
6.创建软连接
ln -s /usr/local/python3/bin/python3 /usr/bin/python
7.测试
python
8.修改yum
[root@ansible2 Python-3.6.3]# cat /usr/bin/yum |head  -n 5
#!/usr/bin/python2.7.5
import sys
try:
    import yum
except ImportError:
上面的python版本修改为之前备份的那个版本
9.如果使用yum还有错，则修改以下文件
vim /usr/libexec/urlgrabber-ext-down
python版本同上
```
