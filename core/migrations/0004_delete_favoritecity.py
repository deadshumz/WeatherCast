# Generated by Django 4.0.5 on 2022-06-17 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_favoritecity_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteCity',
        ),
    ]
