# Generated by Django 2.2.1 on 2020-02-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.IntegerField(choices=[(0, '女'), (1, '男')], verbose_name='性别'),
        ),
    ]