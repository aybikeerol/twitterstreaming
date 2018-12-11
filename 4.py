import time
from tweepy import Stream, api
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy.api

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret =''
class listener(StreamListener):
    def on_data(self, data):
        try:

            saveFile=open('tweets.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return (True)
        except BaseException as e:
             print ("Failed on data, ", str(e))
             time.sleep(1)
    def on_error(self, status):
        print (status)

auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["python"], languages=["en"])
