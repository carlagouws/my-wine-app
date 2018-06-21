from django.db import models
from django.utils import timezone

TYPE_CHOICES = (
        ('Not Selected','Select type'),
        ('Red','Red'),
        ('White', 'White'),
        ('Rose','Rose'),
        ('Sparkling','Sparkling'),
    )

VARIETY_CHOICES = (
        ('Not Selected','Select grapes'),
        ('Cabernet Franc', 'Cabernet Franc'),
        ('Cabernet Sauvignon', 'Cabernet Sauvignon'),
        ('Cinsault', 'Cinsault'),
        ('Granache', 'Granache'),
        ('Malbec', 'Malbec'),
        ('Merlot', 'Merlot'),
        ('Montepulciano','Montepulciano'),
        ('Nero d\'Avola','Nero d\'Avola'),
        ('Prosecco','Prosecco'),
        ('Pinotage','Pinotage'),
        ('Pinot Grigio', 'Pinot Grigio'),
        ('Pinot Gris', 'Pinot Gris'),
        ('Pinot Noir', 'Pinot Noir'),
        ('Sangiovese', 'Sangiovese'),
        ('Sauvignon blanc', 'Sauvignon Blanc'),
        ('Shiraz', 'Shiraz'),
        ('Tempranillo','Tempranillo'),
    )

class Wine(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg')
    image_2 = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, default='Select type')
    variety = models.CharField(max_length=20, choices=VARIETY_CHOICES, default='Select grapes')
    # radio button choices
    vintage = models.CharField(max_length=4)
    region = models.CharField(max_length=30, null=True, blank=True)
    # review
    comments = models.TextField(null=True, blank=True)
    # Bought or sampled
    # If bought, where and how much?