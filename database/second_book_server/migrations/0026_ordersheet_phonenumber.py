# Generated by Django 2.1.4 on 2018-12-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0025_auto_20181217_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersheet',
            name='phonenumber',
            field=models.IntegerField(default='18801119875'),
        ),
    ]