# Generated by Django 2.2 on 2019-12-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liens', '0002_auto_20191209_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='liensale',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
