# Generated by Django 4.0.2 on 2022-04-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_popularfeatures_featuresimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularfeatures',
            name='FeaturesImages',
            field=models.ImageField(upload_to='', verbose_name='/media/images/'),
        ),
    ]
