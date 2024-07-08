from django.db import models

# Create your models here.
INSTRUMENT_CHOICES = [
    ("GUITAR", "Guitar"),
    ("PIANO", "Piano"),
    ("DRUMS", "Drums"),
    ("BASS", "Bass"),
    ("VIOLIN", "Violin"),
    ("SAXOPHONE", "Saxophone"),
    ("TRUMPET", "Trumpet"),
    ("FLUTE", "Flute"),
    ("CLARINET", "Clarinet"),
    ("VOCALS", "Vocals"),
    ("OTHER", "Other"),
]


class MusicianModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(
        max_length=20, choices=INSTRUMENT_CHOICES, default="OTHER"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
