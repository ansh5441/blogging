import json

from django.contrib.auth.models import User
from django.core import serializers
from django.db import models


def get_dictionary(obj):
    data = serializers.serialize("json", [obj])
    dictionary = json.loads(data)[0]['fields']
    dictionary['id'] = obj.id
    dictionary.pop('created')
    dictionary.pop('updated')
    return dictionary


class Blog(models.Model):
    title = models.CharField(max_length=256, default="")
    body = models.TextField(default="")
    writer = models.ForeignKey(User)
    thumb = models.ImageField(upload_to='thumb')

    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def get_dictionary(self):
        return get_dictionary(self)


class Comment(models.Model):
    text = models.TextField(default="")
    writer = models.ForeignKey(User)
    parent = models.ForeignKey(Blog)
    parent_comment = models.IntegerField(db_index=True)

    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def get_dictionary(self):
        return get_dictionary(self)
