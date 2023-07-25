# Generated by Django 4.2.3 on 2023-07-25 10:44

import django.core.validators
from django.db import migrations, models
import finalProject.user_profile.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionuser',
            name='phone_number',
            field=models.CharField(default=1, max_length=10, validators=[django.core.validators.MinLengthValidator(10), finalProject.user_profile.validators.phone_number_validator]),
            preserve_default=False,
        ),
    ]
