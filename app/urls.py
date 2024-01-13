from unicodedata import name 
from django.urls import path
from app import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='regiter'),
    path('login', views.logISn, name='login'),
    path('logout', views.logOut, name='logout'),
    path('acc', views.acc, name='acc'),
    path('valider', views.valider, name='acc')
]