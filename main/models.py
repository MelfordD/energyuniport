from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from blog.models import ArticlePost
# django-ckeditor
from ckeditor.fields import RichTextField
# django-mptt
from mptt.models import MPTTModel, TreeForeignKey

class Comment(MPTTModel):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )

    # mptt
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    # str
    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]
