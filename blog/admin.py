from django.contrib import admin

from .models import Post #Importing 'Post' class from blog/models.py

admin.site.register(Post) #This makes our 'Post' class from the model visible on the admin page
