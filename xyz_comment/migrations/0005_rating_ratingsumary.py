# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-08-17 08:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import xyz_util.modelutils


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0004_auto_20200807_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('object_name', models.CharField(blank=True, db_index=True, max_length=256, null=True, verbose_name='\u540d\u79f0')),
                ('stars', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='\u8bc4\u5206')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment_ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-create_time',),
                'verbose_name': '\u8bc4\u5206',
                'verbose_name_plural': '\u8bc4\u5206',
            },
        ),
        migrations.CreateModel(
            name='RatingSumary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('object_name', models.CharField(blank=True, db_index=True, max_length=256, null=True, verbose_name='\u540d\u79f0')),
                ('score', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=3, verbose_name='\u8bc4\u5206')),
                ('user_count', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='\u53c2\u4e0e\u4eba\u6570')),
                ('detail', xyz_util.modelutils.JSONField(blank=True, default={}, verbose_name='\u8be6\u60c5')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': '\u8bc4\u5206\u6c47\u603b',
                'verbose_name_plural': '\u8bc4\u5206\u6c47\u603b',
            },
        ),
    ]
