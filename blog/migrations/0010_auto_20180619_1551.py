# Generated by Django 2.0.6 on 2018-06-19 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180619_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='country',
            new_name='region',
        ),
    ]
