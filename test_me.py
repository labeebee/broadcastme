from tweet import load_data,details,new_twitter
import tweet




def test_details():
    a,b,c,d=details("one")
    assert a=="consumer_key"
    assert b=="consumer_secret"
    assert c=="access_token"
    assert d=="access_secret"

    

def test_new_twitter():
    new_twitter("two","pwd2","conumer_key2","csec2","atoken2","asec2")
    data=load_data("db.json")
    assert data["two"]["TWITTER"]==["conumer_key2","csec2","atoken2","asec2"]

    



    
    

    
    
