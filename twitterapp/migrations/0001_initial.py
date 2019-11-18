# Generated by Django 2.2.1 on 2019-11-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_name', models.CharField(max_length=200)),
                ('twitter_id', models.CharField(max_length=200)),
                ('twitter_content', models.TextField(max_length=140)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
    ]
