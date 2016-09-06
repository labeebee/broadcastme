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

def del_channel(key):
	data = load_file("data.json")
	if key in data:
		del data[key]
		print 'removed data'
		open("data.json", "w").write(json.dumps(data,sort_keys=True,indent=4,separators=(',', ':')))
	else:
		print 'Unable to find the key'
	return data
if __name__ == '__main__':
	del_channel('fb')
