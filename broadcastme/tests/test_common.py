from ..common import load_data,signup,signin

def test_load_data(data_file):
    b=load_data(data_file)
    assert len(b)>0


def test_new_account(data_file):
    signup("three","pwd3", data_file)
    data=load_data(data_file)
    assert data["three"]=={"PASSWORD":"pwd3"}

def test_signin(data_file):
      signup("one","pwd1", data_file)
      assert signin("one","pwd1", data_file)==True
    

