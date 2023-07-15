import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f=open(filename).read()
    return json.loads(f)
filename='randomuser_data.json'
print(get_data(filename))