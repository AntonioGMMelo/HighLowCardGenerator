# Generated by Django 3.1.3 on 2020-12-16 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicationHLCG', '0003_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesettings',
            name='user',
        ),
    ]