# Generated by Django 2.2.1 on 2019-11-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=200)),
                ('embbed_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUserData',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('screen_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='TwitterData',
        ),
        migrations.AddField(
            model_name='tweetdata',
            name='screen_name',
            field=models.ForeignKey(on_delete=True, to='twitterapp.TwitterUserData'),
        ),
    ]