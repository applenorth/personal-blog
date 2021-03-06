# Generated by Django 2.2.1 on 2020-02-19 12:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_article_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='文章描述'),
        ),
    ]
