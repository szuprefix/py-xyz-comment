# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from xyz_restful.mixins import UserApiMixin
from . import serializers, models
from rest_framework import viewsets
from xyz_restful.decorators import register

__author__ = 'denishuang'


@register()
class CommentViewSet(UserApiMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    filter_fields = {
        'content_type__app_label': ['exact'],
        'content_type__model': ['exact'],
        'content_type': ['exact'],
        'object_id': ['exact'],
        'user': ['exact']
    }

