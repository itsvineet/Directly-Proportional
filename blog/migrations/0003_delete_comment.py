# Generated by Django 2.0.7 on 2019-02-08 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
