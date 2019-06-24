## Python的语句与语法

| 语句 | 角色 |  例子  |
| :--- | ---:| ---: |
| 赋值| 创建引用值 |a='Apple',b='bike'|
| 调用|执行函数|log.write('mylog')
|打印调用|打印对象|print(1,'hello')
|if/elif/else|选择动作|if a in b: print(a)
|for/else|序列迭代|for i in list: print(i)
|while/else|一般循环|while True: print('True')
|pass|空占位符|for i in list: pass
|break|循环/迭代退出|while True:if a==b: break
|continue|循环继续|for i in list: if i<5: continue
|def |函数定义|def add(a,b): print(a+b)
|return|函数返回|def add(a,b): return  a+b
|import|模块访问|import os
|from|属性访问|from sys import stdin
|class|创建类|class myclass(): def myprint(): print('myprint')
|try/except/finally|捕获异常|try: open('/tmp/file') except: print('no file')
|raise|触发异常|raise <'error type'>
|assert|调试检查|assert a<0,'a is too large'
|with/as|环境管理器|with open(file) as f: f.read()
|del|删除引用|del_list[i] del_list[i:j] del obj.attr

### Python语句的格式
#### 语句的开头
在python里是不使用{}或者别的符号来限制语句的开始和结尾的，一个语句的开始(除了复合语句)，就是开头，换行就是结束。在开头，不能随意增加空格：
```python 
>>> print (1)
1
>>>  print (1)
  File "<stdin>", line 1
    print (1)
    ^
IndentationError: unexpected indent
```

#### 语句的对齐
在复合语句里也是同样的，当你使用缩进时，必须一致：
```python
>>> def add(str):
...     str=str
...    print(str)
  File "<stdin>", line 3
    print(str)
             ^
IndentationError: unindent does not match any outer indentation
```

#### 复合语句
复合语句有单行写法和多行写法。从冒号后面就是复合语句的开始。
单行：复合语句只有一行时，可使用单行写法，但是复合语句所包含的语句不是单行时，需要使用对齐的缩进来表示复合语句
```python
#单行语句
>>> if 1>0: print(1)
...
1
#多行语句
>>> if 1>0:
...     int=1
...     print(int)
...
1
```

#### 语句的结束
一般语句里，一行的结束就是此语句的结束。
在简单语句可以使用分号来隔开多个语句。
```python
>>> a=3;b=3;print(a+b)
6
```
使用列表，元组，字典的时候按照一定的方式可以把一个语句分成多行:
```python
>>> dict={1:'first',
... 2:'second'}
```

#### 处理错误
当我们所写的语句有bug，会出现一些错误，程序会中断运行。
但我们在这个时候，不想让程序中断但还是需要提示报错的时候可以使用try:
```python
>>> while True:
	_input=input("please input digit:")
	try:
		print("{:d} *10 is {:d}".format(int(_input),int(_input)*10))
		break
	except:
		print("{} is not a number".format(_input))

		
please input digit:a
a is not a number
please input digit:1
1 *10 is 10
```

### 变量赋值
#### 变量命名规则
变量名可以使大小写字母，数字和下划线，但只能以大小写字母和下划线开头，不能以数字开头。变量名是区分大小写的，保留字符是不能使用的。
python3.0里的保留字符：
false	class	finally	is
None	continue	for	lambda
True   def	    from    nonlocal
and	  del     dlobal    not
as   	  elif       if          or
assert	else    import    pass
break    except    in      raise
特殊变量名：
__main__等，前后都有两个下划线的变量名，有很多是有特殊意义的

