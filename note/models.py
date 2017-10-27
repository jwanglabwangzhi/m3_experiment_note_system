# -*- coding: utf-8 -*-
import sys,os
import time,datetime
reload(sys)
sys.setdefaultencoding('utf-8')
#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse

from account.models import Profile


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='profile_post')
    #body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateField(default=str(datetime.datetime.now())[:10])
    #updated = models.DateTimeField(auto_now=True)
    #image=models.ImageField(upload_to='image', verbose_name='图片',blank=True)
    file_name_dir=models.TextField(max_length=200,blank=True)
    


    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note:note_details', args=[str(self.id)])    
        
        
        
'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
'''
        
