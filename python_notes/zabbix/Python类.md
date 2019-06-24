## Python类
### 为何使用类
- 通过类来实现程序逻辑，就可以建立其实际结构和关系的模型
- 比如：一只狗在跑：
&ensp;- 继承：狗是动物的一种，可以继承所有动物的特性：
&ensp;&ensp;- 出生时间，存活状态等等
&ensp;- 组合：
&ensp;&ensp;- 狗是哺乳动物，陆地行走的动物。因此又这两种特性。
&ensp;&ensp;&ensp;- 作为哺乳动物有性别之分，父母子女等属性。
&ensp;&ensp;&ensp;- 作为陆地行走动物，可以有走，跑，站，坐等属性。
&ensp;- 然后我们再生成一个狗类，所有的狗相关的特性，再添加进去，这样当我们定义一个变量后，什么都不做就有这些基本特性了。
### OOP属性继承搜索
- python当中的OOP相比其他语言简单
- 关于属性继承顺序和搜索方式：查找当前，查找先继承的，查找其他。
- 比如：我们有类C1，定义a=10,b=20,c=30。有类C2，定义a=15。类C3继承成组合了类C1，C2，定义了b=25
- 这个时候，我们要是继承的顺序是C1，C2：C3的a=10,b=25,c=30
- 要是继承的顺序是C2,C1：C3的a=15,b=25,c=30
```python
>>> class c1:
	 a=10
	 b=20
	 c=30

>>> class c2:
	 a=15

>>> class c3(c1,c2):
	 b=25
>>> c3.a
10
>>> c3.b	 
25
>>> c3.c	 
30
```
### OOP类和实例
实例可以继承累的特性：跟之前说的，我们可以定义类：狗，我们也可以生成单独的的实例：其中一只狗。
class dog: ...
dog1=dog()
这个意味着dog1是独立的实例，属于“狗”这个类，默认拥有狗的所有属性
```python
>>> class dog:
	 name=''
	 def run(self):
		 print('{} is running'.format(self.name))
	 
>>> dog1=dog()
>>> dog1.name='d1' 
>>> dog2=dog()
>>> dog2.name='d2'
>>> dog1.run()
d1 is running
>>> dog2.run()
d2 is running
```
### 类方法调用
当我们生成实例后，可以通过实例.方法的方式调用类的方法
比如类dog里，有跑（run()）的方法：dog1可以使用dog1.run()来调用此方法，也可以生成其他方法
### OOP代码重用
因为所有的事里默认有类的所有属性（变量，方法等），因此代码可以重用。
- 如果没有OOP：我们要编写100只狗，每只狗都是单独的代码，每只狗的共性也需要重复写；我们有100种类型的动物，每种动物的特性都得重新写。
- 如果有OOP：我们可以定义类，实例可以默认继承相同特性

