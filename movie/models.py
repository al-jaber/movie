from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    release_date = models.DateField(blank=True)

    def __str__(self):
        return f"{self.name}: {self.rating}"


class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.movie.name}"
    