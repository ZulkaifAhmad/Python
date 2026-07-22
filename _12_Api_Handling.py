import requests

def handle_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
    timeZoneOfFirstElement = data["data"]["data"][0]["location"]["timezone"]
    print(timeZoneOfFirstElement)    
    return data

if __name__ == "__main__":
    handle_api()
    
    

