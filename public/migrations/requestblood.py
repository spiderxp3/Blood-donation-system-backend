# Generated by Django 3.1.7 on 2021-08-08 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', 'initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestBlood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('donation_location', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=500)),
                ('date_of_donation', models.DateField(help_text='yyyy-mm-dd')),
                ('pin_code', models.IntegerField(help_text='You can edit your request later using this code', unique=True)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bloodgroup')),
            ],
        ),
    ]
