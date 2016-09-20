import json


def load_data(dbfile,id,pwd):
    with open(dbfile) as f:
        data=json.load(f)
        global id_details
        id_details=data[id]
        id_pwd=id_details["PASSWORD"]
        if pwd==id_pwd:
            return (id_details)



    
def new_account(id,pwd):
      with open ("db.json") as f:
        data=json.load(f)
        if id not in data:
            data[id]={"PASSWORD":pwd}
            f=open("db.json","w")
            json.dump(data,f)
            f.close()
        else:
            print("User id Already Exist")
    
