import twitter
import json
import datetime
import os
from dotenv import load_dotenv

# Loads env variables
project_folder = os.path.expanduser('~/Desktop/party_analyzer')
load_dotenv(os.path.join(project_folder, '.env'))

# Assigns env variables to necessary keys for Twitter API
consumer_key1 = os.getenv('consumer_key')
consumer_secret1 = os.getenv('consumer_secret')
access_token_key1 = os.getenv('access_token_key')
access_token_secret1 = os.getenv('access_token_secret')

# Instantiates Twitter API
api = twitter.Api(
    consumer_key=consumer_key1,
    consumer_secret=consumer_secret1,
    access_token_key=access_token_key1,
    access_token_secret=access_token_secret1,
    tweet_mode='extended'
)

# List of Twitter users that the Tweets were taken from
dem_users = ['SpeakerPelosi', 'AOC', 'IlhanMN', 'SenSchumer']
rep_users = ['realDonaldTrump', 'senatemajldr', 'SenTedCruz', 'LindseyGrahamSC']

# New tweets are added to existing data and saved to files
if os.path.exists('data/raw_dem_data.txt'):
    with open("data/raw_dem_data.txt") as infile:
        dem_data = json.load(infile)

    with open("data/raw_rep_data.txt") as infile:
        rep_data = json.load(infile)
else:
    dem_data = []
    rep_data = []

for user in dem_users + rep_users:
    tweets = api.GetUserTimeline(screen_name=user, count=200, include_rts=False)
    tweets = [_.AsDict() for _ in tweets]

    for item in tweets:
        try:
            data = {
                'tweet_id': item['id'],
                'handle': item['user']['screen_name'],
                'retweet_count': item['retweet_count'],
                'text': item['full_text'],
                'collected_at': str(datetime.datetime.now()),
                'created_at': item['created_at'],
            }

        except:
            data = {
                'tweet_id': item['id'],
                'handle': item['user']['screen_name'],
                'retweet_count': 0,
                'text': item['full_text'],
                'collected_at': str(datetime.datetime.now()),
                'created_at': item['created_at'],
            }

        if data['handle'] in dem_users and data not in dem_data:
            dem_data.append(data)
        elif data['handle'] in rep_users and data not in rep_data:
            rep_data.append(data)
        else:
            continue

with open("data/raw_dem_data.txt", "w") as outfile:
    json.dump(dem_data, outfile)

with open("data/raw_rep_data.txt", "w") as outfile:
    json.dump(rep_data, outfile)
