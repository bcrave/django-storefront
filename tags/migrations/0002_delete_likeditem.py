# Generated by Django 4.0.1 on 2022-01-28 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikedItem',
        ),
    ]
