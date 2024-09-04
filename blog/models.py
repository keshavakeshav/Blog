from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=225,default='Unknown')
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name if self.name else 'Unnamed Category'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users')
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='post/thumbnail')
    description = RichTextField(blank=True,null=True)
    tags = models.CharField(max_length=255)
    posted_at = models.DateField(default=datetime.now)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')

    def __str__(self):
        return self.title if self.title else 'Untitled Post'
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField()
    website = models.CharField(max_length=255,null=True,blank=True)
    commented_at = models.DateTimeField(default=datetime.now)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'