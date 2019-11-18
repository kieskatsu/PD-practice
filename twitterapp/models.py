from django.db import models

# Create your models here.
class TwitterUserData(models.Model):
    name = models.CharField(max_length=200)
    screen_name = models.CharField(primary_key=True, max_length=200)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.screen_name

class TweetData(models.Model):
    screen_name = models.ForeignKey(TwitterUserData, to_field='screen_name', on_delete=True)
    tweet_id = models.CharField(primary_key=True, max_length=200)
    embed_code = models.TextField()

    def __str__(self):
        return self.tweet_id

