from django.conf.urls import url
from . import views

app_name = "polls"
urlpatterns = [
    #The dollar sign matches the end of the string
    url(r'^$', views.detail, name='detail'),
    url(r'^data/', views.index, name='index'),
]