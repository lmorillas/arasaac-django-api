from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from arasaacApi.imagesApi.models import Image_es, Image_en


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class Image_es_Serializer(mongoserializers.DocumentSerializer):
    #def create(self, validated_data):
    #    return Image_es.objects.create(**validated_data)    

    class Meta:
        model = Image_es
        fields = '__all__'

class Image_en_Serializer(mongoserializers.DocumentSerializer):
    #def create(self, validated_data):
    #    return Image_en.objects.create(**validated_data)    

    class Meta:
        model = Image_en
        fields = '__all__'