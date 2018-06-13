from django.db import models

TYPE_CHOICES = (
       ('red','Red'),
       ('white', 'White'),
       ('rose','Rose'),
       ('sparkling','Sparkling'),
    )

CULTIVAR_CHOICES = (
       ('granache','Granache'),
    )

class Wine(models.Model):
    name = models.CharField(max_length=255)
    # image
    type = models.CharField(max_length=9, choices=TYPE_CHOICES, default='red')
    cultivar = models.CharField(max_length=20, choices=CULTIVAR_CHOICES)
    # radio button choices
    vintage = models.CharField(max_length=4)
    # review
    comments = models.TextField()
    slug = models.SlugField(unique=True)