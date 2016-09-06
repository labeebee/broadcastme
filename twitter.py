from broadcast_me import load_file

def load_data(id):
    data=load_file("twitter_db.json")
    global acc
    acc=data[id]
    
