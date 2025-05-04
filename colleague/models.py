from django.db import models

class Colleague(models.Model):
    name = models.CharField(max_length=30, blank=True)
    job = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)

    def __str__(self):
        return self.name
