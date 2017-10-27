# -*- coding:utf-8 -*-
from django import forms

from .models import Post


class New_Post_Form(forms.Form):
    title = forms.CharField(label='题目', max_length=100)
    summary = forms.CharField(label="实验总结",widget=forms.Textarea(attrs={'style': 'height:200px;width:500px'}),required=None)
    #file=forms.FileField(label='上传文件',required=None)    
    #image=forms.ImageField(label='上传图片',required=None)


    class Meta:  
        model = Post 
        fields = ('title', 'summary',)   # 'image', 'file'，
    
 




