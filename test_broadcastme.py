import channels

def test_facebook_post():
    A = channels.FaceBook('labeebg2@gmail.com', 'password')
    message = '2nd refactor test post from channels.py'
    acknowledgement = A.facebook_post(message)
    assert acknowledgement is True
    
    

