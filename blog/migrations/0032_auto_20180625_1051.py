# Generated by Django 2.0.6 on 2018-06-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20180625_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='rating',
            field=models.CharField(choices=[('None', '-----'), ('&#9734', 'Cabernet Sauvignon'), ('Two', 'Cinsault'), ('Three', 'Granache'), ('Four', 'Malbec'), ('Five', 'Malbec')], default='-----', max_length=20),
        ),
    ]
