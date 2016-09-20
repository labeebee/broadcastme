import channels
from unittest import mock
from common import new_account
from fb_data import new_fb
def test_facebook_post():

    new_account("labeebg2@gmail.com","password")
    new_fb("labeebg2@gmail.com","password","10202702084847551","EAACEdEose0cBAJxTg1E99MyFEZAEF1uohn5y7rGBqriXlVXl9ss0Jvg4vPAB6oWQRgQPuoQTPD6rzDI7MEB1XMw2UEI8kHlrDaNgRCDOEhDPtND56Lqy8Bxai37QiMrjN4DphMzo4kl6HoGxZAAQaMrJEsZCRZC0OigzrXgiCgZDZD")

    
    original_facebook = channels.facebook
    channels.facebook = mock.Mock()
    mock_graph = mock.Mock()
    channels.facebook.GraphAPI.return_value = mock_graph
    
    A = channels.FaceBook('labeebg2@gmail.com', 'password','db.json')
    message = 'unit test, dependency injection test'
    uid="labeebg2@gmail.com"
    pwd="password"
    A.facebook_post(uid,pwd,message)

    channels.facebook.GraphAPI.assert_called_with("EAACEdEose0cBAJxTg1E99MyFEZAEF1uohn5y7rGBqriXlVXl9ss0Jvg4vPAB6oWQRgQPuoQTPD6rzDI7MEB1XMw2UEI8kHlrDaNgRCDOEhDPtND56Lqy8Bxai37QiMrjN4DphMzo4kl6HoGxZAAQaMrJEsZCRZC0OigzrXgiCgZDZD")
    mock_graph.get_object.assert_called_with("10202702084847551")
    mock_graph.put_wall_post.assert_called_with("unit test, dependency injection test")
    

