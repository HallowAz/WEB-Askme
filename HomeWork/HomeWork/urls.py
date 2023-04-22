"""
URL configuration for HomeWork project.

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
from django.urls import path
from askme import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/<int:page>', views.index, name='index-page'),
    path('admin/', admin.site.urls),
    path('question/<int:question_id>/', views.question, name="question"),
    path('question/<int:question_id>/<int:page>', views.question, name="question"),
    path('login/', views.login, name='login'),
    path('ask/', views.ask, name='ask'),
    path('hot/', views.hot, name='hot'),
    path('hot/<int:page>', views.hot, name='hot-page'),
    path('tag/<tag_name>', views.tag, name='tag'),
    path('tag/<tag_name>/<int:page>', views.tag, name='tag'),
    path('signup/', views.sign_up, name='signup')
]
