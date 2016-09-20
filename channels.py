import facebook
import requests
from common import load_data

import fb_data

class FaceBook:
     
     def __init__(self, username, password, filename):
          self.username = username
          self.password = password
          self.filename = filename


     def facebook_post(self,uid,message):
          data = load_data(self.filename)
          user_data=data[uid]["FACEBOOK"]
          access_token = user_data[1]
          graph = facebook.GraphAPI(access_token)
          profile = graph.get_object(data[self.username][1])
          graph.put_wall_post(message)
                   
