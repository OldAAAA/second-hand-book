# Generated by Django 2.1.4 on 2018-12-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0029_ordersheet_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='type',
            field=models.CharField(default='系统公告', max_length=20),
        ),
    ]