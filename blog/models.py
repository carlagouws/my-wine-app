from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

TYPE_CHOICES = (
        ('Red','Red'),
        ('White', 'White'),
        ('Rose','Rose'),
        ('Sparkling','Sparkling'),
    )

VARIETY_CHOICES = (
        ('Barbera','Barbera'),
        ('Blaufränkisch','Blaufränkisch'),
        ('Cabernet Franc', 'Cabernet Franc'),
        ('Cabernet Sauvignon', 'Cabernet Sauvignon'),
        ('Carignan','Carignan'),
        ('Carménère','Carménère'),
        ('Chardonnay','Chardonnay'),
        ('Châteauneuf-du-Pape', 'Châteauneuf-du-Pape'),
        ('Chenin Blanc','Chenin Blanc'),
        ('Cinsault', 'Cinsault'),
        ('Colombard','Colombard'),
        ('Durif (Petite Sirah)','Durif (Petite Sirah)'),
        ('Gamay','Gamay'),
        ('Gewürztraminer','Gewürztraminer'),
        ('Glera (Prosecco)','Glera (Prosecco)'),
        ('Graciano','Graciano'),
        ('Granache/Garnacha', 'Granache/Garnacha'),
        ('Grüner Veltliner','Grüner Veltliner'),
        ('Malbec', 'Malbec'),
        ('Malvasía','Malvasía'),
        ('Marsanne','Marsanne'),
        ('Mataro','Mataro'),
        ('Maturana','Maturana'),
        ('Mazuelo','Mazuelo'),
        ('Merlot', 'Merlot'),
        ('Montepulciano','Montepulciano'),
        ('Muscat','Muscat'),
        ('Nebbiolo','Nebbiolo'),
        ('Nero d\'Avola','Nero d\'Avola'),
        ('Petit Verdot','Petit Verdot'),
        ('Pinotage','Pinotage'),
        ('Pinot Blanc/Bianco','Pinot Blanc/Bianco'),
        ('Pinot Grigio', 'Pinot Grigio'),
        ('Pinot Gris', 'Pinot Gris'),
        ('Pinot Meunier', 'Pinot Meunier'),
        ('Pinot Noir', 'Pinot Noir'),
        ('Riesling','Riesling'),
        ('Roussanne','Roussanne'),
        ('Sangiovese', 'Sangiovese'),
        ('Sauvignon Blanc', 'Sauvignon Blanc'),
        ('Sémillon','Sémillon'),
        ('Shiraz', 'Shiraz'),
        ('Syrah', 'Syrah'),
        ('Tempranillo','Tempranillo'),
        ('Trebbiano','Trebbiano'),
        ('Trollinger','Trollinger'),
        ('Viognier','Viognier'),
        ('Viura (Macabeo)','Viura (Macabeo)'),
        ('Zinfandel','Zinfandel'),
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
        ('Co-op', 'Co-op'),
        ('Laithwaite\'s', 'Laithwaite\'s'),
        ('Lidl', 'Lidl'),
        ('M&S', 'M&S'),
        ('Majestic Wine', 'Majestic Wine'),
        ('Morrisons', 'Morrisons'),
        ('Ocado', 'Ocado'),
        ('Oddbins', 'Oddbins'),
        ('Sainsbury\'s', 'Sainsbury\'s'),
        ('Tesco', 'Tesco'),
        ('Virgin Wines', 'Virgin Wines'),
        ('Waitrose', 'Waitrose'),
    )

# Wine object model
class Wine(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg')
    image_2 = models.ImageField(null=True, blank=True)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, null=True, blank=True)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    variety = MultiSelectField(choices=VARIETY_CHOICES, max_choices=5, max_length=100, null=True, blank=True)
    vintage = models.CharField(max_length=4)
    region = models.CharField(max_length=30, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    shop = models.CharField(max_length=20, choices=SHOP_CHOICES, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name