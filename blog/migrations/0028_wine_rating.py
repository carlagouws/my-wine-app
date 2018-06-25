# Generated by Django 2.0.6 on 2018-06-22 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.STAR_RATINGS_RATING_MODEL),
        ('blog', '0027_auto_20180621_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]
