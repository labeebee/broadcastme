
from tweety import load_data,details,new_twitter,new_account
import tweety



def test_load_data():
    b=load_data("one")
    assert len(tweety.acc)>0



def test_details():
    a,b,c,d=details("one")
    assert a=="consumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"

def test_new_twitter():
  
    b=new_twitter("two","conumer_key2","csec2","atoken2","asec2")
    assert b["two"]["twitter"]==["conumer_key2","csec2","atoken2","asec2"]

def test_new_account():
    b=new_account("three")
    assert b["three"]=={}

    
    

    
    
