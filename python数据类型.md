## python数据类型：
1. Number（数字）
2. String(字符串)
3. List(列表)
4. Dictonary（字典）
5. Tuple(元组)
6. sets(集合)


其中数字、字符串、元组是不可变的，列表、字典是可变的。  
对不可变类型的变量重新赋值，实际上是重新创建一个不可变类型的对象，并将原来的变量重新指向新创建的对象（如果没有其他变量引用原有对象的话（即引用计数为0），原有对象就会被回收）。
### 数字
- int:整数  
        &ensp;&ensp; 1.正负数
        &ensp; &ensp;2.十六进制(表示方式为0x或者0X开头。例如：0xff)
        &ensp; &ensp;3.八进制(表示方式为0o或者0O开头。例如：0o632457)
        &ensp;&ensp; 4.二进制 (表示方式为0b或者0B开头。例如：0b101100)
- fraction:分数
- float:浮点数
- complex:复数
- bool:布尔型(特殊的数值类型，只有True和False两个值)
##### 进制转换
###### 整数转其他进制
使用bin(i),oct(i),hex(i)函数可以将十进制数分别转换为二进制，八进制，十六进制
```python 
>>> s=10
>>> bin(s)
'0b1010'
>>> oct(s)
'0o12'
>>> hex(s)
'0xa'
```
使用int(str,base)可以将非十进制的数转换成整数
，其中str是文本形式的数字，base可以为2,8,16数字，分别代表二进制，八进制，十六进制，最高到36位，最低为2
```python
 >>> int('0b10010',2)
18
>>> int('0o52415',8)
21773
>>> int('0x134ab',16)
79019
>>> int('s',32)
28
>>> int('yz',36)
1259
```
当然也可以进行16进制转二进制八进制，八进制可以转其他进制
```python
>>> hex(0b1001)
'0x9'
>>> hex(0o1234)
'0x29c'
>>> oct(0b101)
'0o5'
>>> oct(0xff)
'0o377'
>>> bin(0xff)
'0b11111111'
>>> bin(0o7777)
'0b111111111111'
```
##### 各类运算符
- 算数运算符：+,-,*,/,%.//,**
- 比较运算符：==，!=,>,<,<=,>=
- 赋值运算符：=,+=,-=,*=,/=,%=,//=.**=
- 位运算符：&,|,^,~,<<,>>
- 逻辑运算符：and,or,not
- 成员运算符：in,not in
- 身份运算符：is,is not
```python
>>> a=12
>>> f=~a
>>> f
-13
>>> bin(f)
'-0b1101'
>>> bin(a)
'0b1100'
>>> bin(a<<1)
'0b11000'
>>> bin(a>>1)
'0b110'
>>> list=[1,2,3,4,5]
>>> a=3
>>> print (a in list)
True
>>> print (a not in list)
False
>>> a=['1,2,3,4,5']
>>> b=a
>>> print (b is a )
True
>>> print (b is not a )
False
>>> b=a[:]
>>> print (b is a)  #这是因为字符串是不可变的
False
>>> print (id(a))
42473480
>>> print (id(b))
42485000
```
##### 运算符优先级
- ** （优先级最高的是幂运算）
- ~,+,-   (加和减都是一元运算符)
- *，/，%，//
- +,-
- <<,>>
- &
- ^,|
- <=,>=,<,>
- ==,!=
- =,+=,-=,*=,/=,%=,//=,**=
##### 数学函数的应用
- power：幂函数，功能与运算符**一样
```
>>> pow(2,3)
8
```
- sqrt：取当前数的平方根
```
>>> import math
>>> math.sqrt(4)
2.0
```
- max：最大值
```python
>>>max(2,3,4,5,1,9,6)
9
```
- min：最小值
```python
>>> min(2,3,4,5,1,9,6)
1
```
- abs与fabs：取绝对值，fabs取出的是浮点数
```python
>>> abs(-1)
1
>>> math.fabs(-1)
1.0
```
- round：四舍五入（当小数为5的时候会向靠近偶数的一端进）
```
>>> round(3.5)
4
>>> round(2.5)
2
>>> round(2.54)
3
>>> round(2.45)
2
```
- ceil：向上取整
```
>>> math.ceil(1.7)
2
>>> math.ceil(1.3)
2
```
- floor：向下取整
```
>>> math.floor(1.7)
1
>>> math.floor(1.3)
1
```
- cmp：python2中的比较函数，当前面数值大返回-1，一样大返回0，后面数值大返回1
```python
>>> cmp(1,2)
-1
>>> cmp(1,1)
0
>>> cmp(2,1)
1
```
- 随机数函数
 &ensp;&ensp;- 取0-1之间的随机小数：
