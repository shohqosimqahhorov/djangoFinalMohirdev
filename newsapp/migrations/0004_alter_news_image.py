# Generated by Django 4.0 on 2023-12-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/images'),
        ),
    ]