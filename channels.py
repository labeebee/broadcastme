import facebook
import requests

import fb_data


data = fb_data.load_file("fb_data.json")
 

class FaceBook:

     
     
     def __init__(self, username, password):
         self.username = username
         self.password = password

     def authenticate(self, username, password):
         # Currently we are passing the Access Token manually
         # via the variable above. However in the future we will be using
         # this method.
         return access_token

     def facebook_post(self, message):
         access_token = data[self.username][2]
         graph = facebook.GraphAPI(access_token)
         profile = graph.get_object(data[self.username][1])
         if (graph.put_wall_post(message)):
             acknw = True
             return acknw
         
