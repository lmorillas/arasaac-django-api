from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework_mongoengine import viewsets as mongoviewsets
from rest_framework_mongoengine import generics as mongogenerics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from arasaacApi.imagesApi.serializers import UserSerializer, GroupSerializer, Image_Serializer
from django.apps import apps 
from arasaacApi.imagesApi import models
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
import coreapi
import coreschema
from rest_framework.filters import BaseFilterBackend



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


class ImagesFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='q',
                location='query',
                required=False,
                type='string',
                schema=coreschema.String(
                        title='Search string',
                        description="Search text string"
                    )
            ),
            coreapi.Field(
                name='tags',
                location='query',
                required=False,
                type='string',
                schema=coreschema.String(
                        title='Search string',
                        description="Search string in tags field"
                    )
            ),
            coreapi.Field(
                name='labels',
                location='query',
                required=False,
                type='string',
                schema=coreschema.String(
                        title='Labels',
                        description="Search string in labels field"
                    )
            ),
        ]
    def filter_queryset(self, request, queryset, view):
        words = request.query_params.get('q', None)
        if words is not None:
            return queryset.search_text(words).order_by('$text_score')
        tags = request.query_params.get('tags')
        if tags:
            queryset = queryset(tags=tags)
        labels = request.query_params.get('labels')
        if labels:
            queryset = queryset(labels=labels)
        return queryset.all()
        


class ImageESViewSet(mongoviewsets.ModelViewSet):
    '''
    retrieve: Return the given image.

    list: Return a list of all the existing images.

    create: Create a new image instance.

    retrieve: Show a single given image.

    update: Updates a single image.

    partial_update: updates a single image with a partial set of input.

    destroy: removes the given resource.
    '''
    lookup_field = 'id'
    serializer_class = Image_Serializer
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (ImagesFilterBackend,)

    @property
    def model(self):
        return getattr(models, 'Image_' + self.kwargs['lang'])

    def get_serializer_class(self):
        Image_Serializer.Meta.model = self.model
        return Image_Serializer
    
    def get_queryset(self):
        return self.model.objects

    '''
    # TODO: words as route or as param?
    @list_route()
    def words(self, request, lang=None):
        words = self.request.query_params.get('q', None)
        if words is not None:
            image_list = self.model.objects.search_text(words).order_by('$text_score')
        else:
            image_list = []

        page = self.paginate_queryset(image_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(image_list, many=True)
        return Response(serializer.data)
    '''
    