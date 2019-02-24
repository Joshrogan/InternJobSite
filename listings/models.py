from django.db import models
from django.conf import settings
from django.urls import reverse

class Listing(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description =  models.TextField()

    def __str__(self):
        return self.company + ' ' + self.role

    def get_absolute_url(self):
        return reverse('listing_detail', args=[str(self.id)])
