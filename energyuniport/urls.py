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
from django.urls import path, include
from blog.views import article_list, index
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import notifications.urls

from blog.views import article_list, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('comments', include('main.urls', namespace='comment')),
    path('notice/', include('notice.urls', namespace='notice')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('password-reset/', include('password_reset.urls')),
    path('article/', include('blog.urls', namespace='article')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)