# Generated by Django 4.2.1 on 2023-07-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotquotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='quoter',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=225),
        ),
    ]