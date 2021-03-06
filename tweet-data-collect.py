# coding:utf-8
import sqlite3
import twitter

access_token_key = '2756721354-lyn1tMpWGfBTC2gXBNY2gq2dCrTbSe5yAW4kki6'
access_token_secret = 'g5f8bu2oAdyTd6b8JzNyHAIoYOKfqgpAyNXYVFZiayJA9'
consumer_key = 'yo9u0g2v6EypTepcA47UhokbR'
consumer_secret = '7sTUmfPVNZnLVdksI9CtlftzvdBelWYBVHGD42L3kqVCVVZYU2'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret
)

def get_embed(stat_id, url):
    try:
        embed = api.GetStatusOembed(status_id=stat_id, url=url, align='center')['html']
        return embed
    except:
        import traceback
        traceback.print_exc()

def get_search_info(search, count):
    '''
    search -> search word\n
    count -> number of tweets you want to get\n
    return [[(name, screen_name, 0),...], [(embed_code, screen_name, tweet_id),...]]
    '''
    try:
        tweets = api.GetSearch(term=search, count=count, lang="ja", result_type="recent")
        user_list = []
        tweet_list =[]
        for tweet in tweets:
            embed_code = get_embed(tweet.id_str, 'https://twitter.com/{}/status/{}'.format(
                tweet.id_str, tweet.user.screen_name
            ))
            user_list.append((tweet.user.name, tweet.user.screen_name, 0))
            tweet_list.append((embed_code, tweet.user.screen_name, tweet.id_str))
        return [user_list, tweet_list]
    except:
        import traceback
        traceback.print_exc()

def save_tweets_data(list):
    try:
        con = sqlite3.connect('./db.sqlite3')
        cur = con.cursor()

        extinct_sql = "select screen_name from twitterapp_twitteruserdata"
        screen_name_list = [i for i in cur.execute(extinct_sql)] # make extinct user_list
        user_list = set(filter(lambda x: x[1] not in screen_name_list, list[0]))

        user_sql = u"insert into twitterapp_twitteruserdata (name, screen_name, point) values (?,?,?)"
        tweet_sql = u"insert into twitterapp_tweetdata (embed_code, screen_name_id, tweet_id) values(?,?,?)"

        cur.executemany(user_sql, user_list) #user_list (converted)
        cur.executemany(tweet_sql, list[1]) #tweet_list
        con.commit()
        con.close()
    except:
        import traceback
        traceback.print_exc()

def main():
    tweets_list = get_search_info(search=u'#かわいい動物', count=1)
    save_tweets_data(tweets_list)

if __name__ == '__main__':
    main()
