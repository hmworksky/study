from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
class BlogPostAdmin(admin.ModelAdmin):
    list_display = {'title','body','timestamp'}
admin.site.register(BlogPost, BlogPostAdmin)
    