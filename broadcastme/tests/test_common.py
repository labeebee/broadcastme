from ..common import load_data,signup,signin

from .common import data_file

def test_load_data():
    b=load_data(data_file)
    assert len(b)>0


def test_new_account():
    signup("three","pwd3", data_file)
    data=load_data(data_file)
    assert data["three"]=={"PASSWORD":"pwd3"}

def test_signin():
      signup("one","pwd1", data_file)
      assert signin("one","pwd1", data_file)==True
    

