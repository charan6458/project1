from django.urls import path
from facebook import views

urlpatterns=[
    path('face/',views.face,name='face'),
]