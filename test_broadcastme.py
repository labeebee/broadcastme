import channels
from unittest import mock

def test_facebook_post():
    original_facebook = channels.facebook
    channels.facebook = mock.Mock()
    mock_graph = mock.Mock()
    channels.facebook.GraphAPI.return_value = mock_graph
    
    A = channels.FaceBook('labeebg2@gmail.com', 'password','fb_data.json')
    message = 'unit test, dependency injection test'
    A.facebook_post(message)

    channels.facebook.GraphAPI.assert_called_with("EAACEdEose0cBAJxTg1E99MyFEZAEF1uohn5y7rGBqriXlVXl9ss0Jvg4vPAB6oWQRgQPuoQTPD6rzDI7MEB1XMw2UEI8kHlrDaNgRCDOEhDPtND56Lqy8Bxai37QiMrjN4DphMzo4kl6HoGxZAAQaMrJEsZCRZC0OigzrXgiCgZDZD")
    mock_graph.get_object.assert_called_with("10202702084847551")
    mock_graph.put_wall_post.assert_called_with("unit test, dependency injection test")
    

