import json


def load_data(dbfile="db.json"):
    with open(dbfile) as f:
        data=json.load(f)
    return (data)



def signup(id,pwd):
      with open ("db.json") as f:
        data=json.load(f)
        if id not in data:
            data[id]={"PASSWORD":pwd}
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
            return True
        else:
            return False

def signin(uid,pwd):
    data=load_data("db.json")
    if data[uid]["PASSWORD"]==pwd:
        return True
    else:
        return False
    
    
    
