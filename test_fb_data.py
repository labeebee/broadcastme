from fb_data import new_fb
from common import load_data,new_account
def test_new_fb():
    new_account("fb_user","fb")
    new_fb("fb_user","fb","user_id","accesstoken")
    a=load_data("db.json")
    assert len(a["fb_user"])>0
