# Import json module
import json

# defining load_file function
def load_file(file):
    # the argument is a filename
    with open(file) as f:
        # the file is opened in f variable
        data = json.load(f)
        # the content of f is loaded in data using
        # the json function "load"
    return data # data is returned
        
        
def new_fb(username, passwd, user_id, access_token): # adds a new user detail
    data = load_file("fb_data.json")
    # call the above method
    if username not in data:
        # checks wether the given usr_id is already in
        # the loaded data or not and if not,
        data[username] = [passwd, user_id, access_token]
        # adds it to the loaded data by creating a new dictionary element
        f = open("fb_data.json","w")
        json.dump(data, f)
        # dumps the new data to f
        # overwrites data in f
        f.close()
               
    
