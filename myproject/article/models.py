from django.db import models
from django.utils import timezone
from rest_framework import serializers


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()
    article_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date