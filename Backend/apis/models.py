from django.db import models


class PopularFeatures(models.Model):
    id = models.IntegerField(primary_key=True)
    FeaturesName = models.CharField(max_length=200)
    FeaturesDesc = models.CharField(max_length=2000)
    FeaturesExt = models.CharField(max_length=20, default='')
    FeaturesImages = models.ImageField('/media/images/img_internal')


class AllFeatures(models.Model):
    id = models.IntegerField(primary_key=True)
    FeaturesName = models.CharField(max_length=200)
    FeaturesDesc = models.CharField(max_length=2000)
    FeaturesExt = models.CharField(max_length=20, default='')
    FeaturesImages = models.ImageField('/media/images/img_internal')


class FileUpload(models.Model):
    id = models.IntegerField(primary_key=True)
    fileName = models.CharField(max_length=200)
    fileId = models.IntegerField()
    upload = models.FileField(upload_to="media/unConverted", default='null')


class FeatureDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    FeatureName = models.CharField(max_length=50)
    FeatureDesc = models.CharField(max_length=500)
    FeatureExt = models.CharField(max_length=10)


class FileStorage(models.Model):
    id = models.IntegerField(primary_key=True)
    UnConverted = models.CharField(max_length=500)
    Converted = models.CharField(max_length=500)


