# Generated by Django 4.2.13 on 2024-05-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityrequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
