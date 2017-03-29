from __future__ import unicode_literals

from django.db import models

# Create your models here.
#class inherits from models.Model , the class is django's version of a database table
class PageCount(models.Model):
        page = models.URLField(default='defaultURL')
        count = models.IntegerField()
