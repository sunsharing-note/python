* urls.py中path(r'api/namespace',views.namespace)的格式为：path(r"url"，对应函数，参数，url别名)参数为键值对形式
* def test(request,参数)是可以加参数的 在urls.py中使用正则表达式,如果在urls.py使用了名字，则后端在使用时需要使用同样的名字(有命url)
* form action={% url "test" %}
* python-mysql参考：https://www.cnblogs.com/yangmv/p/5327477.html https://www.cnblogs.com/wendoudou/p/mysql.html https://baijiahao.baidu.com/s?id=1581168905220720890&wfr=spider&for=pc
* 如果页面较多，全都放在urls.py中比较繁琐，建议在每个app下新建urls.py文件，并进行分发
* 引入include，并修改urls.py：path(r'^k8s',include(k8s.urls))，然后在APP下的urls.py中去做具体细分
  
1. pip install django
2. django-admin startproject mysite
3. python manage.py startapp cmdb
4. python manage.py runserver 127.0.0.1:8000  # 运行
5. 假如使用数据库： python manage.py makemigrations
6. python manage.py migrate
7. 如果使用Mysql则需要在__init__.py中添加import pymysql;pymysql.install_as_MySQLdb()