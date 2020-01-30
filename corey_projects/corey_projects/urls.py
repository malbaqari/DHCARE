"""corey_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from dhcare import views as dhcare_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminui/', dhcare_views.adminui, name='adminui'),
    path('receptionui/', dhcare_views.receptionui, name='receptionui'),
    path('receptionui-get/', dhcare_views.receptionui_get, name='receptionui-get'),
    path('receptionui-book/', dhcare_views.receptionui_book, name='receptionui-book'),
    path('appointment-confirm/', dhcare_views.appointment_confirm, name='appointment-confirm'),
    path('doctorui-get/', dhcare_views.doctorui_get, name='doctorui-get'),
    path('doctorui-submit/', dhcare_views.doctorui_submit, name='doctorui-submit'),
    path('doctorui/', dhcare_views.doctorui, name='doctorui'),
    path('new-patient/', dhcare_views.new_patient, name='new-patient'),
    path('adminui-get/', dhcare_views.adminui_get, name='adminui_get'),
    path('adminui-submit/', dhcare_views.adminui_submit, name='adminui_submit'),
    path('login/', auth_views.LoginView.as_view(template_name='dhcare/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dhcare/logout.html'), name='logout'),
    path('', include('dhcare.urls')),
]
