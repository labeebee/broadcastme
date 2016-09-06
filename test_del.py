import broadcast_me
def test_del_channel():
    
   data = del_channel('fb')
   assert 'fb' not in data 
