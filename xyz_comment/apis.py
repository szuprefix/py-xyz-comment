# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from xyz_restful.mixins import UserApiMixin
from xyz_util.statutils import do_rest_stat_action

from . import serializers, models, stats
from rest_framework import viewsets, exceptions, response, decorators, permissions
from xyz_restful.decorators import register

__author__ = 'denishuang'


@register()
class CommentViewSet(UserApiMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = {
        'content_type': ['exact'],
        'object_id': ['exact'],
        'user': ['exact'],
        'create_time': ['range'],
        'reply_count': ['gte', 'lte']
    }

    def filter_queryset(self, queryset):
        qset = super(CommentViewSet, self).filter_queryset(queryset)
        ct = self.request.query_params.get('content_type')
        if not ct and self.action == 'list':
            return qset.exclude(content_type=ContentType.objects.get_for_model(models.Comment))
        return qset


@register()
class FavoriteViewSet(UserApiMixin, viewsets.ModelViewSet):
    serializer_class = serializers.FavoriteSerializer
    queryset = models.Favorite.objects.all()
    permission_classes = []
    filter_fields = {
        'content_type': ['exact'],
        'object_id': ['exact', 'in'],
        'user': ['exact'],
        'create_time': ['range']
    }

    @decorators.list_route(['GET', 'POST'])
    def record(self, request):
        qs = request.query_params
        if not qs.get('content_type'):
            raise exceptions.ValidationError('content_type should not be empty.')
        if not qs.get('object_id'):
            raise exceptions.ValidationError('object_id should not be empty.')
        qd = dict(user=request.user, content_type=qs.get('content_type'), object_id=qs.get('object_id'))
        f = self.get_queryset().filter(**qd).first()
        if request.method == 'GET':
            if not f:
                return response.Response(qs)
        elif request.method == 'POST':
            if not f:
                qd['content_type'] = ContentType.objects.get(id=qd['content_type'])
                f = models.Favorite(party=self.party, **qd)
            d = request.data
            f.notes[d['anchor']] = d
            f.save()
        return response.Response(self.get_serializer_class()(f).data)


    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_favorite)

