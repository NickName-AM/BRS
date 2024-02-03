from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

# from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Book(models.Model):
    GENRE_CHOICES = {
        'AC': 'action',
        'FN': 'fantasy',
        'AD': 'adventure',
        'DR': 'drama',
        'HS': 'historical' 
    }

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book/', default='default.jpg')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    # genre = ArrayField(models.CharField(max_length=20))
    genre = MultiSelectField(choices=GENRE_CHOICES, max_length=10)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-create')