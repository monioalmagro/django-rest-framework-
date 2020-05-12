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

    
    
    response = requests.post(url,data=json.dumps(payload),headers=headers)
    
        
    print(response.url)
    print(response.status_code)

    