```
>>> import random
>>> random.random()
0.18001643527271916
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- 取自定义数里的随机数：(可以取多个元素)
```
>>> random.choice([1,2,3,4,5])
2
>>> random.choice([1,2,3,4,5])
3
>>> random.sample([1,2,3,4,5,6,7,8,9],2)
[3, 7]
>>> random.sample([1,2,3,4,5,6,7,8,9],3)
[4, 9, 3]
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- 随机打乱顺序：
```
>>> a=[1,2,3,4,5,8]
>>> random.shuffle(a)
>>> a
[1, 8, 2, 3, 4, 5]
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- 获取N位随机数：(二进制)
```
>>> random.getrandbits(6)
55
>>> random.getrandbits(6)
48
>>> random.getrandbits(7)
104
```
- modf：把浮点数的整数位和小数位单独取出来
```
>>> math.modf(1.4)
(0.3999999999999999, 1.0)
>>> math.modf(1.5)
(0.5, 1.0)
>>> math.modf(2.8)
(0.7999999999999998, 2.0)
>>> math.modf(3.1)
(0.10000000000000009, 3.0)
```
- log：指数函数。默认e为底数，结果为浮点数。也可以自定义底数
```
>>> math.log(4,2)
2.0
>>> math.log2(4)
2.0
>>> math.log10(100)
2.0
>>> math.log(100,10)
2.0
```
- 格式化输出：格式化输出保留有效数字,格式化输出的是字符串
```python
>>> s=format(2.345,'0.2f')
>>> s
>>> type (s)
<class 'str'>
>>> round(2.5)
2
>>> format(2.5,'0.0f')
'2'
```
- Decimal模块：在使用浮点数的时候，因为计算机是使用二进制表示，所以会出现精度问题，可以使用Deciamal模块来解决精度问题
```python
>>> a=4.2
>>> b=2.1
>>> a+b
6.300000000000001
>>> from decimal import Decimal
>>> a=Decimal('2.1')
>>> b=Decimal('4.2')
>>> a+b
Decimal('6.3')
```
- 格式化输出——format：使用format进行进制转换
```python
>>> a=20
>>> bin(a)
'0b10100'
>>> oct(a)
'0o24'
>>> hex(a)
'0x14'
>>> format(a,'b')
'10100'
>>> format(a,'o')
'24'
>>> format(a,'x')
'14'
```
### 字符串  
字符串(python2默认使用ascii编码，使用Unicode编码须在字符串前加u,python3使用unicode编码）  
a='str'  
a=u'str'  
#### 字符串表示方法
- 单引号：'str' '1'
- 双引号："str""1"
- 三引号：'''...str...''' """...str..."""
- 转义字符：“str1 \tadded tab\nstr2”
- Raw字符串：r"C:\user\administrator"(无法进行转义操作)
#### 字符串操作
##### 字符串合并
```python 
 >>> 'abc'+'def'
