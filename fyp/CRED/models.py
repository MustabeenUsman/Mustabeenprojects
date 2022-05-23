from datetime import datetime
from email.quoprimime import quote
from os import link
from django.db import models
import os
from django.contrib.auth.models import User

def get_file_path(request, filename):
    original_filename=filename
    nowTime = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)
# Create your models h
class Videos(models.Model):
    CATEGORIES = (
        ('Happy','Happy'),
        ('Anger','Anger'),
        ('Fear','Fear'),
        ('Sad','Sad'),
        ('Contempt','Contempt'),
        ('Disgust','Disgust'),
        ('Surprise','Surprise'),
    )
    name = models.CharField(max_length=200, null=True)
    url_link = models.URLField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image=models.ImageField(upload_to="images/",default="")
    #img=models.ImageField(upload_to='static/images', height_field=None,\
     #      width_field=None, max_length=100)
    def __str__(self):
        return self.name

class Audios(models.Model):
    CATEGORIES = (
        ('Happy','Happy'),
        ('anger','ager'),
        ('fear','fear'),
        ('sad','sad'),
        ('contempt','contempt'),
        ('disgust','disgust'),
        ('surprise','surprise'),
    )
    name = models.CharField(max_length=200, null=True)
    url_link = models.URLField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to=get_file_path,default="")
    #img=models.ImageField(upload_to='static/images', height_field=None,\
     #      width_field=None, max_length=100)
    def __str__(self):
        return self.name

class Books(models.Model):
    CATEGORIES = (
        ('Happy','Happy'),
        ('anger','ager'),
        ('fear','fear'),
        ('sad','sad'),
        ('contempt','contempt'),
        ('disgust','disgust'),
        ('surprise','surprise'),
    )
    name = models.CharField(max_length=200, null=True)
    url_link = models.URLField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to=get_file_path,default="")
    #img=models.ImageField(upload_to='static/images', height_field=None,\
     #      width_field=None, max_length=100)
    def __str__(self):
        return self.name

class Quotes(models.Model):
    CATEGORIES = (
        ('Happy','Happy'),
        ('anger','ager'),
        ('fear','fear'),
        ('sad','sad'),
        ('contempt','contempt'),
        ('disgust','disgust'),
        ('surprise','surprise'),
    )
    name = models.CharField(max_length=200, null=True)
    url_link = models.URLField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to=get_file_path,default="")
    #img=models.ImageField(upload_to='static/images', height_field=None,\
     #      width_field=None, max_length=100)
    def __str__(self):
        return self.name


class video_playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'video')


class audio_playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audios, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'audio')


class book_playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'book')
        
class quote_playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quotes, on_delete=models.CASCADE)    
    class Meta:
        unique_together = ('user', 'quote')


class video_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)



class audio_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audios, on_delete=models.CASCADE)


class book_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
        
class quote_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quotes, on_delete=models.CASCADE)        