### 类对象提供默认行为
- class语句创建类对象，将其引用到一个变量，此语句类似def
- class语句内的赋值语句会生成一个属性，这里的赋值语句包含def
- 类属性提供对象的状态和对象
```python
>>> class c1:
	 a=1

>>> class c1:
	 def func(self):
		 print('this is class func')
>>> c1().func()	 
this is class func
```
### 实例元素是具体的元素
- 像函数那样调用类会创建新的实例对象，每次类调用时，会生成一个新的实例对象。
- 每个实例对象继承类的属性并获得了自己的命名空间，由类创建的实例对象是新命名空间，对继承创建该实例的类对象的属性
- 在方法内对self属性做赋值运算会产生每个实例自己的属性，在类方法函数内，第一个参数会引用正处理的实例对象（self），对self属性做赋值运算会创建或修改实例内的数据，而不是类的数据
```python
>>> class c1:
	 name=''
	 def func(self):
		 print(self.name)
>>> a=c1()
>>>> a.name='dog'
>>> a.func() 
dog
```
#### 初始化实例
```python
>>> class c1:
	 name=[]
#未初始化实例时，a和b的指向的是同一个对象 
>>> a=c1()	 
>>> b=c1()
>>> a.name is b.name
True
>>> a.name.append(1)
a.name
>>> a.name
[1]
>>> b.name
[1]

初始化实例之后，a与b指向的不是同一个对象了
>>> class c1:
	 def __init__(self):
		 self.name=[]
>>> a=c1()	 
>>> b=c1()
>>> a.name is b.name 
False
>>> a.name.append(1)
>>> b.name
[]
>>> a.name 
[1]
```
### 类通过继承可以定制
- 超类列在了类开头的括号中
&ensp;例如：class subclass(class):
- 类从超类中继承属性
- 实例会继承所有可读取累的属性
&ensp;&ensp;实例查找类的属性时，会从创建该实例的类开始查找，之后是第一个超类，第二个超类。在超类查找也是相同顺序
- 每个实例.属性都会开启新的独立搜索
- 逻辑的修改是通过创建子类，而不是修改超类
```python
>>> class c1:
	 def myprint(self):
		 print(self.name)
>>> a=c1()
>>> a.myprint()	 
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    a.myprint()
  File "<pyshell#165>", line 3, in myprint
    print(self.name)
AttributeError: 'c1' object has no attribute 'name'
>>> class c2(c1):
	 def setname(self,name):
		 self.name=name
>>> a=c2()
>>> a.setname('myname')
>>> a.myprint()
myname
```
### 类可以截获Python运算符
- 以下划线命名的方法(`__函数名__`)是特殊的钩子，python运算符重载是通过特殊命明方法来实现的。例如：`__add__`
- 当实例出现在内置运算符时，这类方法会自动调用：实例对象+其他对象，会调用`__add__`方法
- 类可覆盖多数内置类型运算符
- 运算符覆盖方法没有默认值，而且也不需要
- 常见的有：
&ensp;&ensp;-  `__add__=+`
&ensp;&ensp;- `__sub__=-`
&ensp;&ensp;- `__str__`打印等字符串操作时
&ensp;&ensp;- `__mul__=*`
```python
>>> class c1:
	 var1=1
	 var2='asdfg'
	 def __add__(self,value):
		 return self.var1 + value
	 def __sub__(self,value):
		 return self.var1 - value
     def __str__(self):
		 return self.var2

>>> a=c1()
>>> a.var1
1
>>> a +3 
4
>>> a.var1=4
>>> a-1 
3	 
>>> a.var2	 
'asdfg'
>>> print(a)
asdfg
```
### 类与字典的关系
```python
>>> class jack:
	 name=''
	 age=0
	 birth=None
	 def __init__(self):
		 self.name='a'

>>> a=jack()
>>> a.name
'a'
>>> a.age 
0
>>> a.birth
>
```
### 类接口技术
- super：超类，定义所有子类都需要的变量（方法）
- Inheritor：完全继承，没有任何修改的子类
- Replacer：继承超类后，修改一些变量（方法）的子类
- Extender：在继承超类的基础上，自己添加了其他变量(方法)的子类
- Provider：在继承超类后，超类里的某些调用没有定义，此类型会定义此类型
### 运算符重载
- `__init__`：构造函数     调用类来创建实例时调用
```python
>>> class c1:
	 def __init__(self):
		 self.name='a'

>>> a=c1()
>>> a.name
'a'
>>> a.name='b'
>>> a.name
'b'

>>> class c1:
	 def __init__(self,name):
		 self.name=name

>>> a=c1('d')
	 
>>> a.name
	 
'd'
```
- `__del__`：析构函数        对象回收时使用
```python
>>> class c1:
	 def __del__(self):
		 print('del')

>>> a= c1()
>>> del a
del
>>> a
	 
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    a
NameError: name 'a' is not defined
```
- `__add__`：运算法+          有加法运算时使用
```python
>> class c1:
	 def __add__(self,value):
		 return self.value+value

>>> a=c1()
>>> a.value=2
>>> a+2
4
>>> a+2+2
6
```
- `__or__`：运算符or
- `__repr__`,`__str__`：打印，转换   repr,print,str时调用
- `__call__`：函数调用    实例当做函数使用时使用
```python
>>> class c1:
	 def __call__(self):
		 print('callable')
	 
>>> a=c1()	 
>>> a()
callable
```
- `__getattribute__`,`__setattr__`,`__delattr__`：默认存在。获取，设置，删除属性时使用
```python
>>> class c1:
	 pass
	 	 
>>> a=c1()
>>> a.__setattr__('a','b')	 
>>> dir(a) 
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a']
>>> a.__getattribute__('a') 
'b'
>>> a.__delattr__('a')	 
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
- `__getitem__`,`__setitem__`,`__delitem__`：操作游标
```python
>>> class c1:
	 name={}
	 def __getitem__(self,index):
		 return self.name[index]
	 def __setitem__(self,index,value):
		 self.name[index]=value
	 def __delitem__(self,index):
		 del self.name[index]

>>> a=c1()
>>> a['first']='1'
>>> a.name
{'first': '1'}
>>> a['first'] 
'1'
>>> del a['first']
>>> a.name	 
{}
```
- `__len__`,`__bool__`：调用len函数/bool函数时获取的信息
```python
>>> class c2(c1):
	 def __init__(self):
		 self.name={}
	 def __len__(self):
		 return len(self.name)

>>> a=c2()
>>> a['first']='1'
>>> a.name
{'first': '1'}
>>> len(a)	 
1
```
- `__lt__`,`__gt__`,`__le__`,`__ge__`,`__eq__`,`__ne__`：有比较运算的时候调用
```python
>>> class c3(c2):
	 value=1
	 def __lt__(self,value):
		 return self.value < value
	 def __gt__(self,value):
		 return self.value > value

>>> a=c3()
>>> a>2
False
>>> 0<a
True
>>> a>0	 
True
```
- `__radd__`：运算符+   与`__add__`相近，但实例在后面
```python
>>> class c4(c3):
	 def __rsub__(self,value):
		 return value - self.value
 
>>> a=c4()
>>> 1-a 
0
```
- `__iter__`,`__next__`：迭代器     当做迭代器使用
```python
>>> class c6(c5):
	 def __iter__(self):
		 return iter(self.name)

>>> a=c6()
>>> a['first']='1'	 
>>> a['second']='2'
>>> for i in a:
	 print (a[i],end=',')
	 
1,2,
```
- `__contains__`：包含  查看某个对象是否存在实例里
```python
>>> class c5(c4):
	 def __contains__(self,value):
		 return value in self.name

>>> a=c5()
>>> a.name
{}
>>> a.name['first']=1
>>> 'first' in a.name
True
>>> '2' in a.name 
False
```

