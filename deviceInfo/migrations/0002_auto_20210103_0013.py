# Generated by Django 3.1.4 on 2021-01-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='givento',
            name='barcode',
            field=models.IntegerField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='takenfrom',
            name='barcode',
            field=models.IntegerField(default='', unique=True),
        ),
    ]
