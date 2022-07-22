from django.db import models
from django.db.models import Q

# Create your models here.


class Link(models.Model):
    alias = models.CharField(max_length=200)
    link_to = models.URLField(max_length=2048)


class LinkQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(alias__icontains=query)
        return self.filter(lookups)


class LinkManager(models.Manager):
    def get_queryset(self):
        return LinkQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