'abcdef'
>>> 'hello' *5
'hellohellohellohellohello'
>>> print ('-'*50)
--------------------------------------------------
>>> "aa""bb"
'aabb'
>>> 'ab''cd'
'abcd'
```
##### 字符串取值
```python 
a="text"
>>> for c in a:
...     print (c,end='')
...
text
>>> for c in a:
...     print (c,end='-')
...
t-e-x-t-
>>> 'x' in a
True
>>> text='this_is_str'
>>> text[0:4]
'this'
>>> text[5:7]
'is'
>>> text[:4]
'this'
>>> text[-3:]
'str'
>>> text[-12:-7]
'this'
>>> text[::2]
'ti_ssr'
>>> text[8:1:-2]
'ss_i'
```
##### 字符串编码转换
```
>>> ord('d')
100
>>> chr(99)
'c'
>>> ord('王')
29579
>>> chr(29579)
'王'
```
##### 字符串大小写转换

- 这里利用ascii编码进行大小写转换
```
>>> Text=""   #初始化Text
>>> text="aSdFgHjK"  
>>> for i in text:
...     i_code=ord(i)
...     if 97<=i_code and i_code<=122:
...             Text+=chr(i_code-32)
...     else:
...             Text+=i
...
>>> Text
'ASDFGHJK'
>>> for x in text:
...     x_code=ord(x)
...     if 65<=x_code and x_code<=90:
...             Text+=chr(x_code+32)
...     else:
...             Text+=x
...
>>> Text
'ASDFGHJKasdfghjk'
```
- 这里利用字符串的方法进行转换
```
>>> str='asdFGHzxcVBN'
>>> str.replace('asd','ASD')
'ASDFGHzxcVBN'
```
- 除此之外，还可以使用字符串的大小写方法进行大小写转换    

ascii编码对照表
二进制 | 十进制 |十六进制 |图形|
---|---|---|---|
0010 0000|32|20|（空格）
0010 0001|33|21|!
0010 0010|34|22|"
0010 0011|35|23|#
0010 0100|36|24|$
0010 0101|37|25|%
0010 0110|38|26|&
0010 0111|39|27|''
0010 1000|40|28|(
0010 1001|41|29|)
0010 1010|42|2A|*
0010 1011|43|2B|+
0010 1100|44|2C|,
0010 1101|45|2D|-
0010 1110|46|2E|.
0010 1111|47|2F|/
0011 0000|48|30|0
0011 0001|49|31|1
0011 0010|50|32|2
0011 0011|51|33|3
0011 0100|52|34|4
0011 0101|53|35|5
0011 0110|54|36|6
0011 0111|55|37|7
0011 1000|56|38|8
0011 1001|57|39|9
0011 1010|58|3A|:
0011 1011|59|3B|;
0011 1100|60|3C|<
0011 1101|61|3D|=
0011 1110|62|3E|>
0011 1111|63|3F|?
0100 0000|64|40|@
0100 0001|65|41|A
0100 0010|66|42|B
0100 0011|67|43|C
0100 0100|68|44|D
0100 0101|69|45|E
0100 0110|70|46|F
0100 0111|71|47|G
0100 1000|72|48|H
0100 1001|73|49|I
0100 1010|74|4A|J
0100 1011|75|4B|K
0100 1100|76|4C|L
0100 1101|77|4D|M
0100 1110|78|4E|N
0100 1111|79|4F|O
0101 0000|80|50|P
0101 0001|81|51|Q
0101 0010|82|52|R
0101 0011|83|53|S
0101 0100|84|54|T
0101 0101|85|55|U
0101 0110|86|56|V
0101 0111|87|57|W
0101 1000|88|58|X
0101 1001|89|59|Y
0101 1010|90|5A|Z
0101 1011|91|5B|[
0101 1100|92|5C|\
0101 1101|93|5D|]
0101 1110|94|5E|^
0101 1111|95|5F|_
0110 0000|96|60|`
0110 0001|97|61|a
0110 0010|98|62|b
0110 0011|99|63|c
0110 0100|100|64|d
0110 0101|101|65|e
0110 0110|102|66|f
0110 0111|103|67|g
0110 1000|104|68|h
0110 1001|105|69|i
0110 1010|106|6A|j
0110 1011|107|6B|k
0110 1100|108|6C|l
0110 1101|109|6D|m
0110 1110|110|6E|n
0110 1111|111|6F|o
0111 0000|112|70|p
0111 0001|113|71|q
0111 0010|114|72|r
0111 0011|115|73|s
0111 0100|116|74|t
0111 0101|117|75|u
0111 0110|118|76|v
0111 0111|119|77|w
0111 1000|120|78|x
0111 1001|121|79|y
0111 1010|122|7A|z
0111 1011|123|7B|{
0111 1100|124|7C|\|
0111 1101|125|7D|}
0111 1110|126|7E|~
#### 字符串方法
##### 字符串大小写相关的方法
- capitalize()：字符串首字母大写
```python
>>> str='hello world'
>>> str.capitalize()
'Hello world'
```
- title()：字符串中单词的首字母大写
```python
>>> str.title()
'Hello World'
```
- upper()：字符串转换成大写
```python
>>> str.upper()
'HELLO WORLD'
``` 
- lower()：字符串转换成小写
```python
>>> str.lower()
'hello world'
```
- swapcase()：字符串大小写互转
```python
>>> str='HellO wORld'
>>> str.swapcase()
'hELLo WorLD'
```
##### 字符串排版相关的方法
- center()：居中对齐
```python
>>> str='hello'
>>> str.center(11)
'   helloo  '
>>> str.center(11,'_')
'___helloo__'
```
- ljust()：居左对齐
```python
>>> str.ljust(11,'_')
'helloo_____'
>>> str.ljust(11)
'helloo     
```
- rjust()：居右对齐
```python
>>> str.rjust(11)
'     hello'
>>> str.rjust(11,'_')
'_____hello'
```
 - expandtabs()：修改tab空格的个数
 ```python
 >>> str='hello\tworld'
>>> print (str)
hello   world
>>> str.expandtabs(9)
'hello    world'
>>> str.expandtabs(4)
'hello   world'
 ```
 - zfill()：将字符串扩充到指定长度，前面使用0填充
 ```python
 >>> str.zfill(20)
'000000000hello\tworld'
 >>> 'sad'.zfill(10)
'0000000sad'
 ```
 - strip()：删除字符串两边(左边lstrip或右边rstrip)的指定字符（默认为空格和换行符）
 ```python
 >>> str='   hello world   '
>>> str.strip()
'hello world'
>>> str.lstrip()
'hello world   '
>>> str.rstrip()
'   hello world'
>>> str='hello,world'
>>> str.strip('h')
'ello,world'
>>> str.strip('[held]')
'o,wor'
 ```
