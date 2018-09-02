from django.urls import path
#from django.conf.url import url, include
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list')
]