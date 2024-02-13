# Generated by Django 4.1.1 on 2022-12-12 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_stripecustomer_plan_stripecustomer_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planID', models.IntegerField()),
                ('planName', models.TextField(blank=True, null=True)),
                ('Proposals', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='fullsale',
            name='plan',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='partialstakesale',
            name='plan',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
