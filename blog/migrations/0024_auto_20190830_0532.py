# Generated by Django 2.2.1 on 2019-08-30 00:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190830_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 5, 32, 34, 411544)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 5, 32, 34, 409645)),
        ),
    ]
