import tweepy
import hashlib
import csv
from Twitter import TwitterTextEngine

#Token Garbage
access_token = "1234"
access_token_secret = "1234"
consumer_key = "1234"
consumer_secret = "1234"

# Oauth garbage
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#obtain a list of the users Followers and following list and assign them each a unique token based on name
def obtainTconnections(target):
    for friend in tweepy.Cursor(api.friends, screen_name=target).items():
        print('friend: ' + friend.screen_name)
        
    for follower in tweepy.Cursor(api.followers, screen_name=target).items():
        print('follower: ' + follower.screen_name)

    with open('Friends.csv', 'w', newline='') as csvfile:
        fieldnames = ['Token', 'Parent', 'Username', 'Display-Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for username in friend:
            Token = hashlib.sha256(username.screen_name.encode('utf-8')).hexdigest()
            writer.writerow({'Token': Token, 'Parent': target, 'Username': friend.user_id, 'Display-Name':friend.screen_name})

    with open('Followers.csv', 'w', newline='') as csxfile:
        fieldnames = ['Token', 'Parent', 'Username', 'Display-Name']
        writer = csv.DictWriter(csxfile, fieldnames=fieldnames)
        writer.writeheader()

        for username in friend:
            Token = hashlib.sha256(username.screen_name.encode('utf-8')).hexdigest()
            writer.writerow({'Token': Token, 'Parent': target, 'Username': friend.user_id, 'Display-Name':friend.screen_name})

def Propogate(following, friends, csvname, dec_targets): #Here we want to take the connections list and then analyze it for anything that would trace back to the original target. If we find something, add them as a decentralized taget.
    with open(friends + 'csv') as csvread:
