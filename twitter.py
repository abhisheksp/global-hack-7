import json
from TwitterAPI import TwitterAPI

with open('twitter.json') as f:
    data = json.load(f)
    api = TwitterAPI(
        data['consumer_key'],
        data['consumer_secret'],
        data['access_token'],
        data['access_token_secret']
    )


def tweet(message):
    api.request('statuses/update', {'status': message})
