# Generated by Django 3.1.7 on 2021-08-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', 'donorpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestblood',
            name='date_of_donation',
        ),
        migrations.RemoveField(
            model_name='requestblood',
            name='pin_code',
        ),
        migrations.AddField(
            model_name='requestblood',
            name='date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
