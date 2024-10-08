# Generated by Django 4.1.1 on 2022-10-14 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_pssdoc_brochure_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellOrLeaseAssets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputFname', models.CharField(blank=True, max_length=50, null=True)),
                ('companyName', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('inputEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('verificationCall', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True)),
                ('investor_category', models.CharField(blank=True, max_length=50, null=True)),
                ('interested', models.CharField(blank=True, max_length=50, null=True)),
                ('sl_assetPurchaseDate', models.CharField(max_length=15)),
                ('sl_indUseAsset', models.CharField(max_length=15)),
                ('sl_assetLocation', models.CharField(max_length=30)),
                ('sl_assetDetails', models.TextField()),
                ('sl_tanIntangible', models.TextField()),
                ('sl_valuePhyAsset', models.CharField(max_length=15)),
                ('sl_sellAtPrice', models.CharField(max_length=15)),
                ('sl_sellWay', models.CharField(max_length=15)),
                ('sl_sellReason', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellorleasebusinessprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SellOrLeaseBusinessProfile',
            },
        ),
        migrations.AlterField(
            model_name='pssbusiproof',
            name='business_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.partialstakesale'),
        ),
        migrations.AlterField(
            model_name='pssdoc',
            name='business_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.partialstakesale'),
        ),
        migrations.CreateModel(
            name='SLImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_photos', models.ImageField(blank=True, null=True, upload_to='')),
                ('business_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sellorleaseassets')),
            ],
        ),
        migrations.CreateModel(
            name='SLDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brochure_doc', models.FileField(blank=True, null=True, upload_to='')),
                ('business_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sellorleaseassets')),
            ],
        ),
        migrations.CreateModel(
            name='SLBusiProof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_proof', models.FileField(blank=True, null=True, upload_to='')),
                ('business_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sellorleaseassets')),
            ],
        ),
    ]
