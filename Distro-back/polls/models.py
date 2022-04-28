from operator import mod
from django.db import models

# Create your models here.
class Distro(models.Model):
    name = models.TextField()  
    Desc = models.TextField(default="")
    link = models.URLField(default="")
class Translation(models.Model):
    #page_name to specify the name of the page we gonna use our values in
    page_name = models.CharField(max_length=100)
    #name of the field
    key = models.CharField(max_length=100)
    #value of the field which will reperesent the translation
    value = models.TextField()
    #to specify to which language this row will be used
    language = models.CharField(max_length=100)
class Features (models.Model):
    #the Contributor name    
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    language = models.CharField(max_length=50,default="English")

#this modules to set dynamic urls for the website
class links(models.Model):
    #page name
    name = models.CharField(max_length=100)
    #page link
    link = models.CharField(max_length=200)
    #link Language
    language = models.CharField(max_length=50)
    #this modules to set dynamic urls for the website
