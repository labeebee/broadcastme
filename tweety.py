from tweepy import OAuthHandler
import tweepy
import json


def load_data(id,pwd):
    with open("db.json") as f:
        data=json.load(f)
        global id_details
        id_details=data[id]
        id_pwd=id_details["PASSWORD"]
        if pwd==id_pwd:
            return (id_details)
        else:
            return(False)


def details(id,pwd):
    data=load_data(id,pwd)
    id_data=data["TWITTER"]
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


    
def new_twitter(uid,ck,cs,at,asc):
    with open ("db.json") as f:
        data=json.load(f)
        uid_data=data[uid]
        if "TWITTER" not in uid_data:
            data[uid]["TWITTER"]=[ck,cs,at,asc]
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
        else:
            print("User id Already Exist")


    
def new_account(id,pwd):
      with open ("db.json") as f:
        data=json.load(f)
        if id not in data:
            data[id]={"PASSWORD":pwd}
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
        else:
            print("User id Already Exist")
    
    
    
    
