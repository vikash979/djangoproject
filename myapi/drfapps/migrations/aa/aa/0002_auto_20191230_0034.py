# Generated by Django 2.2.5 on 2019-12-30 00:34

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('drfapps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='event',
            managers=[
                ('events', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
