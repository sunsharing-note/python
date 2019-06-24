import os  
os.mkdir(name)   #创建目录  
os.path.exists(name)   #判断文件或者目录是否存在  
os.path.isdir(name)     #判断指定对象是否为目录。是True,否则False。  
os.mknod(name)    #创建一个文件  
os.path.isfile(name)   #判断文件是否存在，存在返回True，否则返回False  
```python
>>> os.mkdir('aaaa')
>>> os.path.exists('aaaa')
True
>>> os.path.isdir('aaaa')
True
>>> os.mknod('test.txt')
>>> os.path.isfile('test.txt')
True
```
os.rmdir(name)     #删除一个目录  
os.remove(name) #删除一个文件  
```python
>>> os.rmdir('aaaa')
>>> os.path.isdir('aaaa')
False
>>> os.remove('test.txt')
>>> os.path.isfile('test.txt')
False
```
os.getcwd()   #获取当前路径，相当于Linux下的pwd命令  
os.path.abspath(file|dir)   #获取文件或者目录的绝对路径  
os.path.basename(name)  #获取文件名或文件夹名  
os.path.dirname(name)   #获取文件或文件夹的路径  
```python
>>> os.getcwd()
'/root/SuXinProject'
>>> os.path.abspath('.')
'/root/SuXinProject'
>>> os.path.dirname('/root/user.sh')
'/root'
>>> os.path.basename('/root/user.sh')
'user.sh'
```
os.path.splitext      #分离文件名与扩展名  
os.path.split     #分离目录与文件名  
os.path.join(path,name)   #连接目录与文件名或目录  
```python
>>> os.path.split('/root/user.sh')
('/root', 'user.sh')
>>> os.path.splitext('/root/user.sh')
('/root/user', '.sh')
>>> os.path.join('/root/','user.sh')
'/root/user.sh'
```
os.chdir(dir)   #切换目录  
os.listdir(dir)   #列出目录下的所有目录和文件  
os.path.getsize(file|dir)    #获取文件的大小，如果是目录则直接返回0  
os.stat(name)    #获取文件属性  
os.system(commond)   #执行系统命令  
os.rename(old,new)    #文件重命名  
```python
>>> os.chdir('/root')
>>> os.listdir('.')
['.vnc', 'mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz', '.pydistutils.cfg', '.cache', '.git', 'file', '.mozilla', '.rnd', 'GUESS', 'Music', 'run.sh', '.finalshell', '.viminfy.tmp', '.config', 'docker-logspout-elk', 'Desktop', 'sed.txt', '100oush.sh', 'pid2.txt', '.cshrc', 'mynginx', '.bash_profile', 'etcd', 'sh.txt', 'oushu.sh', '.docker', '.viminfx.tmp', 'pid.sh', 'test', '.pycharm_helpers', 'user.sh', 'net', 'jiujiu.sh', '.dbus', 'sum100.sh', '.ssh', '.bashrc', 'LinEnum', 'sysinfo.sh', '.esd_auth', 'for100oushu.sh', 'pid1.txt', '.local', 'SuXinProject', 'phone.sh', '.ansible', '.viminfz.tmp', 'Documents', '.viminfo.tmp', 'study', '.ICEauthority', 'Pictures', 'for99.sh', '.bash_logout', '.pid.sh.swp', 'qiuhe.sh', 'pid.txt', '.viminfo', '.npm', 'fors00oushu.sh', '.pki', '99.sh', '.gitconfig', 'etcd-v3.2.10-linux-amd64', 'nohup.out', 'Public', 'user1.sh', 'diff.txt', '.Xauthority', '.virtualenvs', '.node_repl_history', '.pip', '.bash_history', 'Downloads', 'Videos', 'killpid.sh', 'Templates', 'daemon.json', 'beijing', 'dif', '.tcshrc', 'kill.sh', '.mysql_history', 'biao.txt', 'blog']
>>> os.path.getsize('./user.sh')
299
>>> os.stat('./user.sh')
posix.stat_result(st_mode=33261, st_ino=143152, st_dev=64769L, st_nlink=1, st_uid=0, st_gid=0, st_size=299, st_atime=1543135673, st_mtime=1542818209, st_ctime=1542818209)
>>> os.system('whoami')
root
0
>>> os.rename('99.sh','999.sh')
```
os.getuid()    #获取用户id  
os.getgid()    #获取用户组id  
os.environ['环境变量名称']='环境变量值'      #设置环境变量  
os.environ['环境变量名称']       #获取环境变量  
os.getenv('环境变量名称')       #获取环境变量  
```python
>>> os.getuid()
0
>>> os.getgid()
0
>>> os.environ['PYTHON']='/usr/local/bin'
>>> os.environ['PYTHON']
'/usr/local/bin'
>>> os.getenv('PYTHON')
'/usr/local/bin'
```
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])      # 从上到下或从下到上遍历树来生成目录树中的文件名  
#### 参数
- top - 以目录为根的每个目录产生3元组，即（dirpath，dirnames，filenames）。dirpath为目录的路径，为一个字符串。
       dirnames列出了目录路径下面所有存在的目录的名称。
       filenames列出了目录路径下面所有文件的名称。
       不明白的可以看下图
- topdown - 如果可选参数topdown为True或未指定，则从上到下扫描目录。如果topdown设置为False，则会自下而上扫描目录，不懂的话可以看下面的代码就明白了
- onerror - 这可能会显示错误以继续行走，或者引发异常以中止行走。
- followlinks - 如果设置为true，则访问符号链接指向的目录。
```python
>>> for root, dirs, files in os.walk("."):
...     for name in dirs:
...             print(os.path.join(root,name))
... 
./shell编程
./test
./ftp
./hexo

>>> for root, dirs, files in os.walk(".", topdown=False):
...      for name in files:
...             print(os.path.join(root, name))
... 
./shell编程/index.html
./test/index.html
./ftp/index.html
./hexo/index.html
./index.html
>>> for root, dirs, files in os.walk("."):
...      for name in files:
...             print(os.path.join(root, name))
... 
./index.html
./shell编程/index.html
./test/index.html
./ftp/index.html
./hexo/index.html
```
