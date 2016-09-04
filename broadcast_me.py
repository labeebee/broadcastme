import json

def load_file(file):
    with open (file)as f:
        data=json.load(f)
    return data
        
        
def add_channel(title,u_name,pwd,key):
    data=load_file("data.json")
    if title not in data:
        data[title]=[u_name,pwd,key]
        f=open("data.json","w")
        json.dump(data,f)
        f.close()
