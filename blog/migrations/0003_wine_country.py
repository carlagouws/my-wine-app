# Generated by Django 2.0.6 on 2018-06-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180613_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='country',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]