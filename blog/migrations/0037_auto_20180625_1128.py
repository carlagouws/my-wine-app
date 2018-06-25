# Generated by Django 2.0.6 on 2018-06-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20180625_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='rating',
            field=models.CharField(choices=[('Not yet!', '-----'), ('★☆☆☆☆', 'One star'), ('★★☆☆☆', 'Two stars'), ('★★★☆☆', 'Three stars'), ('★★★★☆', 'Four stars'), ('★★★★★', 'Five stars')], default='-----', max_length=20),
        ),
    ]
