# Generated by Django 2.2.1 on 2019-08-26 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190826_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 26, 15, 49, 18, 161999)),
        ),
    ]
