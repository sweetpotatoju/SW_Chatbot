"""
URL configuration for SW_Chatbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path, include
from main.views import keyboard, message, mainpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('keyboard/', keyboard, name='keyboard'),
    path('message/', message, name='message'),
    path('', mainpage, name='userpage'),

=======
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> 62ffb3f4a349cbf30c870e2140d0944eb8952f8a
]
