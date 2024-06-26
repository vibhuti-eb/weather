# Generated by Django 4.2.13 on 2024-05-29 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bodyapp', '0002_alter_cityrequest_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherResponse',
            fields=[
                ('cityRequest', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='bodyapp.cityrequest')),
                ('longitude', models.CharField(max_length=10)),
                ('latitude', models.CharField(max_length=10)),
                ('temperature', models.CharField(max_length=5)),
                ('pressure', models.CharField(max_length=10)),
                ('humidity', models.CharField(max_length=10)),
            ],
        ),
    ]
