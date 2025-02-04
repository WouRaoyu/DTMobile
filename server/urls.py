"""
URL configuration for DTServer project.

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
from geoinfo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("judge_list/", views.judge_list),
    path("judge_detail/<int:pk>", views.judge_detail),
    path("judge_append", views.judge_append),
    path('upload_file', views.upload_file)
]
