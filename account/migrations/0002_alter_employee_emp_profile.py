# Generated by Django 5.0.1 on 2024-03-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
