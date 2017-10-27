# -*- coding:utf -*-
from django.conf.urls import url    
from . import views    

from .views import list_post

urlpatterns = [        
    # post views        
    url(r'^list$', views.list_post, name='list_post'),
    url(r'^(?P<id>\d+)/$', views.note_details, name='note_details'),
    url(r'^create_new_post$', views.create_new_post, name='create_new_post'),
    url(r'^file_download(?P<created_time>\*+)/(?P<author_id>\d+)(?P<file_name>\*+)$', views.file_download, name='file_download'),
    ]
    
    
    
