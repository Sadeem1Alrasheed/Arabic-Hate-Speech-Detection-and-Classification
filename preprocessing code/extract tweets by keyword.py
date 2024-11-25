import tweepy
import pandas as pd
import re

consumer_key = "oNZq4zatcs2gtrkBrVOahhU6l"
consumer_secret = "1PrMMHVq2PKTnV0ym3QNFybsCNwQrB4X8YSBaTwuYFDrFVGv2M"
access_token = '1155998763694956544-M4OMH5LE9Wsqz9ZAFobEynPwbHQ7XW'
access_token_secret = 'MaBRruWCxmX1wL9e1wZ9CVEttkI62Fyy5S8bSC7Rvp4Gy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

keyword = 'سني'
tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="ar", result_type="recent", tweet_mode='extended').items(25)

t = {'tweet': [], 'name': [], 'country': [], 'label': []}

try:
    for tweet in tweets:
        print(tweet.user.location)
        print(tweet.user.name)
        if tweet.full_text.startswith('RT @'):
            full_text = tweet.retweeted_status.full_text
        else:
            full_text = tweet.full_text
        # Remove username from tweet text
        full_text = re.sub(r'@\w+', '', full_text)
        print(full_text)
        t['name'].append(tweet.user.name)
        t['tweet'].append(full_text)
        t['country'].append(tweet.user.location)
        t['label'].append("كراهية/غير كراهية")
        print('------------------------------------------------------------')
except tweepy.TweepError as e:
    print("Error: " + str(e))
    pass

df = pd.DataFrame(t)
df.to_excel('tweets.xlsx', index=False)