from django.db import models
from ckeditor.fields import RichTextField

class Basic(models.Model):
    title = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    delivery = RichTextField(blank=True)
    payment = RichTextField(blank=True)
    confidence = RichTextField(blank=True)
    help = RichTextField(blank=True)
    twitter = models.TextField(blank=True)
    facebook = models.TextField(blank=True)
    youtube = models.TextField(blank=True)
    instagram = models.TextField(blank=True)

    footer = RichTextField(blank=True)

    def __str__(self):
        return self.title
