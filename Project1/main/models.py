from django.db import models
from django.contrib.auth.models import User

class ImgPlace(models.Model):
    person = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE),
    img = models.FileField(),
    place = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.place

    def __str__(self):
        return self.person


class NamesPlace(models.Model):
    names = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.names
