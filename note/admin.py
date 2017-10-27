# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post
from account.models import Profile

# Register your models here.

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper



class PostAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'user_name', 'get_created')
    list_filter = (('created', custom_titled_filter('创建时间')),('author__name', custom_titled_filter('姓名')))
    search_fields = ('title', 'summary')
    #raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['created']
    
    # 显示用户邮箱地址
    def user_name(self, obj):
        return u'%s' % obj.author.name
    user_name.admin_order_field = 'author' # 允许以该字段排序    
    user_name.short_description = u'姓名'    
    
    def get_title(self,obj):
        return u'%s' % obj.title      
    get_title.short_description = u'标题'  
    
    def get_created(self,obj):
        return u'%s' % obj.created
    get_created.admin_order_field = 'created'        
    get_created.short_description = u'创建时间'
    

admin.site.register(Post, PostAdmin)
