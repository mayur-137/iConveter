# Generated by Django 4.0.3 on 2022-05-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_fileupload_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allfeatures',
            name='FeaturesImages',
            field=models.ImageField(upload_to='', verbose_name='/media/images/img_internal'),
        ),
        migrations.AlterField(
            model_name='popularfeatures',
            name='FeaturesImages',
            field=models.ImageField(upload_to='', verbose_name='/media/images/img_internal'),
        ),
    ]
