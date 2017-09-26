#coding=utf-8
from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.
class TagInline(admin.TabularInline):
    model=Tag
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')#列表中要显示的字段
    search_fields=('name',)#在列表页面添加要搜索字段
    inlines=[TagInline]#Inline
    # fields=('name','email')
    fieldsets=(
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',),#css
            'fields':('age',),
        }]
    )
admin.site.register(Contact,ContactAdmin)#只显示 name和email这两个字段
admin.site.register([Test,Tag])#注册自定义模块
