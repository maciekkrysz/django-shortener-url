from django.db import models

# Create your models here.


class Link(models.Model):
    alias = models.CharField(max_length=200)
    link_to = models.CharField(max_length=2048)