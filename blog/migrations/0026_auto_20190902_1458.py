# Generated by Django 2.2.4 on 2019-09-02 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190901_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 14, 58, 20, 270842)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 14, 58, 20, 268874)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
