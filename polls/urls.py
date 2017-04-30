from django.conf.urls import url
from . import views

app_name = "polls"
urlpatterns = [
    #The dollar sign matches the end of the string
    url(r'^$', views.detail, name='detail'),
    url(r'^data/', views.index, name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = "results"),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote"),
]