from tweety import load_data,details,new_twitter,new_account
import tweety



def test_load_data():
    b=load_data("one","pwd1")
    assert len(tweety.id_details)>0



def test_details():
    a,b,c,d=details("one","pwd1")
    assert a=="consumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"

    

def test_new_twitter():
    new_account("two","pwd2")
    new_twitter("two","conumer_key2","csec2","atoken2","asec2")
    data=load_data("two","pwd2")
    assert data["TWITTER"]==["conumer_key2","csec2","atoken2","asec2"]

    

def test_new_account():
    new_account("three","pwd3")
    data=load_data("three","pwd3")
    assert data=={"PASSWORD":"pwd3"}

    
    

    
    
