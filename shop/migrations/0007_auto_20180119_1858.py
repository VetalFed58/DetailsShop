# Generated by Django 2.0.1 on 2018-01-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_detail_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/details'),
        ),
    ]
