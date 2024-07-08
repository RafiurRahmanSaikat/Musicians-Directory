from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musician.models import MusicianModel


class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    musicians = models.ManyToManyField(MusicianModel)
    release_date = models.DateField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.album_name
