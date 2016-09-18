import facebook
import requests

import fb_data


 

class FaceBook:
     
     def __init__(self, username, password, filename):
          self.username = username
          self.password = password
          self.filename = filename


     def facebook_post(self, message):
          data = fb_data.load_file(self.filename)
          access_token = data[self.username][2]
          graph = facebook.GraphAPI(access_token)
          profile = graph.get_object(data[self.username][1])
          graph.put_wall_post(message)
                   
