from common import load_data,signup,signin
def test_load_data():
    b=load_data("db.json")
    assert len(b)>0


def test_new_account():
    signup("three","pwd3")
    data=load_data("db.json")
    assert data["three"]=={"PASSWORD":"pwd3"}

def test_signin():
      signup("one","pwd1")
      assert signin("one","pwd1")==True
    

