# Generated by Django 4.1.1 on 2022-11-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_stripecustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecustomer',
            name='plan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stripecustomer',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
