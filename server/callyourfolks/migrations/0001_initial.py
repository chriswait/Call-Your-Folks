# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('happened', models.NullBooleanField()),
                ('recommended', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('period', models.IntegerField(null=True)),
                ('avatar', models.ForeignKey(to='callyourfolks.Avatar')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(to='callyourfolks.User'),
        ),
        migrations.AddField(
            model_name='call',
            name='contact',
            field=models.ForeignKey(to='callyourfolks.Contact'),
        ),
        migrations.AddField(
            model_name='call',
            name='user',
            field=models.ForeignKey(to='callyourfolks.User'),
        ),
    ]
