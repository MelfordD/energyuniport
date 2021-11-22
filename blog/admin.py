from django.contrib import admin

#ArticlerPost
from .models import ArticlePost, ArticleColumn


#ArticlePost admin
admin.site.register(ArticlePost)

admin.site.register(ArticleColumn)