##### 字符串查找相关的方法
 - startswith(prefix[,start[,end]])/endswith(suffix[,start[,end]])  判断是否以特定字符串开头或者结尾
```python
>>> str='hello,world'
>>> str.startswith('hello')
True
>>> str.startswith('hello',0,5)
True
>>> str.startswith('hello',1,5)
False
>>> str.endswith('rld',8)
True
>>> str.endswith('rld',9)
False
>>> str.endswith('rld',8,11)
True
```   
- count(sub[,start[,end]])：相应字符串在文本中的个数
```python
>>> str='hello,world'
>>> str.count('l')
3
>>> str.count('ll')
1
```
- find/rfind()：分别从字符串前后开始查找第一个匹配到的字符串的位置,找不到就返回-1
```python
str='hello,world'
>>> str.find('l')
2
>>> str.rfind('l')
9
```
- index/rindex()：与find方法类似，但是找不到会报错
```python
>>> str.index('l')
2
>>> str.rindex('l')
9
>>> str.index('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> str.find('a')
```
- replace(old,new[,count])：替换字符串，count代表替换个数
```python
>>> str.replace('l','L')
'heLLo,worLd'
>>> str.replace('l','L',1)
'heLlo,world'
```
##### 格式判断相关方法
- isalpha() ：判断是否是字母
- isdigit()：判断是否是数字
- isalnum()：判断是否是数字和字母
- islower()：判断是否有字母，且字母为小写字母
- isupper()：判断是否有字幕，且字母为大写字母
- isspace()：判断是不是只有空格和换行符号
- istitle()：判断字符串每个单词的首字母是否大写
- isdecimal()：判断是不是数字
- isnumeric()：判断是不是数字
- isidentifier()：判断字符能否成为标识符
- isprintable()：判断字符是否全部能打印的  

