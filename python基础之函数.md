## Python函数
函数是python为了代码最大程度的重用和最小化代码冗余而提供的最基本的程序结构。函数也是一种设计工具，使用函数，我们也可以把复杂的系统分解为可管理的部件
### 函数的意义
- 最大化代码重用和最小化代码冗余
- 流程的分解

函数的相关语句和表达式

| 语句   |  例子 | 
| :------: | :------:| 
| Calls |my_function('Fir Arg','Sec Arg')  
|def|def myfunction(fir_arg,sec_arg):
|return|return fir_arg+sec_arg
|global|global x;x=new_value
|nonlocal|nonlocal x;x=new_value
|yield|def my_sqr(x): for i in range(x): yield i **2
|lambda|funcs=[lambda x: x**2,lambda x:x*3]

### 编写函数
def是可执行的代码。在python里，只有def执行之后，才会生成相应的函数。要是def没有执行，相应的函数就不会生成。def语句在if、while语句甚至是其他def语句里也是合法的。
- def创建了一个对象，并将其赋值给一个变量。def语句是生成一个函数对象，并将其赋值给函数名变量
- lambda创建一个函数对象发送给调用者。因此，也可使用lambda表达式创建函数，这一功能允许我们把函数定义内联到语法上一条def语句不能工作的地方
- return将一个结果对象返回给调用者。这个返回值成为函数调用的结果。
- yield向调用者返回一个结果对象，但是记住他离开的地方
- global声明了一个模块级的变量并被赋值。在默认情况下，所有在函数内被赋值的变量，是在这个函数里的本地变量，并仅在函数运行过程中存在。为分配一个可以在整个模块中都可以使用的变量名，函数需要在global语句中列举出来。
-  nonlocal声明了将要赋值的一个封闭的函数变量。python3.x里才有的语句。函数里嵌套函数时，都是用相同变量名，只想继承上一个函数里的相同变量时可以使用。
-  函数是通过赋值（对象引用）传递的。参数是通过赋值传递的。但是在python中赋值就是对象引用。因此当参数被传递的对象为可变对象，当对参数进行变更时，会影响到被传递进来的变量
-  参数、返回值以及变量并不需要声明。这个与其他变量相同，不需要提前声明。

#### def语句
def语句将创建一个函数并将其赋值给一个变量名：
def <变量名>([参数1,参数2,...]):
	<语句>
def语句的首行定义函数名，并引用函数对象，函数名的本质就是函数的内存地址。
参数个数是0或以上数目。
语句里，可以包含return语句，在调用函数时，会返回一个值。当没有return时，默认返回值为None。
函数里，也可以使用yield语句来生成返回值。
因为def是执行语句，因此函数是实时生成的

```python
>>> def hanshu(x,y):
	return x*y

>>> hanshu('abc',2)
'abcabc'
>>> hanshu(2,[1,2,3])
[1, 2, 3, 1, 2, 3]
```

在这个函数里，x*y的结果取决于x和y的对象类型，因为python本身不定义变量，因此传递的值的类型与返回的类型都不一定是固定的类型。

### python作用域

作用域针对的是变量。在使用同一个变量名时，会出现作用域问题。
- 一个def内定义的变量名能够被def内部使用。不能在函数外部引用这个变量名。
- def内的变量名与def外的变量名并不冲突。在def内赋值的与def外赋值的相同变量名是不同变量。
变量名有如下三种不同作用域：
1. 全局：在def外定义的变量名是全局变量
2. 本地：在def内部定义的叫做本地变量
3. 其他：嵌套def时，各自的变量也是独立的。

#### 本地变量与全局变量

```python 
>>> x=10        #全局变量
>>> def funx():
	x=20        #本地变量
	print(x)

>>> print(x)    #打印的是全局变量
10
>>> funx()      #打印的是本地变量
20
>>> x=10
>>> def funx():
	print(x)
	#本地变量没有定义的话会引用全局的变量
>>> print(x)
10
>>> funx()
10
```

