from django.conf.urls import url
from Login import views
from django.urls import path,include

urlpatterns=[

   url(r'^$',views.index,name='index'),

   path('home/',views.home, name='home')
 
]