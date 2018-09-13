import tweepy
import csv

# Please use your own credentials
auth = tweepy.OAuthHandler('X', 'Y')
auth.set_access_token('Z',
                      'A')

api = tweepy.API(auth)

with open('prachanda_tweets.csv', 'w', encoding='utf-8') as oli_file:
    for tweet in tweepy.Cursor(api.search,
                               q="prachanda",
                               count=100,
                               geocode='27.706572,85.316189,8km',
                               result_type="recent",
                               include_entities=True,

                               lang="en").items():
        oli_csv = csv.writer(oli_file)
        print(tweet)
        oli_csv.writerow([tweet.text])

print('Hello')
