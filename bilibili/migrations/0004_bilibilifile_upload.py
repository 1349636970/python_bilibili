# Generated by Django 2.1.1 on 2018-11-01 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilibili', '0003_auto_20181025_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilibilifile',
            name='upload',
            field=models.FileField(default='no file', upload_to='../videos'),
        ),
    ]