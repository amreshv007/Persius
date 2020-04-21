from django.db import models
from django.contrib.auth.models import User


class ImgPlace(models.Model):
    # person = models.ForeignKey(User, on_delete=models.CASCADE),
    img = models.ImageField(upload_to='place_images'),
    place = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.place


class NamesPlace(models.Model):
    names = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.names
