# Generated by Django 4.2.3 on 2023-08-05 17:32

from django.db import migrations, models
import finalProject.motorbike.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorbike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('bike_type', models.CharField(choices=[('Scooter', 'Scooter'), ('Chopper', 'Chopper'), ('Sportbike', 'Sportbike'), ('Off-Road', 'Off-Road'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=30)),
                ('year', models.IntegerField(validators=[finalProject.motorbike.validators.check_year])),
                ('engine_size', models.IntegerField(validators=[finalProject.motorbike.validators.engine_size_validator])),
                ('fuel_capacity', models.IntegerField(validators=[finalProject.motorbike.validators.fuel_capacity_validator])),
                ('fuel_type', models.CharField(choices=[('Diesel', 'Diesel'), ('А95Н', 'А95Н'), ('LPG', 'LPG'), ('Electricity', 'Electricity'), ('Other', 'Other')], max_length=11)),
                ('top_speed', models.IntegerField(validators=[finalProject.motorbike.validators.top_speed_validator])),
                ('emission_standard', models.CharField(choices=[('Euro I', 'Euro I'), ('Euro II', 'Euro II'), ('Euro III', 'Euro III'), ('Euro IV', 'Euro IV'), ('Euro V', 'Euro V'), ('Euro V+', 'Euro V+')], max_length=8)),
                ('price', models.FloatField(validators=[finalProject.motorbike.validators.price_validator])),
                ('short_description', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
