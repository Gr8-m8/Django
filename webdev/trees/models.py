from django.db import models

class TreeType(models.Model):
    latin = models.CharField(max_length=255)
    se = models.CharField(max_length=255)
    info = models.CharField(max_length=2047)