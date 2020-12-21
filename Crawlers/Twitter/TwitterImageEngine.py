import argparse
import datetime
import subprocess
import urllib
import tweepy
import time
import json
import csv
import re
import os
import sys

## CREDIT TO zmwangx. He designed most of the code used here

#Step two: Extracting media
#Process:
#   1) Download Images and Video
#   2.) Store It

path = "~/Media/"
Ifolder = "/Images/"

def checkDirs():
    if not os.path.exists(path+Ifolder):
        os.makedirs(directory+Ifolder)

# Oauth stuff
oauth_json_file = os.path.expanduser('~/.config/twitter/oauth.json')
if not os.path.exists(oauth_json_file):
    print_error('no ' + oauth_json_file)
    exit(1)
oauth = json.loads(open(oauth_json_file, 'r').read())
auth = OAuthHandler(oauth['consumer_key'], oauth['consumer_secret'])
auth.set_access_token(oauth['access_token'], oauth['access_token_secret'])
api = API(auth)

#Status time!
statuses = []
for status in Cursor(api.user_timeline, screen_name=screen_name, since_id=since_id).items():
    statuses.append(status)

#Replay Backwards
for status in reversed(statuses):
    status_id = str(status.id)
    print >>status_log, status_id
    date = status.created_at.strftime('%Y%m%d%H%M%S')
    if hasattr(status, 'retweeted_status') or not hasattr(status, 'extended_entities'):
        continue
    if 'media' in status.extended_entities:
        print 'http://twitter.com/' + screen_name + '/status/' + status_id # print uri of status
        count = 0;
        for media in status.extended_entities['media']:
            count += 1
            if media['type'] == 'photo':
                image_uri = media['media_url'] + ':large'
                print image_uri
                filename = date + '-twitter.com_' + screen_name + '-' + status_id + '-' + str(count)

                if not os.path.exists(path+Ifolder+screen_name):
                    os.makedirs(directory+Ifolder+screen_name)

                filepath = (directory + Ifolder + screen_name) + '/' + filename
                # download image
                urllib.urlretrieve(image_uri, filepath)
                # identify mime type and attach extension
                if os.path.exists(filepath):
                    mime = magic.from_file(filepath, mime=True)
                    if mime == "image/gif":
                        newfilepath = filepath + ".gif"
                    elif mime == "image/jpeg":
                        newfilepath = filepath + ".jpg"
                    elif mime == "image/png":
                        newfilepath = filepath + ".png"
                    else:
                        err = filepath + ": unrecgonized image type"
                        print_error(err)
                        continue
                    os.rename(filepath, newfilepath)
                else:
                    # donwload failed for whatever reason
                    err = filename + ": failed to download " + image_uri
                    print_error(err)
                    continue
### finish traversing