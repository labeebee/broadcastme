import json


def load_data(dbfile):
    with open(dbfile) as f:
        data=json.load(f)
    return (data)



    
def signup(id, pwd, dbfile):
      with open (dbfile) as f:
        data=json.load(f)
        if id not in data:
            data[id]={"PASSWORD":pwd}
            f=open(dbfile,"w")
            json.dump(data,f)
            f.close()
        else:
            return True
        

def signin(uid, pwd, dbfile):
    data=load_data(dbfile)
    if uid in data:
        if data[uid]["PASSWORD"]==pwd:
            return True
        else:
            return False
    else:
        return False
    
    

    