>isdigit、isdecimal、isnumeric三者的区别
>isdigit()
>True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
>False: 汉字数字
>Error: 无

>isdecimal()
>True: Unicode数字，，全角数字（双字节）
>False: 罗马数字，汉字数字
>Error: byte数字（单字节）

>isnumeric()
>True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
>False: 无
>Error: byte数字（单字节）
##### 字符串分隔
- split([sep[,maxsplit]])/rsplit([sep[,maxsplit]])：分别从左右按照sep字符串分隔，最多分隔maxsplit此，默认无数次
```
>>> str='asd,fgh,jkl'
>>> str.split(',')
['asd', 'fgh', 'jkl']
>>> str.rsplit(',',1)
['asd,fgh', 'jkl']
```
- splitlines()以\n或者\r或者\n\r分隔
```python
>>> str='asd\nfgh\njkl'
>>> str.splitlines()
['asd', 'fgh', 'jkl']
```
- partition(sep)：将分隔符也作为一个元素列出来
```python
>>> 'http://www.baidu.com'.partition('://')
('http', '://', 'www.baidu.com')
```
##### 字符串其他方法
- join()：以特定的分隔符将字符串分隔
```python
>>> str='asdfg'
>>> '-'.join(str)
'a-s-d-f-g'
```

#### 字符串格式化输出
python字符串格式化输出的三种方式  
1. 使用字符串格式格式化操作符——百分号%
2. 使用字符串方法 format
3. 使用 f-strings进行字符串格式化
##### 使用%进行格式化
这种格式化表达式类似于C语言

| 格式化操作符（%）   |  说明 |  
| :--------: | :--------:|
| s   | 获取传入对象的str方法的返回值，并将其格式化到指定位置  | 
|r|与s一样，但输出方式是repr方式，而不是str
|c|整数：将数字转换成其unicode对应的值，10进制范围为 0<=i<=1114111（py27则只支持0-255）；字符：将字符添加到指定位置 
|d|有符号十进制（整数），将整数、浮点数转换成十 进制表示，并将其格式化到指定位置  
|i|有符号整数
|u|无符号整数
|o|将整数转换成八 进制表示，并将其格式化到指定位置
|x|将整数转换成十六进制表示，并将其格式化到指定位置  
|X|与x一样，A-F是大写
|e|浮点指数，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
|E|与e一样，E为大写
|f|将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
|F|浮点数十进制
|g|浮点e或f，自动调整将整数、浮点数转换成 浮点型或科学计数法表示
|G|浮点E或F，自动调整将整数、浮点数转换成 浮点型或科学计数法表示
|%|当字符串中存在格式化标志时，需要用 %%表示一个百分号
> 注：Python中百分号格式化是不存在自动将整数转换成二进制表示的方式   
 
举例
```python
>>> "%s|%r|%c" %("this is str","this is repr","C")
"this is str|'this is repr'|C"
>>> "%d|%i|%o|%x|%X|" %(3,5,12,13,14)
'3|5|14|d|E|'
>>> "%e|%E|%f|%F|%g|%G" %(1.5E3,1.5e3,13.5,13.5,1.5e13,13.5E15)
'1.500000e+03|1.500000E+03|13.500000|13.500000|1.5e+13|1.35E+16'
>>> "%(string)-10s"%({'string':'1'})
'1 
>>> "%(float)+10.2F"%({'float':3.1})
'     +3.10'
>>> "%(float)-10.2f"%({'float':3.1})
'3.10      '
```

