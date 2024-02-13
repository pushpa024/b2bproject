# Generated by Django 4.0.3 on 2022-04-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
