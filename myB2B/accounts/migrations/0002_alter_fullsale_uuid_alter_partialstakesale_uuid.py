# Generated by Django 4.1.1 on 2022-10-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullsale',
            name='uuid',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterField(
            model_name='partialstakesale',
            name='uuid',
            field=models.UUIDField(unique=True),
        ),
    ]
