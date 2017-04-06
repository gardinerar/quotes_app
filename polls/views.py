from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

import time
from .models import PageCount
from .models import Question

# Create your views here.
def index(request):
    #PageCount represents the table
    row, created = PageCount.objects.get_or_create(page="index")
    row.count = row.count + 1
    row.save() #writes the row back to the database
    if created:
        words = "You are our first visitor! Congrats!"
    else:
        words = "<p>Hello, world at " + time.strftime("%c") + "</p>"
    # return HttpResponse(words + " Visit number " + str(row.count))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context) 

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)