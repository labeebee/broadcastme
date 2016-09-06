from broadcast_me import load_file
from tweepy import OAuthHandler
import tweepy
def load_data(id):
    data=load_file("twitter_db.json")
    global acc
    acc=data[id]
    return (acc)
    
def details(id):
    ac=load_data(id)
    consumer_key=ac[0]
    consumer_secret=ac[1]
    access_token=ac[2]
    access_secret=ac[3]
    return(consumer_key,consumer_secret,access_token,access_secret)


def posting (id,msg):
    ckey,csec,atoken,asec=details(id)
    auth= OAutHandler(ckey,csec)
    auth.set_access_token(atoken,asec)
    tweepy.API(auth).update_status(msg)
    print("tweet successfully")
    
    
    
