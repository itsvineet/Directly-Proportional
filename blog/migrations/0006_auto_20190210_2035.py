# Generated by Django 2.1.5 on 2019-02-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190209_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='NO NAME', max_length=256),
        ),
    ]
