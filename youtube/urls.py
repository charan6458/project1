from django.urls import path
from youtube import views

urlpatterns=[
    path('welcome/',views.welcome,name='welcome'),
    path('home/',views.home,name='home'),
    path('hello/',views.hello,name='hello'),
]