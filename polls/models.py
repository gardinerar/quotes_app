from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here. We are creating the database schema here. :)
#class inherits from models.Model , the class is django's version of a database table
class Quotes(models.Model):
        #ID field is created automatically
        quote_text = models.CharField(max_length=200, default="gasp")
        pub_date = models.DateTimeField('date published')
        def __str__(self):
                return self.quote_text
        def was_published_recently(self):
                return self.pub_date >= timezone.now() - datetime.timedelta(days=5)
