from django.contrib import admin
from .models import PageCount
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(PageCount)
admin.site.register(Question)
admin.site.register(Choice)