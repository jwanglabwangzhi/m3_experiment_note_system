# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout   
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django import forms
from django.core.urlresolvers import reverse  
 
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .models import Profile
from .backends import CustomUserAuth
from note.views import list_post
from note.models import Post


# Create your views here.
def user_login(request):        
    if request.method == 'POST':            
        login_form = LoginForm(request.POST) 
        user_name=request.POST.get("user_name","")
        password=request.POST.get("password","")  
        #print 'a################'
        if login_form.is_valid(): 
            cd = login_form.cleaned_data
            #print cd['username'],cd['password']
            backend = CustomUserAuth()
            user = backend.authenticate(username=cd['username'],
                                password=cd['password'])
            
            if user is not None:                    
                if user.is_active:                        
                    login(request, user)
                    return HttpResponseRedirect('/account/')
                    #redirect('dashboard')
                    #print request.POST.get('next')
                    
                    #return render(request,'/account/login.html')
                    #return render(request,'account/dashboard.html')
                    #list_post(request)
                    #author_id = request.user.id
                    #object_list = Post.objects.filter(author_id=author_id) 
                    #return render(request, 'note/post/list.html', {'posts': object_list})
                    #return render(request,'note/post/list.html',)
                else:                        
                    return HttpResponse('Disabled account')
            else:            
                return HttpResponse('Invalid login')           
            

    else:            
        login_form = LoginForm()        
    return render(request, 'registration/login.html', {'form': login_form})


 
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

    
'''            

                
            user = authenticate(username=user_name, password=password)
        print user
        login(request, user)
        return render(request,
            'account/dashboard.html',
            )                 
                
                
'''  
    
    
    
    
def register(request):
    if request.method == 'POST':
        try:  
            user_form= UserRegistrationForm(request.POST)  
        except Exception as e:  
            # 登录失败 返回错误提示      
            err = "注册失败，请重试"  
            return result_response(request, err)
                      
        if user_form.is_valid():
            name=request.POST.get("name","")
            student_id=request.POST.get("student_id","")
            password=request.POST.get("password","")
            #blackpassword=make_password(password)
            email=request.POST.get("email","")
            
            profile = Profile()
            profile.name=name
            profile.student_id=student_id
            profile.password=password
            profile.email=email
            if Profile.objects.filter(email=email).exists():
                return render(request,
                              'account/register.html',
                              {''})
            else:
                profile.save()
                return render(request,
                             'account/register_done.html',
                             {'name': name})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'account/register.html',
                 {'user_form': user_form})



    
@login_required
def dashboard(request):
    author_id = request.user.id
    object_list = Post.objects.filter(author_id=author_id)    
    return render(request,
                 'account/dashboard.html',
                 {'posts': object_list})

'''
    list_post(request)
    author_id = request.user.id
    object_list = Post.objects.filter(author_id=author_id) 
    return render(request, 'note/post/list.html', {'posts': object_list})
'''


@login_required
def note_details(request,id):
    post = get_object_or_404(Post,id=id)
    print post.title
                 
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)

        if user_form.is_valid():
            name=request.POST.get("name","")
            email=request.POST.get("email","")
            student_id=request.POST.get("student_id","")
            password=request.POST.get("password","")
                      
            profile = Profile()
            profile.name=name
            profile.student_id=student_id
            profile.email=email  
            profile.password=password
            user_form.save()
            return HttpResponseRedirect('/account/')            
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
                 'account/edit.html',
                 {'user_form': user_form})
            

