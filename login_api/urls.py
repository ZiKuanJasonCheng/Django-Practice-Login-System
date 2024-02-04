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
#from . import views
from django.urls import path
from django.urls import include, re_path  #from django.conf.urls import url  # https://stackoverflow.com/questions/63367594/the-url-function-in-django-has-been-deprecated-do-i-have-to-change-my-source
from .views import login, logout, update_pwd, index, itinerary, results, register
from django.contrib.auth.views import LoginView, LogoutView  # The built-in view funciton

app_name = "login_api"
urlpatterns = [
    # https://blog.csdn.net/m0_46629123/article/details/121131651
    #path('', index, name="index"),  # http://127.0.0.1:8000/login_api/
    path('login/', login, name="login"),  # http://127.0.0.1:8000/login_api/login/
    path('logout/', logout, name="logout"),  # http://127.0.0.1:8000/login_api/logout/
    path('update_pwd/', update_pwd, name="update_pwd"),  # http://127.0.0.1:8000/login_api/update_pwd/
    path('register/', register, name="register"),  # http://127.0.0.1:8000/login_api/register/
    path('<int:account_id>/', itinerary, name="account_itinerary"),  # http://127.0.0.1:8000/login_api/1/
    path("<int:account_id>/results/", results, name="account_results"),  # http://127.0.0.1:8000/login_api/1/results/
]
