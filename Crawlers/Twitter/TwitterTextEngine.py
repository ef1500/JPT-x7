# -*- coding: utf-8 -*-
#step one - Extracting all data from the target's tweets
#   -ALL TEXT
#       -Hashtags
#       -Names
#       -Dates/Times
#       -Any Other keywords
import tweepy
import csv
import re

consumer_key = "foo"
consumer_secret = "foo"
access_token = "foo"
access_token_secret = "foo"

filename = "foo"
target_hashtag_filename = "foo"
#not dealing with this right now

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

csvFile = open(filename, 'a')
csvWriter = csv.writer(csvFile)

#obtain central target's tweets
def getTweetText(target):
    tweepy.Cursor(api.user_timeline, id=target)
    for tweet in tweepy.Cursor(api.user_timeline).pages():
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
        process_page(tweet)

#obtain all hashtags from target's posts
def obtainHashtags(filename, user):
    Hashtag_open = open(target_hashtag_filename, 'a')
    csvwriter_two = csv.writer(Hashtag_open)
    with open(filename, 'r') as ctable:
        reader = csv.reader(ctable)
        for row in reader:
            for field in row:
                htregex = (r'(?<=\s|^)#(\w*[A-Za-z_]+\w*)', field)
                if match:
                    csvwriter_two.writerow(["Hashtag", htregex.text.encode('utf-8')])

#TODO: NAME ENGINE