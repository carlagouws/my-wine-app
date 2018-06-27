from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

TYPE_CHOICES = (
        ('Not Selected','Select type'),
        ('Red','Red'),
        ('White', 'White'),
        ('Rose','Rose'),
        ('Sparkling','Sparkling'),
    )

VARIETY_CHOICES = (
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
        ('Sauvignon Blanc', 'Sauvignon Blanc'),
        ('Shiraz', 'Shiraz'),
        ('Tempranillo','Tempranillo'),
    )

RATING_CHOICES = (
        (u"\u2605"+u"\u2606"+u"\u2606"+u"\u2606"+u"\u2606", u"\u2605"+u"\u2606"+u"\u2606"+u"\u2606"+u"\u2606"),
        (u"\u2605"+u"\u2605"+u"\u2606"+u"\u2606"+u"\u2606", u"\u2605"+u"\u2605"+u"\u2606"+u"\u2606"+u"\u2606"),
        (u"\u2605"+u"\u2605"+u"\u2605"+u"\u2606"+u"\u2606", u"\u2605"+u"\u2605"+u"\u2605"+u"\u2606"+u"\u2606"),
        (u"\u2605"+u"\u2605"+u"\u2605"+u"\u2605"+u"\u2606", u"\u2605"+u"\u2605"+u"\u2605"+u"\u2605"+u"\u2606"),
        (u"\u2605"+u"\u2605"+u"\u2605"+u"\u2605"+u"\u2605", u"\u2605"+u"\u2605"+u"\u2605"+u"\u2605"+u"\u2605"),
    )

SHOP_CHOICES = (
        ('Aldi', 'Aldi'),
        ('Asda', 'Asda'),
        ('M&S', 'M&S'),
        ('Sainsbury\'s', 'Sainsbury\'s'),
        ('Tesco', 'Tesco'),
        ('Virgin Wines', 'Virgin Wines'),
        ('Waitrose', 'Waitrose'),
    )

class Wine(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg')
    image_2 = models.ImageField(null=True, blank=True)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, null=True, blank=True)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, default='Select type')
    variety = MultiSelectField(choices=VARIETY_CHOICES, max_choices=5, max_length=100, null=True, blank=True)
    vintage = models.CharField(max_length=4)
    region = models.CharField(max_length=30, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    shop = models.CharField(max_length=20, choices=SHOP_CHOICES, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
