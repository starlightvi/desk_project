from django.urls import path 
from . import views 
#url/path/route is attached to a method 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
] 
#path('route path homepage', views.methodconnectedto, name)