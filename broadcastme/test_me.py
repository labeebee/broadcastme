from tweety import details,new_twitter
from common import load_data,signup


def test_details():
    a=signup("one","pwd1")
    new_twitter("one","conumer_key","consumer_secret","access_token","access_secret")
    a,b,c,d=details("one")
    assert a=="conumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"


    

def test_new_twitter():

    a=signup("one","pwd1")
    if a==True:
        new_twitter("one","conumer_key","consumer_secret","access_token","access_secret")
    data=load_data("db.json")
    assert data["one"]["TWITTER"]==["conumer_key","consumer_secret","access_token","access_secret"]
    signup("two","pwd2")
    new_twitter("two","conumer_key2","csec2","atoken2","asec2")
    data=load_data("db.json")
    assert data["two"]["TWITTER"]==["conumer_key2","csec2","atoken2","asec2"]


    



    
    

    
    
