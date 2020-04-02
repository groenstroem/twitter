import json

import requests
from twitter import OAuth, Twitter

with open('config.json') as config_file:
    config = json.load(config_file)

oauth_token = config['oauth_token']
oauth_secret = config['oauth_secret']
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, consumer_key, consumer_secret))
overview = requests.get('https://grønstrøm.nu/api/v1/next-day').json()
twitter.statuses.update(status=f'{overview["title"]}\n{overview["message"]}')
