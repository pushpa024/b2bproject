# Generated by Django 4.1.1 on 2022-10-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_sellorleaseassets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_assetDetails',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_assetLocation',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_assetPurchaseDate',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_indUseAsset',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_sellAtPrice',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_sellReason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_sellWay',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_tanIntangible',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sellorleaseassets',
            name='sl_valuePhyAsset',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
