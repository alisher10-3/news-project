from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'id': self.id})