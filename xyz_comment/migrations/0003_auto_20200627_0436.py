# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-06-27 04:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import xyz_util.modelutils


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_auto_20200204_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('object_name', models.CharField(blank=True, db_index=True, max_length=256, null=True, verbose_name='\u540d\u79f0')),
                ('notes', xyz_util.modelutils.JSONField(blank=True, default={}, verbose_name='\u7b14\u8bb0')),
                ('notes_count', models.PositiveSmallIntegerField(blank=True, default=1, verbose_name='\u7b14\u8bb0\u6570')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6709\u6548')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_favorites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-create_time',),
                'verbose_name': '\u6536\u85cf',
                'verbose_name_plural': '\u6536\u85cf',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_count',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False, verbose_name='\u56de\u8d34\u6570'),
        ),
    ]
