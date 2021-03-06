# Generated by Django 3.1.4 on 2021-01-02 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenFrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField(default='', max_length=255, unique=True)),
                ('modelName', models.CharField(default='', max_length=200)),
                ('takenfrom', models.CharField(default='', max_length=200)),
                ('date', models.DateField(default='', max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GivenTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField(default='', max_length=255, unique=True)),
                ('modelName', models.CharField(default='', max_length=200)),
                ('givento', models.CharField(default='', max_length=200)),
                ('date', models.DateField(default='', max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
