from django.db import models

# Create your models here.
#  word = ReferenceField(User)

from mongoengine import Document, EmbeddedDocument, fields


class Author(Document):
    pass

class Image(Document):
    path = fields.StringField(required=True)
    tags = fields.ListField(fields.StringField(), required=False, null=True)
    labels = fields.ListField(fields.StringField(), required=True, null=True)
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }


class Image_es(Image):
    meta = {
        'collection': 'Image_es',
        'indexes': [
            {'fields': ['$tags', "$labels"],
             'default_language': 'spanish',
             'weights': {'tags': 10, 'labels': 2}
             }
        ]}

class Image_en(Image):
    meta = {
        'collection': 'Image_en',
        'indexes': [
            {'fields': ['$tags', "$labels"],
             'default_language': 'english',
             'weights': {'tags': 10, 'labels': 2}
             }
        ]}

    # document = News.objects.search_text('testing').first()
