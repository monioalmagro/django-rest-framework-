import requests 
import json

""" Con el methodo post obtenemos recursos, con el post lo creamos"""


if __name__ == "__main__":
    url = "http://localhost:8000/api/1.0/create_user/"
    headers = {'content-type': 'application/json'}
    payload = {
        'first_name':'Emiliano', 
        'last_name': 'Eze',
        'username':'almagro', 
        'email':'emi@gmial.got', 
        'password':12345}

    """ r = requests.get(url)
    print(r.status_code)
    print(r.headers['Content-Type']) """
   
    #response = requests.post(url,json=payload)
    #500
    response = requests.post(url,data=json.dumps(payload),headers=headers)
    #415
    #response = requests.post(url,params=payload)
    #400
    #response = requests.post(url,data=json.dumps(payload),headers=headers)
    #500
    #response = requests.post(url,data=payload,headers=headers) # lo guarda en el form
    #500
    #response = requests.post(url,data=json.dumps(payload),headers=headers)# lo guarda en data
    
    #response = requests.post(url,params=payload,headers=headers)
    #print(response.content)
    #json post se encarga de serializarlos
    #data nosotros nos encargamos de serializarlos
        
    print(response.url)
    print(response.status_code)

    #if response.status_code == 200:
    #    print(response.content)