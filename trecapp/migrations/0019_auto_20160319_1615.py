# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0018_auto_20160319_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='profile_picture',
            field=models.ImageField(default=b'profile_pic.png', upload_to=b'images/{{ self }}'),
            preserve_default=True,
        ),
    ]
