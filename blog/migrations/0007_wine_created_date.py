# Generated by Django 2.0.6 on 2018-06-14 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180613_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]