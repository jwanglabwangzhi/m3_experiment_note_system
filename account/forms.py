# -*- coding:utf-8 -*-
from django import forms
        
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Profile


'''        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'student_id')
'''

class LoginForm(forms.Form):        
    username = forms.CharField(label='用户名（邮箱）',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    def clean(self):      
        email=self.cleaned_data["username"]
        password=self.cleaned_data["password"]
        is_email_exist = Profile.objects.filter(email=email).exists()
        #print 'yes'
        black_password = make_password(password)
        if not is_email_exist: 
            raise forms.ValidationError(u"该邮箱未被注册，请重新登录")  
        else:
            p=Profile.objects.get(email=email)
            if p.password == password:
                pass
            else:
                raise forms.ValidationError(u"密码错误")
     
        
        

    
class UserRegistrationForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=50)
    student_id = forms.CharField(label="学号（没有学好请输入九个0）", max_length=9, min_length=9)
    email = forms.EmailField(label='邮箱',error_messages={'required': '邮箱已被注册'})
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='请再次输入密码',
                                widget=forms.PasswordInput)
                                
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('密码不一致')
        return cd['password2']

    def clean(self):            
         # 用户名  
        try:            
            email=self.cleaned_data['email']  
            student_id=self.cleaned_data['student_id']  
        except Exception as e:  
            print 'except: '+ str(e)  
            raise forms.ValidationError(u"注册账号需为邮箱格式")      
   
        # 注册验证         
        is_email_exist = Profile.objects.filter(email=email).exists()
        if is_email_exist:  # is_student_id_exist or
            raise forms.ValidationError(u"该邮箱已被注册，请尝试找回密码")

        is_student_id_exist = Profile.objects.filter(student_id=student_id).exists()
        if is_student_id_exist:
            raise forms.ValidationError(u"该学号已被注册，请尝试找回密码")

class UserEditForm(forms.ModelForm):
    name = forms.CharField(label='姓名')
    student_id = forms.CharField(label="学号")
    email = forms.EmailField(label='邮箱')
    password = forms.CharField(label='密码')
    class Meta:
        model = Profile
        fields = ('name','email','student_id','password')      
