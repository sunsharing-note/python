## re正则处理
### 正则定义
正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。
### 常用正则表达式的方法
- re.compile(编译)
- pattern.match(从头匹配)
- pattern.search(匹配一个)
- pattern.findall(匹配所有)
- pattern.sub(替换)

### 特殊字符集

| 特殊字符   |  解释 |  
| :--------: | :--------:| 
| . |匹配除换行符之外的任何字符|
| ^ |匹配字符串的开头|
| $ |匹配字符串的结尾|
| * |匹配前面的字符0次或更多次，尽可能多的重复，ab*将匹配'a','ab'或者a后面加任意数量的b|
| + |匹配前面的字符一次或更多次，ab+将匹配'ab'后加任意数量的b|
| ? |匹配前面的字符0次或一次，ab将匹配'a'或'ab'
|*?,+?,??| *,+,?都属于贪婪匹配，就是尽可能多的匹配，而有时我们希望以最少的模式匹配，可以在限定符之后加?表示以最少的方式匹配
|{m}|匹配前一个字符至少m次|
|{m,n}|匹配前一个字符最少m次，最多n次|
|{m,n}?|以非贪婪模式匹配前一个字符，最少m次，最多n次，并以尽可能少的方式匹配|
|\ |转义字符，将\后面的字符进行转义|
|[]|表示一组字符，字符可以单个列出，也可以给定范围，如[abc]表示a或b或c，[a-z]表示26个小写字母中的任意一个，[^a-z]匹配非小写字母，[0-5][0-9]表示匹配00-59，特殊字符在[]也失去特殊意义，[(+* )]将匹配任何文字字符的'(',')','+','*'
| \||A\|B 匹配A或者B
|()|匹配括号内的正则，每个括号都是一个组，从左往右的括号，编号依次加一
|\A|匹配字符串的开头
|\b|只用以匹配单词的词首和词尾(退格符)
|\B|只在当前位置不在单词边界时匹配。
|\d|匹配任何Unicode的十进制数字，与[0-9]相同
|D|匹配任何非十进制的字符，与[^0-9]相同
|\s|匹配Unicode的空白字符，匹配ascii字符集中包含空格的字符，相当于[\t\n\r\f\v]
|\S|匹配不是空白字符的字符，相当于[^\t\r\n\f\v]
|\w|匹配字母数字下划线，相当于[a-zA-Z0-9_]
|\W|匹配非字母数字下划线，相当于[^a-zA-Z0-9]
|\Z|仅匹配字符串结尾
|`(?P<name>)`|给分组加一个别名，`(?P<a>)`给分组取别名为a，每个组名只能在正则表达式中定义一次
|(?P=name)|引用前面别名为name的分组匹配到的任何文本
|(?<=)|前向界定，表示你要匹配的字符串前面是某个字符串的时候才匹配，('(?<=abc)def','abcdef')当def前面是abc的时候才匹配
|(?=)|后向界定，表示你要匹配的字符串后面是某个字符串的时候才匹配，('abc(?=def)','abcdef')
|(?<!)|非前向界定，表示你要匹配的字符串前面不是某个字符串的时候才匹配，('(?<=abc)def','abcdef')当def前面不是abc的时候才匹配
|(?!)|非后向界定，表示你要匹配的字符串后面不是某个字符串的时候才匹配，('abc(?=def)','abcdef')
|(?(id/name)yes-pattern|no-pattern)

### 正则表达式方法
- re.compile(pattern,flags=0)
编译一个正则表达式模式为正则表达式对象，其可用于使用他的匹配match(),search()以及其他方法
```python
>>> comp=re.compile(r'\d+')
>>> ret=comp.match('123456')
>>> ret.group()
'123456'
```
相当于
```python
ret=re.match(r'\d+','123456')
```

- re.search(pattern,string,flags = 0)
 查找正则表达式匹配到的第一个位置，并返回相应的匹配对象

- re.match(pattern,string,flags = 0)
 从字符串的开头匹配，并返回相应的匹配对象

- re.fullmatch(pattern,string,flags = 0)
  将会对整个字符串进行匹配，并返回相应的匹配对象

- re.split(pattern,string,maxsplit = 0,flags = 0)
  按照正则匹配模式进行拆分字符串,maxsplit为最多拆分次数，并且字符串的其余部分将作为列表的最后一个元素返回，如果分隔符中有捕获组并且它在字符串的开头或者结尾匹配，则结果将以空字符串开头。
