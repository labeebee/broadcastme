import facebook
import requests

# The variable access_token is temporarily defined manually for now.
# The authenticate() function is supposed to provide the same in the future.
access_token = 'EAACEdEose0cBACx37U2G8mqvItLnPcFWIbZCr6Hsm92B7ctpx7kA6PYhdhZAtGYOzir0oPEvohoGVyPf8EZA80MT3LjqITwpbTMoct7BZCFyNmkBZA7rmJZADAxyZCypPK7YzIXKZAUYrZCzCSbUt23Upn00MX5akBUiHEQgvIkgeTAZDZD'

# temporarily declared as authenticate() is not implemented
user = '10202702084847551' 

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
         graph = facebook.GraphAPI(access_token)
         profile = graph.get_object(user)
         if (graph.put_wall_post(message)):
             acknw = True
             return acknw
         