#### 作用域法则
- 内嵌的模块是全局作用域
- 全局作用域的作用范围仅限于单个文件
- 每次的函数的调用都创建了一个新的本地作用域
- 赋值的变量名除非声明全局变量或非本地变量，否则均为本地变量
- 所有其他的变量名都可以归纳为本地全局或者内置。

变量名使用时，查找顺序：
- 本地变量名——在本地是否使用此变量名赋值过
- 上一层结构中def或lambda的本地变量名——上一层是否使用此变量名赋值过
- 全局变量名——在整个文件里是否对变量名赋值过
- 内置变量名——python内部是否存在此变量名
如果找不到以上变量名则会报错

```python
>>> def newdef():
	x=20
	def newdef2():
		print(x)
	newdef2()
	
>>> newdef()
20

>>> x=10
>>> def newdef():
	def newdef2():
		print(x)
	newdef2()
	
>>> newdef()
10
```
 
#### global语句
在函数内，想改变全局变量，可以使用global语句来定义此变量为全局变量。

```python
>>> g='global'
>>> l='global'
>>> def glo():
	global g
	g='local'
	l='local'
	
>>> g
'global'
>>> l
'global'
>>> glo()
>>> g
'local'
>>> l
'global'
``` 

在glo函数里，都重新赋值了g与l,但在函数执行后只有g改变了，当使用global之后，当前函数里所使用的所有对变量g的更改都会对全局变量g进行更改。
除了这个方法，还有引用自己的方法（交互模式里，可以import __main__）与sys.modules的方法（可以使用引用过的所有模块，交互模式里本身可用__main__方式）。

```python
>>> x=10
>>> import __main__
>>> __main__.x
10
>>> def glo():
	__main__.x+=1
	
>>> glo()
>>> x
11

>>> s=10
>>> import sys
>>> sys.modules['__main__'].s
10
>>> def glo():
	sys.modules['__main__'].s+=1
	
>>> glo()
>>> s
11
```

#### 作用域与嵌套函数
被嵌套函数的作用域就是上级函数，在这里，想调用inner函数，必须是在函数outer里面，不能直接使用。可以使用返回内部函数的方法来提取内部函数：

```python
>>> def outer():
	def inner():
		print('inner')
	inner()
	
>>> func1=outer()
inner
```

##### 工厂函数
工厂函数：根据要求的对象，一个能够记住嵌套作用域的变量值的函数。
```python
>>> def printx(x):  
	def printy(y):  #嵌套函数
		return x*y  #返回x*y的值
	return printy   #返回嵌套的函数

>>> a=printx(3)    #定义x值为3后的嵌套函数赋值
>>> a(2)
6
>>> a(3)
9
``` 

#### nonlocal语句
nonlocal让内部函数中的变量在上一层及以下层函数中生效（父级级父级以下）

```python
x=1
>>> def func1():
	x=2
	def func2():
		nonlocal x
		x=3
		return x
	func2()
	print(x)

>>> func1()
3
>>> x
1
```
因为x并不是全局变量，所以只有在调用函数时nonlocal语句才会生效，这里x=3，当直接输出x而不调用函数时那么x=1

### 参数
#### 参数简介
参数：argement或parameter，对象作为输入值传递给函数的方式。
参数传递时的简要关键点：
- 参数的传递是通过自动将对象赋值给本地变量名来实现
- 在函数内部的参数名的赋值不会影响调用者
- 改变函数的可变对象参数的值也许会对调用者有影响

传递参数为可变对象与不可变对象时：
不可变对象通过值进行传递——数值、字符串等
可变对象是通过指针进行传递——列表、字典等

```python
>>> a=3
>>> def printa(a):
	a=a+1
	print(a)

>>> a
3
>>> printa(a)
4
>>> a
3
```

#### 参数传递
在这里，b[:]方式会新生成一个列表对象，因此函数里的y与setlist(b[:])是两个不同的对象。这种方法可以避免可变参数的修改。
```python
>>> def setlist(y):
	y.append(3)
	
>>> a=[1,2]
>>> setlist(a[:])
>>> a
[1, 2]
>>> setlist(a)
>>> a
[1, 2, 3]
```

