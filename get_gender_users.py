import json

import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    gender=[]
    for i in data['results']:
        if i['gender']=='male':
            gender+=[1]
        elif i['gender']=='female':
            gender+=[0]
    return gender
f=open('randomuser_data.json').read()
data=json.loads(f)
print(get_gender_users(data))