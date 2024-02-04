"""login_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path  #from django.conf.urls import url  # https://stackoverflow.com/questions/63367594/the-url-function-in-django-has-been-deprecated-do-i-have-to-change-my-source
from login_api.views import login, logout, index
from django.contrib.auth.views import LoginView, LogoutView  # The built-in view funciton

urlpatterns = [
    path('login_api/', include("login_api.urls"), name="login_api"),  # http://127.0.0.1:8000/login_api/
    path("", index, name="index"),  # http://127.0.0.1:8000/
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    #re_path(r'^accounts/login/$', LoginView.as_view(template_name='../templates/login_api/login_page.html')),  #login  # /accounts/login/是Django預設的登入pattern(/accounts/logout/也是預設值)，這個pattern對於某些Django的函式而言是參數的預設值
    #re_path(r'^accounts/logout/$', LogoutView.as_view(template_name='../templates/login_api/logout.html')),  #logout
    re_path(r'^index/$', index),  # http://127.0.0.1:8000/index/
]
