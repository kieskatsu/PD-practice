# Generated by Django 2.2.1 on 2019-11-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0003_auto_20191110_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweetdata',
            old_name='embbed_code',
            new_name='embed_code',
        ),
    ]
