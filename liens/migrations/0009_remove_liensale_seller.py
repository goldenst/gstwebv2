# Generated by Django 2.2 on 2019-12-10 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liens', '0008_liensale_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liensale',
            name='seller',
        ),
    ]
