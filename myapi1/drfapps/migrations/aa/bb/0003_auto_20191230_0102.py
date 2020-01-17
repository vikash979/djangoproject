# Generated by Django 2.2.5 on 2019-12-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapps', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_staff',
            new_name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
