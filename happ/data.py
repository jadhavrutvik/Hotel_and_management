import requests
import json
URL="http://127.0.0.1:8000/"
def stuget(no=None):
    data={}
    if no is not None:
        data={'no':no}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
stuget()
    
def studpost():
    data={
        'no':4,
        'name':'idali',
        'image':'/media/media/123.jpg',
        'price':30,
        'details':'ajsnnnfdnsihdfan'

    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    d=r.json()
    print(d)
# studpost()
    
def studupdate():
    data={
        'no':3,
        'name':'poha',
        'price':50
        
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    d=r.json()
    print(d)
# studupdate()

def studdelete():
    data={
        'no':1
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    d=r.json()
    print(d)

# studdelete()