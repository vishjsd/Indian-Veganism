# Generated by Django 3.0.8 on 2021-05-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=2, upload_to='media'),
            preserve_default=False,
        ),
    ]