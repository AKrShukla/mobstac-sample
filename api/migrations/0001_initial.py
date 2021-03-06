# Generated by Django 2.0.12 on 2020-03-23 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='dynamicQR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('qr_type', models.CharField(max_length=50, verbose_name='qr_type')),
                ('organization', models.CharField(max_length=50, verbose_name='Organization')),
                ('content_type', models.CharField(max_length=50, verbose_name='Content')),
                ('custom_url', models.CharField(max_length=400, verbose_name='Url')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author ')),
            ],
        ),
        migrations.CreateModel(
            name='staticQR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('qr_type', models.CharField(max_length=50, verbose_name='qr_type')),
                ('organization', models.CharField(max_length=50, verbose_name='Organization')),
                ('url', models.CharField(max_length=400, verbose_name='Url')),
            ],
        ),
    ]
