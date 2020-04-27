"""cohousing URL Configuration

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
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('', views.index, name='index'),
    path('redirect', views.redirect, name="redirect"),
    path('search', views.search, name="search"),
    path('redirect', views.redirect, name="redirect"),
    path('houseDetail/<int:id>', views.houseDetail, name="houseDetail"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('faq', views.faq, name="faq"),
    path('about', views.about, name="about"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
