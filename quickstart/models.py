from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200)
    published_date = models.DateField('date published')

class Contact(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField(max_length=254)
