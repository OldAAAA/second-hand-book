# Generated by Django 2.1.4 on 2018-12-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_book_server', '0016_user_comment_comment_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
