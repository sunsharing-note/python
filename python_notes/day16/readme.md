 ##### 成员修饰符

 ```
__表示私有 不能直接被外部所访问 私有字段 私有方法
 ```

 ##### 特殊成员

 ```
 __init__
 __call__
 __int__
 __str__
 __add__
 __del__ 析构方法：对象被销毁时自动执行
 __dict__ 将对象中封装的所有内容以字典方式返回
 __getitem__ 切片或者索引
 __setitem__
 __delitem
 ```

 ##### metaclass 类的祖宗

 ```
在python里，一切事物都是对象
type("类名",(object,),func....)
 ```

 ##### 异常处理和反射

 ```
 try exception finally

 反射：
 getattr hasattr setattr delattr
```
##### 单例模式

```
单例：用于使用同一份实例（对象）
```