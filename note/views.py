# -*- coding: utf-8 -*-
import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post
from .forms import New_Post_Form

# Create your views here.
def list_post(request, category=None):
    author_id = request.user.id
    object_list = Post.objects.filter(author_id=author_id)
    # print type(object_list)
    # print object_list
    #title= object_list.title
    #publish=object_list.publish
    #author=object_list.author
    #print title,publish,author
    #这边注意不要试图中调用视图，这样的return传不过去。
    return HttpResponse('Disabled account')
    #return render(request, 'note/post/list.html', {'posts': object_list})
    #return render(request,
                  #'note/post/list.html',
                  #{'posts': object_list})
    
    
    '''
    paginator = Paginator(object_list, 5) # 5 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts})
                                                   
                                                   
    '''

def note_details(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'note/post/detail.html', {'post': post})

 

    
def create_new_post(request):
    if request.method == 'POST':   
        author_id = request.user.id
        post_form= New_Post_Form(request.POST)
        #upload_file(request)
        #print request.POST

                             
        title=request.POST.get("title","")
        summary=request.POST.get("summary","")
        #file=request.POST.get("file","")
        #image=request.POST.get("image","")
        author_id=request.user.id
        #files=request.post.get['files']
        #files=request.FILES
        files=request.FILES.getlist(u"files")
        file_name_list=[]
        new_file_dir='e:/media/file/'+str(datetime.datetime.now())[:10]+'/'+str(author_id)+'/'
        if not os.path.exists(new_file_dir):
            os.makedirs(new_file_dir)
        for f in files:
            file_name_list.append(f.name)
            destination=open(new_file_dir+f.name,'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        #for count, x in enumerate(request.FILES.getlist["files"]):
            #print str(count)
        #with open('e:/media/image/test.txt','wb+') as destination:
            #for chunk in 

        post = Post()
        post.title=title
        post.summary=summary
        post.author_id=author_id
        post.file_name_dir=str(file_name_list)
        #post.image=image
        post.save()
        return render(request,'note/post/post_success.html')
    else:
        post_form = New_Post_Form()
        return render(request,
                     'note/post/create_new_post.html',
                     {'post_form': post_form})

 
''' 
def uploadfile(request):
    author_id=request.user.id
    
    for count, x in enumerate(request.FILES.getlist('file')):
        def process(f):
            with open('e:/media/')
'''     

from django.http import FileResponse  
def file_download(request,created_time,author_id,file_name):
    #author_id=request.user.id
    #created=request.POST.get("created","")
    #filename=request.POST.get("files","")
    fire_dir='e:/media/'+str(created_time)+'/'+str(author_id)+'/'
    file=open(fire_dir+file_name,'rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%filename 
    return response  
