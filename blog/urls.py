"""energyuniport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='home'),
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    path('increase-likes/<int:id>/', views.IncreaseLikesView.as_view(), name='increase_likes'),
    path('list-view/', views.ArticleListView.as_view(), name='list_view'),
    path('detail-view/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_view'),
    path('create-view/', views.ArticleCreateView.as_view(), name='create_view'),
]
    