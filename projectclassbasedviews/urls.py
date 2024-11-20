"""
URL configuration for projectclassbasedviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Fbv_string/',Fbv_string,name='Fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(),name='Cbv_string'),


    path('Fbv_html/',Fbv_html,name='Fbv_html'),
    path('ClassBased/',ClassBased.as_view(),name='ClassBased'),


    path('insert_fbv/',insert_fbv,name='insert_fbv'),
    path('InsertCbv/',InsertCbv.as_view(),name='InsertCbv'),
]
