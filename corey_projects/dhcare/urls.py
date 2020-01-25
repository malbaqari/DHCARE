from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='dhcare-home'),
    path('about/', views.about, name='dhcare-about'),
]
