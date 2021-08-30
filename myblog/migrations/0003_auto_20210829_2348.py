# Generated by Django 3.2.6 on 2021-08-29 18:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20210829_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 29, 18, 18, 22, 967770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 8, 29, 18, 18, 22, 966770, tzinfo=utc)),
        ),
    ]