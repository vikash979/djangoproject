# Generated by Django 2.2.1 on 2019-12-31 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drfapps', '0002_auto_20191231_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='timestamp',
        ),
    ]
