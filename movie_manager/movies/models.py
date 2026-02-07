from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    certified_by=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.certified_by

class Production(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class MovieInfo(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    censor_details = models.OneToOneField(CensorInfo, on_delete=models.SET_NULL, related_name='movie', null=True, blank=True)
    production_house = models.ForeignKey(Production, on_delete=models.CASCADE, related_name='movies', null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='acted_movies', blank=True)

    def __str__(self):
        return self.title