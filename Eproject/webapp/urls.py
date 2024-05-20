from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
     path('s_notice/', views.s_notice, name='s_notice'),
     path('tu_notice/',views.tu_notice,name='tu_notice')
]