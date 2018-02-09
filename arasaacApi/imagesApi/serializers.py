from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from arasaacApi.imagesApi.models import Image_es, Image_en

# Users y groups for testing 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# Image class
class Image_Serializer(mongoserializers.DocumentSerializer):
    def __init__(self, *args, **kwargs):
        super(Image_Serializer, self).__init__(*args, **kwargs)
        # restrict get with fields param
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
                fields = request.query_params.get('fields')
                if fields:
                    fields = fields.split(',')
                    allowed = set(fields)
                    existing = set(self.fields.keys())
                    for field_name in existing - allowed:
                        self.fields.pop(field_name)
    class Meta:
        #model = Image_es  
        model = None # Agnostic model. Detemined later with the request param
        fields = ('id', 'path', 'tags', 'labels')


# One serializer for lang ? 
# Langs used by mongo ?