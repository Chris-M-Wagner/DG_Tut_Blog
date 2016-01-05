#More about modelfields: 
# https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class Post(models.Model): #Defines our model 'Post' as an object. models.Model makes "Post" a django model so it will save in the database.
	author = models.ForeignKey('auth.User') #Links to the auth.User model
	title = models.CharField(max_length=200) #Field with limited character entry
	text = models.TextField() #No character limit
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)##?

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #Double underlines = called "dunder" (aka double-underscore)
		return self.title

