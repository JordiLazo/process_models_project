"""academy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.utils import timezone
from django.views.generic import ListView
from academyApp.models import Academia
from django.conf.urls import url
from academyApp.views import test, filtro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListView.as_view(
         queryset=Academia.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
         context_object_name='latest_academies_list',
         template_name='academies_list.html'),
     name='academies_list'),
    path('details/', ListView.as_view(queryset=Academia.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
                context_object_name='latest_academies_list',
                template_name='academies_details.html'),
                name='academies_details'),
    url('details/academis/<str:pk>/', test, name='academies_details2'),
    url('details/academis', filtro, name='academies_details'),
]


"""
    path('', ListView.as_view(
                queryset=Academia.objects.values('city').distinct(),
                context_object_name='latest_academies_list',
                template_name='academies_list.html'),
                name='academies_list'),
                    path('', displaycity, name='academies_list'),

"""