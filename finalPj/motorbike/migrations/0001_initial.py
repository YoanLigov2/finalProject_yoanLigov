# Generated by Django 4.2.3 on 2023-07-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorbike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_model', models.CharField()),
                ('year', models.IntegerField()),
                ('engine_size', models.IntegerField()),
                ('fuel_capacity', models.IntegerField()),
                ('fuel_type', models.CharField()),
                ('top_speed', models.IntegerField()),
                ('emission_standard', models.CharField()),
                ('price', models.FloatField()),
                ('image', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]