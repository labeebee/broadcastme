import channels

def test_facebook_post():
    A = channels.FaceBook('random', 'random')
    message = 'test post from channels.py'
    acknowledgement = A.facebook_post(message)
    assert acknowledgement is True
    
    

