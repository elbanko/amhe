from django.db import models

# Create your models here.
class Testimonial(models.Model):
    date = models.CharField(max_length=100)
    quote = models.CharField(max_length=100000)
    posted_by = models.CharField(max_length=100)