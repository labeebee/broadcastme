import json
import facebook
import requests
from .common import load_data
      
def facebook_post(uid,message):
     data = load_data("db.json")
     user_data=data[uid]["FACEBOOK"]
     access_token = user_data[1]
     graph = facebook.GraphAPI(access_token)
     profile = graph.get_object(user_data[0])
     graph.put_wall_post(message)
     return True

def new_fb(uid, user_id, access_token):
     data = load_data("db.json")
     if "FACEBOOK" not in data[uid]:
          data[uid]["FACEBOOK"] = [user_id, access_token]
          f = open("db.json","w")
          json.dump(data, f)
          f.close()
          return True
     else:
          return False
