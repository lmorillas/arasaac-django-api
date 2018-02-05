from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework_mongoengine import viewsets as mongoviewsets
from rest_framework_mongoengine import generics as mongogenerics
from arasaacApi.imagesApi.models import Image_es, Image_en
from arasaacApi.imagesApi.serializers import UserSerializer, GroupSerializer, Image_es_Serializer, Image_en_Serializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ImageESViewSet(mongoviewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = Image_es_Serializer
    queryset = Image_es.objects.all()

    #def get_queryset(self):
    #    return Image_es.objects.all()

class ImageENViewSet(mongoviewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = Image_en_Serializer
    queryset = Image_en.objects.all()


class ImageEnSnippetList(mongogenerics.ListCreateAPIView):
    serializer_class = Image_en_Serializer
    queryset = Image_en.objects.all()
    

class ImageEnDetail(mongogenerics.RetrieveUpdateDestroyAPIView):
    serializer_class = Image_en_Serializer
    queryset = Image_en.objects.all()