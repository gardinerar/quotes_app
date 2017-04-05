from __future__ import unicode_literals

from django.db import models

# Create your models here. We are creating the database schema here. :)
#class inherits from models.Model , the class is django's version of a database table
class PageCount(models.Model):
        page = models.URLField(default='defaultURL')
        count = models.IntegerField(default=0)
        # uniqueClientCount = 
class Question(models.Model):
        #ID field is created automatically
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
        