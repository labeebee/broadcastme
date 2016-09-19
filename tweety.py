from tweepy import OAuthHandler
import tweepy
import json


def load_data(id):
    with open("db.json") as f:
        data=json.load(f)
        global acc
        acc=data[id]
        return (acc)


def details(id):
    data=load_data(id)
    id_data=data["twitter"]
    consumer_key=id_data[0]
    consumer_secret=id_data[1]
    access_token=id_data[2]
    access_secret=id_data[3]
    return(consumer_key,consumer_secret,access_token,access_secret)


def posting (id,msg):
    ckey,csec,atoken,asec=details(id)
    auth= OAuthHandler(ckey,csec)
    print(auth)
    auth.set_access_token(atoken,asec)
    tweepy.API(auth).update_status(msg)
    print("tweet successfully")


    
def new_twitter(uid,ck,cs,at,asc):
    with open ("db.json") as f:
        data=json.load(f)
        uid_data=data[uid]
        if "twitter" not in uid_data:
            data[uid]["twitter"]=[ck,cs,at,asc]
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
        else:
            print("User id Already Exist")
        return (data)


    
def new_account(id):
      with open ("db.json") as f:
        data=json.load(f)
        if id not in data:
            data[id]={}
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
        else:
            print("User id Already Exist")
        return (data)
    
    
    
    
