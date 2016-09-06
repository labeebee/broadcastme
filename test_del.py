from broadcast_me import del_channel
def test_del_channel():
    
   data =del_channel('fb')
   assert 'fb' not in data 
