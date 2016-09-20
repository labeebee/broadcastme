from tweepy import OAuthHandler
from common import load_data
import tweepy
import json


def details(id,pwd):
    data=load_data("db.json")
    if data[id]["PASSWORD"]==pwd:
        id_data=data[id]["TWITTER"]
        consumer_key=id_data[0]
        consumer_secret=id_data[1]
        access_token=id_data[2]
        access_secret=id_data[3]
        return(consumer_key,consumer_secret,access_token,access_secret)


def posting (ckey,csec,atoken,asec):
    auth= OAuthHandler(ckey,csec)
    auth.set_access_token(atoken,asec)
    tweepy.API(auth).update_status(msg)
    return True


    
def new_twitter(uid,pwd,ck,cs,at,asc):
    data=load_data("db.json")
    passw=data[uid]["PASSWORD"]
    if pwd==passw:
        if "TWITTER" not in data[uid]:
            data[uid]["TWITTER"]=[ck,cs,at,asc]
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
        else:
            print("User id Already have Twitter")
    else:
        print ("WRONG PASSWORD")

    
    
    