参数传递是由特定匹配规则的：
- 位置：从左到右
- 关键字参数：通过参数名进行匹配
- 默认参数：为没有传入值得参数定义参数值
- 可变参数：收集任意多基于位置或关键字的参数——参数以* 或**开头
- 可变参数解包：传递任意多的基于位置或关键字的参数——传递值以* 或**开头
- Keyword-only参数：参数必须按照名称传递

> 传递参数时，要注意顺序：非关键字参数->关键字参数->字典参数

```python
>>> def myfunc(a,b):
	print(a,b)

>>> myfunc(1,2)
1 2
>>> myfunc(b=1,a=2)
2 1
```

#### 匹配语法

| 语法     | 位置 |  
| :-----: | :----:| 
|func(value)|调用者  常规参数：通过位置进行匹配| 
|func(name=value)|调用者 关键字参数：通过变量名匹配|
|func(*sequence)|调用者 迭代传递所有元素
|func(**dict)|调用者  以‘键’为关键字，‘值’为相应值的方式传递字典所有元素
|def func(name)|函数  常规参数：通过位置或变量名进行匹配
|def func(name=value)|函数 默认参数值：如果没有在调用中传递的话
|def func(*name)|函数 匹配并收集（在元组中）所有包含位置的参数
|def func(**name)|函数 匹配并收集（在字典中）所有包含关键字的参数
|def func(*arg,name)|函数 参数必须在调用中按照关键字传递

常规参数函数用法：
```python
>>> def myfunc(a,b):
	result=a+b
	print(result)

>>> myfunc(1,2)
3
```

关键字参数函数：

```python
>>> def myfunc(a,b):
	result=a+b
	print(result)

>>> myfunc(b=1,a=3)
4
```
迭代传递参数用法：
```python
>>> def myfunc(a,b,c):
	result=a+b+c
	print(result)
	
>>> myfunc(*[1,2,3])
6
```
在字典中匹配所有参数用法：
```python 
>>> def myfunc(a,b,c):
	result=a+b+c
	print(result)

>>> myfunc(**{'a':1,'b':2,'c':3})
6
>>> myfunc(1,**{'b':2,'c':3})
6
```
默认参数函数用法：
```python 
>>> def myfunc(a,b=3):
	print(a+b)
 #当有默认参数存在时，可以只传入其他的参数
>>> myfunc(3)
6
>>> myfunc(3,2)
5
```
可变参数函数用法：
可变参数，可以传递任意个参数
*args方式是把所有常规参数调用与迭代调用放进一个元组里：
```python
>>> def myfunc(*a):
	result=''.join(a)
	print (result)

>>> myfunc('1,','2,','3')
1,2,3
>>> myfunc('first,',*['second,','third'])
first,second,third
```
**args方法是把任意个关键字参数与字典调用方式存放在变量名为args的字典里
```python
>>> def myfunc(**a):
	print(a)

>>> myfunc(a='1',b='2')
{'a': '1', 'b': '2'}
>>> myfunc(a='1',b='2',**{'c':'3'})
{'a': '1', 'b': '2', 'c': '3'}
```
必须使用关键字传递的方法：
函数里的参数：
常规——有/无默认值
*args——存放在列表
**args——存放在字典
在python3开始，在*args与**args中间可以加入一个“必须使用关键字传递的参数”
使用方法为是0个或多个常规参数+*或*args+“必须使用关键字传递的参数”+0个或1个**args。
```python
>>> def myfunc(*,b,**c):
	print(b,c)

>>> myfunc(**{'b':4})
4 {}
>>> def myfun(*a,b,**c):
	print(a,b,c)

>>> myfun(2,**{'b':4,'c':5})
(2,) 4 {'c': 5}
```

