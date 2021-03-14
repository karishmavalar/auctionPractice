# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Auctions(models.Model):
    name = models.CharField(max_length=128)
    starts_on = models.DateTimeField(default=timezone.now)
    ends_on = models.DateTimeField()
    featured_image = models.ImageField(upload_to='featured image')
    enable = models.BooleanField(default=True)
    auction_description = models.TextField()
    auction_image = models.ImageField(upload_to='auction image')
	
