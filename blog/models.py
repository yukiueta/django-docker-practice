from django.db import models

# Create your models here.

class Blog(models.Model):
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    title = models.CharField('name', max_length=150)
    detail = models.CharField('detail', max_length=1000)
