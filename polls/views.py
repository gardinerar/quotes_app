from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from reconstitute import updateQuotes

import time
from .models import Quotes

# Create your views here.
def index(request):
    updateQuotes()
    latest_quote_list = Quotes.objects.order_by('-pub_date')[:15]
    context = {'latest_quote_list': latest_quote_list,}
    return render(request, 'polls/index.html', context) 

def detail(request):
    latest_quote_list = Quotes.objects.order_by('-pub_date')[:15]
    context = {'latest_quote_list': latest_quote_list,}
    return render(request, 'polls/detail.html', context) 
