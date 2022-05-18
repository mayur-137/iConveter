from django.contrib import admin
from .models import PopularFeatures, AllFeatures, FeatureDetails, FileUpload, FileStorage


class AuthorAdmin(admin.ModelAdmin):
    pass


class RegisterModel(admin.ModelAdmin):
    list_display = ['id', 'FeaturesName', 'FeaturesDesc', 'FeaturesExt', 'FeaturesImages']


class RegisterFeatureModel(admin.ModelAdmin):
    list_display = ['id', 'FeatureName', 'FeatureDesc', 'FeatureExt']


class UploadFile(admin.ModelAdmin):
    list_display = ['id', 'fileName', 'fileId', 'upload']


class FileStorage1(admin.ModelAdmin):
    list_display = ['id', 'UnConverted', 'Converted']


admin.site.register(PopularFeatures, RegisterModel)
admin.site.register(AllFeatures, RegisterModel)
admin.site.register(FeatureDetails, RegisterFeatureModel)
admin.site.register(FileUpload, UploadFile)
admin.site.register(FileStorage, FileStorage1)


