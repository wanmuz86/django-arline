# Generated by Django 4.0.5 on 2022-06-21 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_flight_flydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='fligtnumber',
            field=models.CharField(default='000', max_length=10),
        ),
    ]