```python
>>> re.split(r'\W+','Words words wordS')
['Words', 'words', 'wordS']
>>> re.split(r'\W+','Words words wordS',1)
['Words', 'words wordS']
>>> re.split(r'\d+','1q2W3e4R',flags=re.IGNORECASE)
['', 'q', 'W', 'e', 'R']
>>> re.split(r'(\W+)', 'words, words...')
['words', ', ', 'words', '...', '']
>>> re.split(r'\W+', 'words, words...')
['words', 'words', '']
```
- re.findall(pattern,string,flags=0)
  从左往右匹配，返回一个列表，如果模式中存在一个或多个组，则返回组列表; 如果模式有多个组，这将是一个元组列表。结果中包含空匹配。
```python
>>> re.findall(r'\d+','123,456')
['123', '456']
>>> re.findall(r'(\d+)(\w+)','123qw,werrc')
[('123', 'qw')]
>>> re.findall(r'(\d+)|(\w+)','123qw,werrc')
[('123', ''), ('', 'qw'), ('', 'werrc')]
```
- re.finditer(pattern,string,flags = 0 )
  返回一个匹配到每个结果的迭代器
```python 
>>> for i in re.finditer(r'\d+','123456'):
	print(i.group())
123456
```
- re.sub(pattern,repl,string,count = 0,flags = 0 )
   将匹配到的字符串替换成repl的值，count表示要替换的模式最多替换次数，repl可以是一个字符串也可以是一个函数，当repl为字符串时，会处理其中的任何反斜杠，，可以使用\id或\g< id>、\g< name>引用分组
```python
>>> re.sub(r'(\d+) (\w+)',r'\2 \1','12345 asdfd')
'asdfd 12345'
```
  当repl是一个函数时，那么这个函数会只接受一个匹配对象参数。例如：
```python
>>> def mat(m):
	if m.group(2)=='1234':
		return m.group(1)
	else:
		return '1234'

>>> re.sub(r'(\d+) (\d+)',mat,'123 1234qer')
'123qer'
>>> re.sub(r'(\d+) (\d+)',mat,'123 123qer')
'1234qer'
``` 
- re.subn(pattern,repl,string,count = 0,flags = 0 )
与sub执行的操作相同，但是返回的是元组，元组最后一个元素为替换次数
```python
>>> def mat(m):
	if m.group(2)=='1234':
		return m.group(1)
	else:
		return '1234'
>>> re.subn(r'(\d+) (\d+)',mat,'as123 1234qer')
('as123qer', 1)
```
### 正则表达式对象
使用re.compile可以编译一个正则表达式对象
- regex.search(string[,pos[endpos]])
  查找正则表达式匹配到的第一个位置，并返回相应的匹配对象可选参数pos和endpos表示设置正则表达式匹配的字符串开始位置和结束位置
```python
>>> pattern=re.compile(r'\d+')
>>> pattern.search('123456',2,5).group()				   
'345'
```
- regex.match(string,posendpos)
  如果字符串开头的零个或多个字符与此正则表达式匹配，则返回相应的匹配对象。pos和endpos用法和regex.search()意思相同
- 编译的正则表达式的方法和属性与正则匹配的函数相同，这里不一一说明
#### 编译对象的常用参数
- re.A(re.ASCII)
  使\w,\W,\b,\B,\d,\D,\s和\S只匹配ASCII字符，而不匹配Unicode字符
- re.I(re.IGNORECASE)
  匹配时不区分大小写
- re.L(re.LOCALE)'
  使\w \W \b \B \s \S \d \D和区分大小写的匹配只取决于当前的环境设定
- re.M(re.MULTILINE)
  多行模式下，'^'和'$'由原来匹配字符串的开头或者结尾变成匹配每行的开头和结尾
- re.S(re.DOTALL) 
  使'.'匹配包含换行符的任何字符
- re.X(re.VERBOSE)
  这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的
```python
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
```

### match对象
- match.group([ group1,... ] )
  返回匹配的一个或多个子组，如果只有一个参数，则结果为单个字符串; 如果有多个参数，则结果是一个元组，每个参数有一个项目。如果没有参数，group1默认为零（返回整个匹配）。 如果groupN参数为零，则相应的返回值是整个匹配的字符串
