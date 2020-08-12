"""JsonHost URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import *
from jsondata import urls

urlpatterns = [
 
    path('',home,name="Homepage"),
    path('<str:storage_id>/<str:storage_url>',UserStorageHandling.as_view(),name="UserStorageHandlingData"),
    path('storage/create/',
         StorageCreation.as_view(), name="StrorageCreation"),
    path('storage/list/',
         StorageList.as_view(), name="StrorageList"),
    path('storage/delete/<int:pk>',
         StorageDeletion.as_view(), name="StrorageDelete"),



    path('projects/', ProjectHandling.as_view(),
         name="ProjectData"),
    path('project/<int:pk>/delete/', ProjectDeletion.as_view(),
         name="ProjectData")
]
