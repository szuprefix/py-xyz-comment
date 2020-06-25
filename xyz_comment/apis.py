# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from xyz_restful.mixins import UserApiMixin
from . import serializers, models, helper
from rest_framework import viewsets
from xyz_restful.decorators import register

__author__ = 'denishuang'


@register()
class CommentViewSet(UserApiMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    filter_fields = {
        'content_type': ['exact'],
        'object_id': ['exact'],
        'user': ['exact'],
        'reply_count': ['gte', 'lte']
    }

    def filter_queryset(self, queryset):
        qset = super(CommentViewSet, self).filter_queryset(queryset)
        ct = self.request.query_params.get('content_type')
        if not ct:
            ctid = helper.get_comment_content_type_id()
            return qset.exclude(content_type=ctid)
        return qset

