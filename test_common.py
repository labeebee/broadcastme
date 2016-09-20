from common import load_data,new_account

def test_load_data():
    b=load_data("db.json","one","pwd1")
    assert len(b)>0


def test_new_account():
    new_account("three","pwd3")
    data=load_data("db.json","three","pwd3")
    assert data=={"PASSWORD":"pwd3"}
