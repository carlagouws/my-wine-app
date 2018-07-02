# Generated by Django 2.0.6 on 2018-07-02 11:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_wine_variety'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='variety',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cabernet Franc', 'Cabernet Franc'), ('Cabernet Sauvignon', 'Cabernet Sauvignon'), ('Cinsault', 'Cinsault'), ('Granache', 'Granache'), ('Malbec', 'Malbec'), ('Merlot', 'Merlot'), ('Montepulciano', 'Montepulciano'), ("Nero d'Avola", "Nero d'Avola"), ('Prosecco', 'Prosecco'), ('Pinotage', 'Pinotage'), ('Pinot Grigio', 'Pinot Grigio'), ('Pinot Gris', 'Pinot Gris'), ('Pinot Noir', 'Pinot Noir'), ('Sangiovese', 'Sangiovese'), ('Sauvignon Blanc', 'Sauvignon Blanc'), ('Shiraz', 'Shiraz'), ('Tempranillo', 'Tempranillo')], max_length=100, null=True),
        ),
    ]