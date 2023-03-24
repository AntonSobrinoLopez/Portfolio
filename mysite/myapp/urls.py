from django.urls import path
from . import views

urlpatterns=[
    path('myapp/',views.index,name='index'),
    path('myfirst/', views.myfirstshtml,name='myfirstshtml'),
    path('portfolio/', views.mymaster, name= 'mymaster'),
]

