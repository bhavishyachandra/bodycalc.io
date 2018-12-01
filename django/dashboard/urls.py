#from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'bodycalc'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
