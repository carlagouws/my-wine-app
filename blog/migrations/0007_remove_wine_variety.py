# Generated by Django 2.0.6 on 2018-07-02 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180629_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='variety',
        ),
    ]