```python
>>> s=re.match(r'(\w+) (\w+)','hello world')
>>> s.group(0)
'hello world'
>>> s.group(1)
'hello'
>>> s.group(2)
'world'
>>> s.group(1,0)
('hello', 'hello world')
```
如果分组太多，我们可以对分组进行命名
```python
>>> m=re.match(r"(?P<first>\w+) (?P<second>\w+)",'hello world')
>>> m.group('first')
'hello'
>>> m.group('second')
'world'
```
如果一个组匹配多次，那么最终将返回的最后一次匹配到的字符串
```python
>>> m=re.match(r'(\d)+','123456')
>>> m.group()
'123456'
>>> m.group(1)
'6'
```
- match.__ getitem__(g)
  与m.group(g)相同，这样使用会更简单
```python
>>> m=re.match(r'(\d)+','123456')
>>> m[0]
'123456'
>>> m[1]
'6'
```
- match.groups(default=None)
  以元组的形式返回匹配到的所有子组，没有被匹配到的分组，默认为None,当然可以设置默认参数
```python
>>> m=re.match(r'(\d+),(\w+)?','1234,')
>>> m.groups()
('1234', None)
>>> m.groups('0')
('1234', '0')
```
- match.groupdict(default=None)
  以字典的形式返回匹配到的值，字典的键为分组名，值为匹配到的字符串，没有匹配到的分组将设置为None
```python
>>> m=re.match(r'(?P<first>\d+) (?P<second>\d+)','123 456')
>>> m.groupdict()
{'first': '123', 'second': '456'}
>>> m=re.match(r'(\d+) (\d+)','123 456')
>>> m.groupdict()
{}
```

- match.start([group]) 和match.end([group])
  分别返回由分组匹配到的字符串的开始和结束的索引，结束字符串的索引为最后一个子符的索引加一group默认为零，将会表示所有匹配到的字符串
```python
>>> m=re.match(r'(\w+) (\w+) (\w+) (\w+)','my name is wanger')
>>> m.start(2)				   
3
>>> m.end(2)				   
7
>>> m.end()				   
17
>>> m.start()				   
0
```
- match.span[group]
  返回一个二元组，元组的元素为分组匹配到的字符串开始的索引和结束的索引，group默认为0，表示匹配到的所有字符串
```python
>>> m=re.match(r'(\w+) (\w+) (\w+) (\w+)','my name is wanger')
>>> m.span(2)					   
(3, 7)
>>> m.span()				   
(0, 17)
```
- match.pos 和match.endpos
  分别返回要匹配字符串的开始搜索的索引和结束搜索的索引
```python
>>> m=re.match(r'(\w+) (\w+) ','my name is wanger')
>>> m.pos				   
0
>>> m.endpos				   
17
```
- match.lastindex
  最后匹配到的分组的索引
```python
>>> m=re.match(r'(\w+) (\w+) ','my name is wanger')
>>> m.lastindex				   
2
>>> m=re.match(r'(\w+) (\w+) (\w+)','my name is wanger')					   
>>> m.lastindex					   
3
```
- match.lastgroup
  最后匹配到的分组的名称,没有命名组则返回空
```python
>>> m=re.match(r'(\w+) (?P<last>\w+) ','my name is wanger')				   
>>> m.lastgroup				   
'last'
```  
### 几个简单的实例
1. 匹配前面是数字123的字符
```python
>>> re.search(r'(?<=123)\w+','123asd,wer').group(0)	'asd'
```
2.匹配前面是数字后面是下划线的字符
```python
>>> re.search(r'(?<=123)\w+(?=_)','123asd_123wer').group(0)				   
'asd'
```
3.匹配手机号码
```python
>>> re.match(r'1[3,5,7,8]\d{9}|','13573528479').group()				   
'13573528479'
```
4.匹配电话号码
```python
>>> re.match(r'\d{3}-\d{8}|\d{4}-\d{7}','0531-82866666').group()				   
'0531-8286666'
```
5.匹配IP地址
```python
>>> re.match(r'\d+\.\d+\.\d+\.\d+','192.168.10.25').group()					   
'192.168.10.25'
```
6.匹配网易邮箱
```python
>>> re.findall(r'\w+@163\.com|\w+@126\.com','wanger@163.com wanger@126.com')
					   
['wanger@163.com', 'wanger@126.com']
```
7.匹配HTML文本
```python
>>> re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<body><h2>wahaha5354</h2></body>').group()
'<body><h2>wahaha5354</h2></body>'
```

