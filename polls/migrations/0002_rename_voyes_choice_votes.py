# Generated by Django 3.2 on 2021-04-26 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='voyes',
            new_name='votes',
        ),
    ]
