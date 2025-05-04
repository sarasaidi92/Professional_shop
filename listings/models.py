from django.db import models
from ckeditor.fields import RichTextField

class Listing(models.Model):
    title = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    text = RichTextField(blank=True)
    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    description = RichTextField(blank=True)
    product_details = RichTextField(blank=True)
    review = RichTextField(blank=True)

    def __str__(self):
        return self.title
