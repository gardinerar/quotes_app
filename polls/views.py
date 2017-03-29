from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCount

# Create your views here.
def index(request):
    #PageCount represents the table
    row, created = PageCount.objects.get_or_create(page="index")
    row.count = row.count + 1
    row.save() #writes the row back to the database
    if created:
        words = "You are our first visitor! Congrats!"
    else:
        words = "Hello, world at " + time.strftime("%c")
    return HttpResponse(words + " Visit number " + str(row.count))
