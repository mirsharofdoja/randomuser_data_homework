import json
import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails=[]
    for i in data['results']:
        emails.append(i['email'])
    return emails
f=open('randomuser_data.json').read()
data=json.loads(f)
print(get_email(data))