### 打印
#### print 函数
从python3.0开始print变成了函数，但返回值为None，print函数的格式如下：
print([object,...][,sep=''][,end='\'][file=sys.stdout])
在这里，object是要打印的内容。object可以是任意对象。默认是没有。
sep是两个object之间隔开的字符。默认是一个空格。
end是结尾，默认为换行。
file为输出目标，默认为标准输出流。
```python
>> print(1,2,3,sep=';')
1;2;3
>>> print(1,2,3,sep=':')
1:2:3
>>> print(1,2,3,end='')
1 2 3
>>> print(1,2,3,end='');print (4,5,6,end='')
1 2 34 5 6
>>> print(1,2,3,end='\n');print (4,5,6,end='')
1 2 3
4 5 6
>>> print(1,2,3,file=open(r'D:\ruanjian\1.txt','wt'))
>>> file=open(r'D:\ruanjian\1.txt')
	  
>>> file.read()
	  
'1 2 3\n'
```

### 判断语句
#### 真值测试
在if语句里的<'test'>位置里的就是判断语句，结果为True，就能进入子语句，判断语句包含：
- 比较运算符：==,!=,>,<,>=,<=
- 逻辑运算符：and,or,not
- 成员运算符：in，not in
- 身份运算符：is，is not
- 其他：对象为空，0，None等的时候是False,其他为True
```python
>>> 1<2
True
>>> True and True
True
>>> 1 and True
True
>>> True or False
True
>>> not True
False
>>> not False
True
>>> 1 in [1,2]
True
>>> 1 in (1,2)
True
>>> 1 in {'1':1}
False
```

#### 逻辑运算符
当我们使用and和or的时候，返回结果不一定是True或False:
and:当其中一个或多个测试值为false的时候，取第一个false的值
```python
False
>>> 1 and [] and {}
[]
```
and:当全部值得测试值为True的时候，取最后一个值
```python
>>> 1 and 2 and True
True
>>> 1 and 2 and True
True
>>> 1 and 2 and True and 3
3
```
or:当其中一个或多个值为True的时候，取第一个True的值
```python
>>> 0 or [1] or {1:'1'}
[1]
>>> 1 or 0 or 2
1
```
or:当全部值为false的时候，去左后一个false值
```python
>>> 0 or [] or {}
{}
>>> False or 0 or {}
{}
```

#### 三元表达式
三元表达式的格式如下：
<'value1'>if <''test'> else <'value2'>
当测试值为真的时候取<'value1'>,假的时候取<'value2'>
```python
>>> 1 if True else 2
1
>>> 1 if False else 2
2
>>> 'True' if 1>2 else 'False'
'False'
>>> 'True' if 1<2 else 'False'
'True'
```
这个还可以如下运用：
[<'value2'>,<'value1'>][<'test'>]
```python
>>> [2,1][True]
1
>>> [2,1][False]
2
>>> ['False','True'][1>2]
'False'
>>> ['False','True'][1<2]
'True'
```

### while语句
whil语句一般格式：
```python
while <'test1'>:
	<'statement1'>
else:
	<'statement2'>
```
只要测试语句为真，会一直循环<'statement1'>。当test1为假的时候会运行else语句里的内容。从这里，退出循环的方法有：
1.在<'statement1'>里的语句更改<'test1'>的结果为False
2.在<'statement1'>里的语句里增加break语句来跳出循环
3.在<'statement1'>里的语句里增加exit()来退出python循环，不过这里会退出整个的python程序

例子
```python
>>> a=0;b=10
>>> while a<b:
	print(a,end='')
	a+=1

0123456789
```

### break,continue语句
break语句用来退出最近所在的for语句或while语句。
continue语句是用来跳到最近所在的for语句或者while语句的结尾。
```python
>>> a=0;b=10
>>> while a<b:
	a+=1
	if a==3: continue
	if a ==7: break
	print (a,end='')

12456
```

### pass语句
pass语句是占位的空语句，在有些复合语句里，可能没有具体的语句，但需要正常运行，这就需要设置空语句（pass）来代替
例子
```python
>>> if True:
	print('true')
else: pass

true
```

### else语句
else语句，只有在for语句和while语句正常结束后，会运行：
```python
>>> a=0;b=10
>>> while a<b:
	print(a,end='')
	a+=1
else:
	print('end')

0123456789end
```

### for语句
for语句在python里是一个通用的序列迭代器：可以遍历任何有序的序列对象内的元素。可用于字符串、列表、元组、其他内置可迭代对象以及之后我们能通过类所创建的新对象。
一般格式：
```python
for <target> in <object>:
	<statements>
else:
	<statements>
```
在这里object需是可迭代的对象。每次从object里提取一个元素付给target，之后循环statements里的语句。
例子
```python
>>> for i in a:
	print (i,end='')

12345
```
#### 用法
使用for循环时，其他开发语言会使用一个变量，定义起始，结束，递增值。但python里只能做迭代。这个时候可以使用range函数来代替。
range函数格式：
range([起始值,]结束值,[递增值])
在这里，起始值默认是0，递增值默认为1。
```python
>>> a=range(10)
>>> for i in a:
	print(i,end='')

0123456789
```
当迭代后的元素为固定长度的元组。列表的时候：
```python
>>> for a,b,c in [(1,2,3),(4,5,6),(7,8,9)]:
	print (a,b,c)

1 2 3
4 5 6
7 8 9
```

嵌套循环（不一定是固定长度）：
```python
>>> for l in [(1,2,3),(4,5,6),(7,8,9)]:
	for i in l:
		print(i,end='')
	print()

123
456
789
```

### 迭代器和解析
#### 文件迭代器
文件访问方式如下：
- <'file'>.read():一次性读取全部内容。
- <'file'>.readline():一次读取一行。
- <'file'>.readlines():生成列表，每一行是每个元素。
- <'file'>.__next__():跟readline()差不多，但读取完之后报错。

`__next__()`报错为stoplteration。在python中任何这类对象都认为是可迭代的。在python里迭代工具（比如for）会调用`__next__()`来获取数据，并以stoplteration来确认何时离开。
> 尽量不要使用readlines()函数，因为这个会一次性得把所有内容读取到内存里（转换为列表），运行速度会比较慢。

#### 手动迭代
为了支持手动迭代代码，python支持next()函数，它会自动读取`__next__()`函数。
next(X)等同于`X.__next__()`。
```python
>>> file=open(r'D:\ruanjian\1.txt')
>>> file.__next__()
'hello,world'
>>> file.seek(0)
0
>>> next(file)
'hello,world'
>>> next(file)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    next(file)
StopIteration
```
这个会从第一行开始读取内容，但是这个文本文件就一行，所以读完之后再读会报错。
迭代协议里，当时用for函数进行迭代时，会传递给iter()内置函数，以便可迭代对象中获取迭代器。返回的对象中有next()方法
```python
>>> li=[1,2,3]
>>> i=iter(li)
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    next(i)
StopIteration
```

对于文件来说，不需要转换成iter类型的这一步，
因为文件对象就是自己的迭代器。
```python
>>> file=open(r'D:\ruanjian\1.txt')
>>> file is iter(file)
True
```
但列表，元组，字符串就不是了。
```python
>>> s='123';l=[1,2,3];t=(1,2,3)
>>> s is iter(s)
False
>>> l is iter(l)
False
>>> t is iter(t)
False
```
如果要使用next方法就需要先将字符串，列表，元组转换成迭代器

#### 其他内置类型迭代器
除了文件以及像列表这样的实际的序列外，其他类型也有其适用的迭代器。例如，遍历字典键的经典方法是明确的获取其键的列表。
```python
>>> dic={'a':1,'b':2,'c':3}
>>> for key in dic.keys():
	print(key,dic[key])
	
a 1
b 2
c 3
```

这个迭代器也可以直接对字典进行迭代：
```python
>>> iter1=iter(dic)
>>> iter1.__next__()
'a'
>>> next(iter1)
'b'
>>> next(iter1)
'c'
```

#### 列表解析
遍历列表时，使用for循环来修饰它:
```python
>>> li=[1,2,3,4,5]
>>> for i in range(len(li)):
	li[i]+=10

>>> li
[11, 12, 13, 14, 15]
```
但这样看来并不简便，我们可以使用产生所需列表的一个单个表达式来完成上面的循环
```python
>>> li=[1,2,3,4,5]
>>> li=[i+10 for i in li ]
>>> li
[11, 12, 13, 14, 15]
```
这个先是运算[i+10 for i in li]之后，再把此值赋给li,具体的运算是先是对li进行迭代，每次把单个值赋给i，在进行i+10,成为新列表的单个元素。 

##### 扩展用法
我们可以使用如下方法，将列表的某一项排除
```python
>>> li=[1,2,3,4,5]
>>> li=[i+10 for i in li if i != 3]
>>> li
[11, 12, 14, 15]
```
也可以在列表中进行循环嵌套,可以看到y的循环嵌套在了x循环里
```python
>>> [x+y for x in [1,2,3] for y in [10,20,30]]
[11, 21, 31, 12, 22, 32, 13, 23, 33]
```

#### 其他迭代环境
map也可用在迭代
```python
>>> list(map(str.upper,open(r'D:\ruanjian\1.txt')))
['HELLO,WORLD']
```
map函数是把后面的可迭代的每个值当做前面的参数传入。
上面的语句可以如下解释：
```python
>>> tmp=[]
>>> for line in open(r'D:\ruanjian\1.txt'):
	tmp.append(str.upper(line))
	
>>> tmp
['HELLO,WORLD']
```
相应的也有sorted会对迭代对象进行排序后生成列表
```python
>>> sorted(open(r'D:\ruanjian\1.txt'))
['hello,world']
```
numerate也会对迭代对象进行运算后生成可迭代列表。enumerate就是在原有的顺序中添加序列号。
```python
>>> list(enumerate(open(r'D:\ruanjian\1.txt')))
[(0, 'hello,world')]
```
sum、any、all、max、min也可使用迭代器。
```python
>>> max([3,5,1,6,4]),min([3,6,8,2,4])
(6, 2)
>>> any([1,[],'True']),all([1,[],'True'])
(True, False)
```

#### python3中新的可迭代对象
在python3中函数生成的是可迭代的特定对象：
```python
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
```
python3的这种方式会延迟计算，在提取内容的时候计算结果，这样会节省内存空间，不需要提前计算后放进内存，迭代对象迭代完成后不能再次读取
```python
>>> def printlist(list1):
	for i in list1:
		print('function print:{}'.format(i))
		yield 'Result: {}'.format(i)

>>> li=[1,2,3,4,5]
>>> s=printlist(li)
>>> s.__next__()
function print:1
'Result: 1'
>>> s.__next__()
function print:2
'Result: 2'
>>> s.__next__()
function print:3
'Result: 3'
```
