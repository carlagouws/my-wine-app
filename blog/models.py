from django.db import models

TYPE_CHOICES = (
       ('red','Red'),
       ('white', 'White'),
       ('rose','Rose'),
       ('sparkling','Sparkling'),
    )

CULTIVAR_CHOICES = (
        ('cabernet franc', 'Cabernet Franc'),
        ('cabernet sauvignon', 'Cabernet Sauvignon'),
        ('cinsault', 'Cinsault'),
        ('granache', 'Granache'),
        ('malbec', 'Malbec'),
        ('merlot', 'Merlot'),
        ('montepulciano','Montepulciano'),
        ('nero d\'avola','Nero d\'Avola'),
        ('pinotage','Pinotage'),
        ('pinot grigio', 'Pinot Grigio'),
        ('pinot gris', 'Pinot Gris'),
        ('pinot noir', 'Pinot Noir'),
        ('sangiovese', 'Sangiovese'),
        ('sauvignon blanc', 'Sauvignon Blanc'),
        ('shiraz', 'Shiraz'),
        ('tempranillo','Tempranillo'),
    )

class Wine(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    # image
    type = models.CharField(max_length=9, choices=TYPE_CHOICES, default='red')
    cultivar = models.CharField(max_length=20, choices=CULTIVAR_CHOICES, default='cabernet franc')
    # radio button choices
    vintage = models.CharField(max_length=4)
    country = models.CharField(max_length=30, null=True, blank=True)
    # review
    comments = models.TextField(null=True, blank=True)
    # Bought or sampled
    # If bought, where and how much?