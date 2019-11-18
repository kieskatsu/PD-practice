from django.contrib import admin
from twitterapp.models import TwitterUserData, TweetData

# Register your models here.
admin.site.register(TwitterUserData)
admin.site.register(TweetData)