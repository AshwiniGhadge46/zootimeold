# Generated by Django 4.2.2 on 2023-07-03 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
