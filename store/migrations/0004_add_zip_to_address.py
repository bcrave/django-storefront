# Generated by Django 4.0.1 on 2022-01-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
