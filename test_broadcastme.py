import channels
from unittest import mock
from common import signup,load_data
from fb_data import new_fb
def test_facebook_post():

    signup("labeebg2@gmail.com","password")
    new_fb("labeebg2@gmail.com","10202702084847551","EAACEdEose0cBAJxTg1E99MyFEZAEF1uohn5y7rGBqriXlVXl9ss0Jvg4vPAB6oWQRgQPuoQTPD6rzDI7MEB1XMw2UEI8kHlrDaNgRCDOEhDPtND56Lqy8Bxai37QiMrjN4DphMzo4kl6HoGxZAAQaMrJEsZCRZC0OigzrXgiCgZDZD")

    data= load_data("db.json")
    assert len(data["labeebg2@gmail.com"])>0
