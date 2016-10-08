from .. import tweety
from .. import common


def test_details(data_file):
    a=common.signup("one","pwd1", data_file)
    tweety.new_twitter("one","conumer_key","consumer_secret","access_token","access_secret", data_file)
    a,b,c,d=tweety.details("one", data_file)
    assert a=="conumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"

def test_new_twitter(data_file):
    a=common.signup("one","pwd1", data_file)
    if a==True:
        tweety.new_twitter("one","conumer_key","consumer_secret","access_token","access_secret", data_file)
    data=common.load_data(data_file)
    assert data["one"]["TWITTER"]==["conumer_key","consumer_secret","access_token","access_secret"]
    common.signup("two","pwd2", data_file)
    tweety.new_twitter("two","conumer_key2","csec2","atoken2","asec2", data_file)
    data=common.load_data(data_file)
    assert data["two"]["TWITTER"]==["conumer_key2","csec2","atoken2","asec2"]


    



    
    

    
    
