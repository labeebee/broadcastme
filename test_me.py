from broadcast_me import load_file,add_channel,tweet
from twitter import tweet



def test_tweet():
    b=tweet("one")
    assert len(b.ac)>0


    
    
