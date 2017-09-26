#coding=utf-8
from django.http import HttpResponse
from TestModel.models import Test

#数据库操作
def testdb(request):
    #初始化
    response=""
    response1=""
    #通过objects这个模型管理器的all()获取所有数据行，相当于SQL中的select * from
    list=Test.objects.all()
    #filter相当于SQL中的where,可以设置条件过滤结果
    response2=Test.objects.filter(id=1)
    #获取单个对象
    response3=Test.objects.get(id=1)
    #限制返回的数据，相当于SQL中的offset 0 limit2;
    Test.objects.order_by('name')[0:2]
    #数据排序
    Test.objects.order_by('id')
    #上面的方法也可以连锁使用
    Test.objects.filter(name="runoob").order_by('id')
    #修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test2=Test.objects.get(id=1)
    test2.name='Google'
    test2.save()
    #另一种方法
    #Test.objects.filter(id=1).update(name='Google')
    #修改所有的列
    #Test.objects.all().update(name='Google')
    #删除数据
    # Test.objects.all().delete()
    #输出所有数据
    for var in list:
        response1+=var.name+" "
    response=response1
    return HttpResponse("<p>"+response+"</p>")
    # test1=Test(name='runoob')
    # test1.save()
    # return HttpResponse("<p>数据添加成功！</p>")
