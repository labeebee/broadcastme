import json
from common import load_data

def new_fb(uid, pwd, user_id, access_token):
    data = load_data("db.json")
    passw=data[uid]["PASSWORD"]
    if pwd==passw:
        if "FACEBOOK" not in data[uid]:
            data[uid]["FACEBOOK"] = [user_id, access_token]
            f = open("db.json","w")
            json.dump(data, f)
            f.close()
        else:
            print("User have already have Facebook")
    else:
        print("WRONG PASSWORD")
        
