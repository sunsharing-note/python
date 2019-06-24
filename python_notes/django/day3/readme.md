* request response
* request中方法：GET POST  path COOKIES files
* render(建议使用) render_to_response
* locals()使用本地变量
* redirect 登录验证时，用redirect更好
* templates
* render(request,"index.html",{"data": user_list}) index.html叫模本 {"data": user_list}叫上下文,引入template context
* python manage.py shell
* {{变量}} 万能的句点号:. {% if %} {% endif %} {% for %} {% endfor %}{forloop.counter}
* filter:{{ obj|upper }} {{ obj|lower }} {{ obj|first|upper }} {{ obj|capfirst }}
* {{ obj|add:1 }} {{ obj|date: 'Y-m-d' }}  {{ obj|urlencode }}
* {% csrf_token %} {% with %}:用简单的变量名替代复杂的
* {% verbatim %}
* 自定义标签：在app中创建template_tags(必须这个名字)文件夹，在其下创建任意py文件
* 然后再html中引入:{% load test %}
* filter参数不能超过两个 simple_tag不能用于if
* 在html中使用extend:{% extends "base.html" %} 
* {% block name %} {endblock}
* {}