##### 使用format方法 
语法：{}.format(value)  
参数:
（value):可以是整数，浮点数，字符串，字符甚至变量。  
Returntype：返回一个格式化字符串，其值在占位符位置作为参数传递。
```python
#位置参数
>>> username='wanger'
>>> password=123456
>>> print ("{}'s password is {}".format(username,password))
wanger's password is 123456  

>>> username='wanger'
>>> password=123456
>>> print ("{1}'s password is {0}".format(password,username))
wanger's password is 123456 
 
#下标参数
>>> si=['KB','MB','GB','TB','PB','EB','ZB','YB']
>>> '1000{0[0]}=1{0[1]}'.format(si)
'1000KB=1MB'

#浮点数精度
>>> '{:.4f}'.format(3.1415926)
'3.1416'
>>> '{:>10.4f}'.format(3.1415926)
'    3.1416'

>>> 'this is a test {t[0]}'.format(t='hello')
'this is a test h'
>>> 'this is a test {t[1]}'.format(t='hello')
'this is a test e'

#使用模块作为参数
>>> import sys
>>> sys.platform
'win32'
>>> "{0.platform}".format(sys)
'win32'
>>> 'my laptop platform is {s}'.format(s=sys.platform)
'my laptop platform is win32'
>>> 'my laptop platform is (s.platform)'.format(s=sys)
'my laptop platform is (s.platform)'

#关键字参数
>>> 'my name is {name} ,age is {age}'.format(name='wanger',age='25')
'my name is wanger ,age is 25

```  
当占位符{}为空时，Python将按顺序替换通过str.format（）传递的值。  
str.format（）方法中存在的值本质上是元组数据类型，元组中包含的每个单独值都可以通过索引号调用，索引号以索引号0开头。  
第三段代码的变量si是一个列表，{0}就代表format()方法的第一个参数，那么{0[0]}就代表列表的第一个元素，{0[1]}就代表列表的第二个元素  
这个例子说明格式说明符可以通过利用（类似） Python 的语法
访问到对象的元素或属性。这就叫做复合字段名 (compound field names) 。  

以下复合字段名都是“ 有效的 ” 。   
•  使用列表作为参数，并且通过下标索引来访问其元素（跟上
一例类似）  
•  使用字典作为参数，并且通过键来访问其值  
•  使用模块作为参数，并且通过名字来访问其变量及函数  
•  使用类的实例作为参数，并且通过名字来访问其方法和属性  
•  以上方法的任意组合  
###### format_spec参数
表达式：format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
- fill ::=  <'any character'>
- align ::=  "<"'左对齐' | ">"‘右对齐’ | "="‘在数字里，符号左对齐，数字右对齐 | "^"‘居中’
- sign  ::=  "+" | "-" | " "（当sign=’+‘时，即使是正数也会显示符号，-只有为负数的时候才显示负号，为空格时，会在正数前面留下符号位）
- width ::=  integer  (定义输出的宽度)

