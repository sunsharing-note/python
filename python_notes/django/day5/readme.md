* 日志


```
----ORM
    单表
    关联表
         一对一 OneToOne
         一对多 ForeignKey
         多对多 ManyToMany
    操作表
         增  create
                models.Book.objects.create(title="",name="")

                dic = {"title":tile,"name":name}
                models.Book.objects.create(**dic)

            如果有foreignkey：
            一对多
                1.models.Book.objects.create(title=title,name=name,publisher_id=2)
                # 推荐2这种
                2.models.Book.objects.create(title=title,name=name,publisher=obj)
            多对多
                # 正向查询
                book = models.Book.objects.fileter(id=2)
                author = models.Author.objects.filter(id__gt=2)
                book.author.add(*author)

                # 反向查询_set
                author = models.Author.objects.filtter(id=3)[0]
                books = models.Book.objects.filter(id__gt=2)
                author.book_set.add(*books)
             save
                方式一
                obj = Book("title":tile,"name":name)
                obj.save()
                方式二
                obj = Book()
                obj.title=""
                obj.name=""
                obj.save()
    自建第三张表
        class book2author(models.Model):
            author = models.ForerigbKey("Author")
            book = models.ForeignKey("Book")
            class Meta:
            unique_together=["author","book"]

    __gt __in __lt __in=[] __contains="" __icontaines=""（不区分大小写）
    models.Publish.objects.filter(book__title="python").values("name")
    # 无所不能的双下划线
    filter(id__gt=2,id__lt=5)
    objects.values("author__name").annotate(Sum("price"))

    F查询与Q查询
    # 所有价格加20 F查询
    models.Book.objects.all().update(price=F("price")+20)
    # Q查询：封装关键字查询
    不加|是and，加了是or
    models.Book.objects.filter(Q(id=3) | Q(title="php"))
    models.Book.objects.filter(Q(id=3) | Q(title="php"),color="red",)

# admin
1.初始化数据库
python manage.py makemigrations
python manage.py migrate
2.建用户
python manage.py createsuperuser
3.如需要注册在admin.py中注册
admin.site.register(Book)





```

