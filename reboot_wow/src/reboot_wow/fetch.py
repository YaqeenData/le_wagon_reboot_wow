import requests

URL = "https://owen-wilson-wow-api.onrender.com/wows/random"


def get_wow():
    response = requests.get(URL)   # 1. send the GET request
    data = response.json()         # 2. turn the JSON answer into python
    # 3. TODO: the API returns a LIST, return only the first element
    return data[0]  # return the first element of the list

if __name__ == "__main__":
    print(get_wow())