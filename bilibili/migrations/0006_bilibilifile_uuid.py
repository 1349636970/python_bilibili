# Generated by Django 2.1.1 on 2018-11-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilibili', '0005_auto_20181101_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilibilifile',
            name='uuid',
            field=models.CharField(default='no uuid', max_length=30),
        ),
    ]
