
from twitter import load_data,details
import twitter



def test_load_data():
    b=load_data("one")
    assert len(twitter.acc)>0



def test_details():
    a,b,c,d=details("one")
    assert a=="consumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"
    

    
    
