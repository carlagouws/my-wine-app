# Generated by Django 2.0.6 on 2018-06-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='description',
            new_name='comments',
        ),
        migrations.AddField(
            model_name='wine',
            name='vintage',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
