# Generated by Django 4.0.4 on 2022-06-01 04:53

from django.db import migrations
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', myapp.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
