# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class APIs(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    requesting = models.TextField(null = True)
    def __str__(self):
        return self.name
