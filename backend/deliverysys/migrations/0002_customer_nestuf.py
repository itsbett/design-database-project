# Generated by Django 4.0.4 on 2022-04-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverysys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nestuf',
            field=models.TextField(default=''),
        ),
    ]