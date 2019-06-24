##### xml中节点Element类的函数

- tag                   当前节点标签名
- attrib                当前节点属性
- text                  当前节点内容
- append                添加一个子节点
- clear                 清空节点
- extend                为当前节点添加 n 个子节点
- find                  获取第一个寻找到的子节点
- findall               获取所有的子节点
- findtext              获取第一个寻找到的子节点的内容
- get                   获取当前节点的属性
- insert                在当前节点创建子节点，然后插入指定位置
- items                 获取当前节点的所有属性，和字典中的items一样，内容都是健值对
- iter                  在根据节点名称寻找所有指定的节点，并返回一个迭代器
- iterfind              获取所有指定的节点，并放在一个迭代器中
- itertext              在子孙中根据节点名称寻找所有指定的节点的内容，并返回一个迭代器
- keys                  获取当前节点的所有属性的 key
- makeelement           创建一个新节点
- remove                删除某个节点
- set                   设置当前节点属性