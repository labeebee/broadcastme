from common import load_data,new_account,load_user_data

def test_load_data():
    b=load_data("db.json")
    assert len(b)>0


def test_new_account():
    new_account("three","pwd3")
    data=load_data("db.json")
    assert data["three"]=={"PASSWORD":"pwd3"}

def test_load_user_data():
    ud=load_user_data("db.json","three","pwd3")
    assert ud=={"PASSWORD": "pwd3"}
