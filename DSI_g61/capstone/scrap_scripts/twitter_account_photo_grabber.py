import requests
import requests_oauthlib
import os
import urllib2
import base64
import time
import Imagga
import json
from PIL import Image
from pprint import pprint
'''
This script retrieve all of the user’s Tweets,
and then begin systematically working through each image
(including preview images for videos) to test which ones have weapons.
You can now go check the gunphotos directory and see the results.
'''

# initialize the API client
api_client = Imagga.swagger.ApiClient(api_server="https://api.imagga.com/v1")

# authentication setting using user name and password
api_client.username = ''
api_client.password = ''


custom_tags = set(["gun","revolver","weapon","pistol","firearm","machine gun","rifle"])

client_key    = "TWITTER_CLIENT_KEY"
client_secret = "TWITTER_CLIENT_SECRET"
token         = "TWITTER_ACCESS_TOKEN"
token_secret  = "TWITTER_TOKEN_SECRET"

oauth = OAuth1(client_key,client_secret,token,token_secret)
#
# Download Tweets from a user profile
#
def download_tweets(screen_name,max_id=None):

    api_url  = "https://api.twitter.com/1.1/statuses/user_timeline.json?"
    api_url += "screen_name=%s&" % screen_name
    api_url += "count=200"

    if max_id is not None:
        api_url += "&max_id=%d" % max_id

    # send request to Twitter
    response = requests.get(api_url,auth=oauth)

    if response.status_code == 200:
        tweets = json.loads(response.content)
        return tweets

    else:
        print("[*] Twitter API FAILED! %d" % response.status_code)

    return None


  #
  # Takes a username and begins downloading all Tweets
  #
def download_all_tweets(username):
    '''
    Takes a username and begins downloading all Tweets.
    '''
    full_tweet_list = []
    max_id          = 200

    # grab the first 200 Tweets
    tweet_list = download_tweets(username)

    # grab the oldest Tweet
    if tweet_list is None:
        return

    oldest_tweet = tweet_list[-1]
    # detect_guns("/Users/justin/Desktop/testimage.jpg")

    full_tweet_list = download_all_tweets("sikdrive_corn")

    print ("[*] Retrieved %d Tweets. Processing now..." % len(full_tweet_list))

    if not os.path.exists("gunphotos"):
        os.mkdir("gunphotos")

    photo_count = 0
    match_count = 0

    # continue retrieving Tweets
    while max_id != oldest_tweet['id']:
        full_tweet_list.extend(tweet_list)
        # set max_id to latest max_id we retrieved
        max_id = oldest_tweet['id']
        print ("[*] Retrieved: %d Tweets (max_id: %d)" % (len(full_tweet_list),max_id))
        # sleep to handle rate limiting
        time.sleep(3)
        # send next request with max_id set
        tweet_list = download_tweets(username,max_id-1)
        # grab the oldest Tweet
        if len(tweet_list):
          oldest_tweet = tweet_list[-1]


    # add the last few Tweets
    full_tweet_list.extend(tweet_list)
    # set exact path here
    # return the full Tweet list
    return full_tweet_list

# set exact path here
# detect_guns("/Users/justin/Desktop/testimage.jpg")

full_tweet_list = download_all_tweets("sikdrive_corn")

print ("[*] Retrieved %d Tweets. Processing now..." % len(full_tweet_list))

if not os.path.exists("gunphotos"):
    os.mkdir("gunphotos")

photo_count = 0
match_count = 0

for tweet in full_tweet_list:

    if tweet.has_key("extended_entities"):
        if tweet['extended_entities'] is not None:
            if tweet['extended_entities'].has_key("media"):
                for media in tweet['extended_entities']['media']:
                    print ("[*] Downloading photo %s" % media['media_url'])
                    photo_count += 1
                    response = requests.get(media['media_url'])
                    file_name = media['media_url'].split("/")[-1]
                    # write out the file
                    fd = open("gunphotos/%s" % file_name,"wb")
                    fd.write(response.content)
                    fd.close()
                    # now test for guns!
                    result = detect_guns("gunphotos/%s" % file_name)
                    if result != True:
                        os.remove("gunphotos/%s" % file_name)
                    else:
                        match_count += 1

print ("[*] Finished! Checked %d photos and detected %d with weapons." % (photo_count,match_count))