fill和align以及后面的width相当于str方法中的center，ljust,rjust 
```python
>>> '{:+^15}'.format('start')
'+++++start+++++'
>>> '{:+^15}'.format('end')
'++++++end++++++'
>>> '{:*<15}'.format('end')
'end************'
>>> '{:*>15}'.format('start')
'**********start'
>>> '{:=+20}'.format(10)
'+                 10'
>>> print("{:=10}\n{:=+20}\n{:-^10}\n{:=-13}".format(10,10,'-',-15))
        10
+                 10
----------
-          15
```
- \#只有在数字显示里，显示二进制数，八进制数，十六进制数的时候，需要显示前面的0b,0o,0x的时候才会用到
```python
>>> "{0:8b},{0:8o},{0:8x}".format(10)
'    1010,      12,       a'
>>> "{0:b},{0:o},{0:x}".format(10)
'1010,12,a'
>>> ("{0:#8b},{0:#8o},{0:#8x}".format(10))
'  0b1010,    0o12,     0xa'
```
- ,符号是表示数字时每三位中间加，
```python
>>> '{:,}'.format(100000000000)
'100,000,000,000'
```
- 0是固定宽度前面补0
- .precision ::=  integer(精度显示)
```
>>> '{:010.5}'.format(3.1415926)
'00003.1416'
```
- type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"  (跟之前使用%表示的相等)
&ensp;&ensp;- 当为字符时：使用s，默认就是s
&ensp;&ensp;- 当为整数时：b,o,x和X是二进制、八进制、十六进制，c是数字按Unicode转换成字符，d是正常十进制，默认就是d。也可以使用n来代替d
```python
>>> "{0:d},{0:b},{0:o},{0:x},{0:X}".format(10)
'10,1010,12,a,A'
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- 为浮点数时：e和E是指数，f和F是浮点数。g和G是同一的，也可以使用n来代替g, %是显示百分比
```python
>>> "{0:e},{0:F},{0:g},{0:n},{0:%}".format(10.3)
'1.030000e+01,10.300000,10.3,10.3,1030.000000%'
```

##### 使用f-strings方法进行格式化
f-strings也称为“格式化字符串文字”，f字符串是f在开头有一个字符串文字，其中以 {} 包含的表达式会进行值替换。表达式在运行时进行评估，然后使用__format__协议进行格式化。其中以 {} 包含的表达式会进行值替换。
###### 特点
1. 代码简洁，没有多余的引号
2. 括号{}里面的变量，可以是字符串类型，也可以是整型、浮点型，或者是复杂类型，比如数组、词典等，会自动转换成成字符串形式。
3. 括号{}里面还可以是函数，比如 f'数组a的长度为:{len(a)}'。一句话，只要是位于 {} 中的，都会当做 python 代码来执行。但里面只能写表达式，不能写执行语句如{a=2}之类的。
4. f-string在本质上并不是字符串常量，而是一个在运行时运算求值的表达式，速度非常快

简单举例
```
>>> name='wanger'
>>> age=25
>>> f"hello,I'm {name},my age {age} "
"hello,I'm wanger,my age 25 "
#也可以使用大写F
>>> F"hello, I'm {name},my age {age} "
"hello, I'm wanger,my age 25 "
```
当然也可以进行简单的计算
```
>>> f"{2*3}"
'6'
```
也可以调用函数
```
>>> def test(input):
...     return input.lower()
...
>>> name='WangEr'
>>> f"{test(name)} is funny"
'wanger is funny'
```
还可以选择直接调用方法
```python
>>> name='WangEr'
>>> f"{name.lower()} is funny"
'wanger is funny'
```
在使用字典的时候。如果要为字典的键使用单引号，请记住确保对包含键的f字符串使用双引号。
```
comedian = {'name': 'wanger', 'age': 25}
f"The comedian is {comedian['name']}, aged {comedian['age']}."
'The comedian is wanger, aged 25.'
```
#### 使用字符串的场景
- 使用多个界定符分隔字符串
split只能使用单一字符串，如果要使用多个分隔符的话，就要用到正则表达式模块了
```
>>> str='asd,dfg;zxc ert  uio'
>>> import re
>>> re.split(r'[;,\s]\s*',str)
['asd', 'dfg', 'zxc', 'ert', 'uio']
```
[]表示里面字符任意匹配。[;, ]表示；或者，或者空格，\s*表示任意个前面字符

- 字符串开头或结尾匹配
比如要看一个地址是否是http://或者ftp://开头
或者查看文件后缀是不是TXT格式
可以这样查看
```python
>>> url='http://www.baidu.com'
>>> ftp='ftp://www.baidu.com'
>>> url.startswith(('http://','ftp://'))
True
>>> txt='ziyuan.txt'
>>> txt.endswith('txt')
True
>>> url[0:7]=="http://" or url[0:6]=="ftp://"
True
>>> txt[7:10]=="txt"
True
```
- 用shell通配符
我们还可以使用shell通配符来检查文件的结尾，这需要用到fnmatch模块
fnmatch不区分大小写，fnmatchcase是区分大小写的
```python
>>> from fnmatch import fnmatch,fnmatchcase
>>> fnmatch('log.txt','*.txt')
True
>>> fnmatch('log.TXT','*.txt')
True
>>> fnmatchcase('log.TXT','*.txt')
False
>>> fnmatchcase('log.TXT','*.TXT')
True
```
- 匹配和搜索特定格式的文本
普通匹配可以使用find方法，如果是特定格式的话还是会用到正则模块
```python
>>> date1='2018/10/24'
>>> date2='2018/12/21'
>>> date3='2018-12-05'
>>> def isdate(date):
...     if re.match(r'\d+/\d+/\d+',date):
...             print ('match OK')
...     else:
...             print ('not match')
>>> isdate(date1)
match OK
>>> isdate(date2)
match OK
>>> isdate(date3)
not match
```
在正则模块re中\d表示单个数字，+表示一个或多个前面的字段

- 搜索和替换特定的文本格式
普通的匹配可以使用replace方法，如果匹配特定格式，还是要用正则模块re
```python
>>> import re
>>> date='today is 13/12/2018'
>>> re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\2-\1',date)
'today is 2018-12-13'
>>> datepat=re.compile(r'(\d+)/(\d+)/(\d+)')   #为了防止每次都要定义匹配模式，可以在这里定义一个匹配的变量，以后匹配直接调用这个变量
>>> datepat.sub(r'\3-\2-\1',date)
'today is 2018-12-13'
>>> date='yestory is 12/12/2018,today is 13/12/2018'
>>> datepat.subn(r'\3-\2-\1',date)
('yestory is 2018-12-12,today is 2018-12-13', 2)
```
\1,\2,\3分别代表前面匹配模式中的第一个括号匹配到的，第二个括号匹配到的，第三个括号匹配到的，使用subn方法可以看到匹配到几次

- 忽略大小写的搜索替换
如果要忽略大小写还是要用到re模块，需要用到的是re的IGNORECASE方法
```python
>>> import re
>>> re.findall('replace','Replace,replace,REPLACE')
['replace']
>>> re.findall('replace','Replace,replace,REPLACE',flags=re.IGNORECASE)
['Replace', 'replace', 'REPLACE']
>>> str='Replace is the same as REPLACE'
>>> re.sub('replace','WORD',str,flags=re.IGNORECASE)
'WORD is the same as WORD'
```
 
- 最短匹配模式
用正则表达式匹配某个文本模式，而他找到的是最长匹配，如果要匹配最短字符，可以用下面的方法
```
>>> strpat=re.compile(r'\"(.*)\"')
>>> text='this is my "name"'
>>> strpat.findall(text)
['name']
>>> text='this is my "name" and this is my "age"'
>>> strpat.findall(text)
['name" and this is my "age']
>>> strpat=re.compile(r'\"(.*?)"')
>>> strpat.findall(text)
['name', 'age']
```

- 删除字符串中不需要的字符
去掉字符串开头，中间或者结尾不想要的字符串，比如空白
```python
>>> s='hello world \n'
>>> s.strip()
'hello world'
>>> s.lstrip()
'hello world \n'
>>> s.rstrip()
'hello world'
>>> import re
>>> re.sub(r'\s+','',s)
'helloworld'
```

- 合并拼接字符串
```
>>> a='hello'
>>> b='world'
>>> a+' '+b
'hello world'
>>> '{} {}'.format(a,b)
'hello world'
>>> ' '.join([a,b])
'hello world'
>>> a=print(a,b)
hello world
```
