from rest_framework import serializers


class PopularFeaturesSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    FeaturesName = serializers.CharField(max_length=200)
    FeaturesDesc = serializers.CharField(max_length=2000)
    # FeaturesImages = serializers.ImageField('/media/images/')


class AllFeaturesSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    FeaturesName = serializers.CharField(max_length=200)
    FeaturesDesc = serializers.CharField(max_length=2000)
    # FeaturesImages = serializers.ImageField('/media/images/')