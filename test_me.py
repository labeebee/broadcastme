from tweety import details,new_twitter
from common import load_data,new_account
import tweety



def test_details():
   a,b,c,d=details("one","pwd1")
   assert a=="conumer_key1"
   assert b=="csec1"
   assert c=="atoken1"
   assert d=="asec1"

    

def test_new_twitter():
    new_account("one","pwd1")
    new_twitter("one","pwd1","conumer_key1","csec1","atoken1","asec1")
    data=load_data("db.json")
    assert data["one"]["TWITTER"]==["conumer_key1","csec1","atoken1","asec1"]

    



    
    

    
    
