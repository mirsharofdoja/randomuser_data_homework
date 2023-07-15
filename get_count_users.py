import json

import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    return len(data['results'])
f=open('randomuser_data.json').read()
data=json.loads(f)
print(get_count_users(data))
