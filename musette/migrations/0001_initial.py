# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-24 18:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import musette.models
import musette.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idcategory', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('position', models.IntegerField(blank=True, default=0)),
                ('hidden', models.BooleanField(default=False, help_text='If checked, this category will be visible only for staff')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['position'],
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('idcomment', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['date'],
                'verbose_name': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('idconfig', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.FileField(blank=True, null=True, upload_to=musette.models.Configuration.generate_path_configuration)),
                ('logo_width', models.PositiveIntegerField(blank=True, help_text='In pixels', null=True, verbose_name='Logo width')),
                ('logo_height', models.PositiveIntegerField(blank=True, help_text='In pixels', null=True, verbose_name='Logo height')),
                ('custom_css', models.TextField(blank=True, null=True, verbose_name='Custom design')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Configurations',
                'verbose_name': 'Configuration',
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('idforum', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Name')),
                ('position', models.IntegerField(blank=True, default=0, verbose_name='Position')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('topics_count', models.IntegerField(blank=True, default=0, editable=False, verbose_name='Topics count')),
                ('hidden', models.BooleanField(default=False, help_text='If hide the forum in the index page', verbose_name='Hidden')),
                ('is_moderate', models.BooleanField(default=False, help_text='If the forum is moderated', verbose_name='Check topics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='musette.Category', verbose_name='Category')),
                ('moderators', models.ManyToManyField(related_name='moderators', to=settings.AUTH_USER_MODEL, verbose_name='Moderators')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='musette.Forum', verbose_name='Parent forum')),
            ],
            options={
                'verbose_name_plural': 'Forums',
                'ordering': ['category', 'position', 'name'],
                'verbose_name': 'Forum',
            },
        ),
        migrations.CreateModel(
            name='MessageForum',
            fields=[
                ('idmessage_forum', models.AutoField(primary_key=True, serialize=False)),
                ('message_information', models.TextField(help_text='If you want to report a message to a forum', verbose_name='Message to inform')),
                ('message_expires_from', models.DateTimeField(help_text='Date from message expired', verbose_name='Message expires from')),
                ('message_expires_to', models.DateTimeField(help_text='Date to message expired', verbose_name='Message expires to')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_information', to='musette.Forum', verbose_name='Forum')),
            ],
            options={
                'verbose_name_plural': 'Messages for forums',
                'verbose_name': 'Message for forums',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('idnotification', models.AutoField(primary_key=True, serialize=False)),
                ('idobject', models.PositiveIntegerField(null=True)),
                ('iduser', models.IntegerField(default=0)),
                ('is_topic', models.BooleanField(default=0)),
                ('is_comment', models.BooleanField(default=0)),
                ('is_view', models.BooleanField(default=0)),
                ('date', models.DateTimeField(blank=True, db_index=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('idregister', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register_forums', to='musette.Forum', verbose_name='Forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register_users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Registers',
                'ordering': ['date'],
                'verbose_name': 'Register',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('idtopic', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=100)),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Last activity')),
                ('description', models.TextField(verbose_name='Description')),
                ('id_attachment', models.CharField(blank=True, max_length=200, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to=musette.models.Topic.generate_path, validators=[musette.validators.valid_extension_image], verbose_name='File')),
                ('is_close', models.BooleanField(default=False, help_text='If the topic is close', verbose_name='Closed topic')),
                ('moderate', models.BooleanField(default=False, help_text='If the topic is moderated', verbose_name='Moderate')),
                ('is_top', models.BooleanField(default=False, help_text='If the topic is important and it will go top', verbose_name='Top')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='musette.Forum', verbose_name='Forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'ordering': ['forum', 'last_activity', 'title', 'date'],
                'verbose_name': 'Topic',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='musette.Topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_users', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
