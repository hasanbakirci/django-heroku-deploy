# Generated by Django 3.1.7 on 2021-03-28 12:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=150)),
                ('boy', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('aciklama', models.TextField(blank=True, null=True)),
                ('fiyat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Siparis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.IntegerField()),
                ('toplam_fiyat', models.FloatField()),
                ('olusturma_tarihi', models.DateField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateField(auto_now=True)),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='siparisler', to='cafe.urun')),
            ],
        ),
    ]