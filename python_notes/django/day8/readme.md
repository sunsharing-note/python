```
数据库操作:
    - 单表操作
    - filter
        models.tb.objects.filter(id=123)
        dic = {"id": 123,"age__gt": 3}
        models.tb.objects.filter(**dic)
    - count
    - order_by
    - 一对多
        class province(models.Model):
        name = models.CharField(max_length=32)
        nid = models...
        class city(models.Model):
        name = models.CharField(max_length=32)
        pro = models.ForeignKey("province",to_filed="nid")
        正向查找
        models.city.objects.all()
        models.city.objects.all().values()
        models.city.objects.all().value_list()
        反向查找
    - 多对多
    class Book(models.Model):
        name =
    class Author(models.Model):
        name = 
    # 或者使用这种方式：
        m = models.ManyToMany.field("Book")
    """ #自己创建第三张表
    class a_to_b(models.Model):
        bid = ForeignKey(Book)
        aid = ForeignKey(Autyor)
        class Meta:
            unique_together = (
                ("bid","aid"),
            )"""
```