特殊参数的传递：
在python里，函数也是对象，函数名也是变量名，因此函数本身也可以传递。
计算最大、最小值的函数时，一般用法：
```python
#这是一个求最小值的函数
>>> def min1(*a):
	reg=a[0]
	for i in a[1:]:
		if i <reg:
			reg=i
	print(reg)
	
>>> min1(2,3,5,1,6,8)
1
#这里将最大和最小值的函数作为参数传入到求最大和最小值的函数里
>>> def lessthan(x,y):
	return x<y

>>> def morethan(x,y):
	return x>y

>>> def minmax(test,*args):
	res=args[0]
	for i in args[1:]:
		if test(i,res):
			res=i
	print(res)

>>> minmax(lessthan,2,3,5,1,6)
1
>>> minmax(morethan,2,3,5,1,6)
6
```
### 函数的高级用法
#### 递归函数
```python
>>> def mysum(s):
	if not s:
		return 0
	else:
		return s[0]+mysum(s[1:])
#或
>>> def mysum(s):
	return 0 if not s else s[0]+mysum(s[1:])
		
>>> mysum([1,2,3,4])
10
```
嵌套列表里面的值相加
```python
>>> li=[1,2,[3,4,5],6,[7,[8,9],10]]
>>> def sumlist(a):
	sum=0
	for i in a:
		if not isinstance(i,list):  #判断遍历的i是否是列表
			sum += i
		else:
			sum += sumlist(i)
	return sum

>>> sumlist(li)
55
```
#### 函数对象：属性和注解
在python里函数也是以对象的形态出现。函数名也是以变量名形式存放。因此函数也可以跨模块，以参数传递等形式。函数对象也能调用根本无关的操作：属性存储与注释。
间接函数调用：
```python
>>> def func(x):
	print(x)
	
>>> func2=func
>>> func2(2)
2
```
把函数放进列表或元组里：
```python
>>> def myfunc(func_name,arg1):
	func_name(arg1)

>>> def func_name(arg1):
	print (arg1)
	
>>> li=[(func_name,1),(func_name,2),(func_name,3)]
>>> for i in li:
	myfunc(i[0],i[1])

1
2
3
```
#### 匿名函数：lambda
lambda会生成函数对象，但不赋值给任何变量。
lambda表达式：
lambda [`<arg1>`][,`<arg2>`][,`<arg3>`]....:expression using args
参数不是必须的，但没有参数就没有相对意义。
lambda简单说明：
lambda是一个表达式，而不是一个语句，也不是一个的代码块。——生成一个对象。
```python
>>> myfunc=lambda a:a*2
>>> myfunc(4)
8
>>> (lambda a,b:a*b)(5,4)
20
```
当我们把函数对象放进列表里等操作的时候，使用def感觉很臃肿，这时可以使用lambda来简化过程。
```python
>>> funclist=[lambda x: x**2,
	      lambda x: x**3,
	      lambda x: x**4]
>>> funclist[0](2)
4
>>> funclist[1](3)
27
```
#### 在序列中映射函数：map
使列表中的每个值都加10
```python
>>> l=[1,2,3,4]
>>> list(map(lambda x: x+10,l))
[11, 12, 13, 14]
```
#### 函数式编程工具：filter
filter与map相似，但是针对返回的bool结果判断，结果为真，保留元素；结果为假，弃用元素。结果也是保存在可迭代对象里：
```python
>>> list(filter(lambda x: x>1,[-1,0,1,2,3,4,5]))
[2, 3, 4, 5]
```
#### 函数式编程工具：reduce
reduce函数是在functools模块里的，因此我们需要导入这个函数。
这个方法是第一次从可迭代对象里提取两个元素当作函数的参数传入，按前面的函数进行运算，保存返回值，当可迭代对象里还有元素的时候，之前的返回值为第一个参数，可迭代对象里取下一个继续运算，知道可迭代对象空。最后返回函数的返回值。
```python
>>> from functools import reduce
>>> reduce(lambda x,y: x+y,[1,2,3,4])
10
>>> reduce(lambda x,y:x if x>y else y,[3,5,2,6,7,4,1,9])
9
```
