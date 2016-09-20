from tweety import details,new_twitter
from common import load_data,new_account
import tweety



def test_details():
    a,b,c,d=details("one","pwd1")
    assert a=="consumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"

    

def test_new_twitter():
    new_account("two","pwd2")
    new_twitter("two","pwd2","conumer_key2","csec2","atoken2","asec2")
    data=load_data("db.json","two","pwd2")
    assert data["TWITTER"]==["conumer_key2","csec2","atoken2","asec2"]

    



    
    

    
    
