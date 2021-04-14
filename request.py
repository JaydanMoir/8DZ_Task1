import requests

def get_intelligence():
    name_heroes = ["Hulk", "Captain America", "Thanos"]
    result_smart = 0
    for name in name_heroes:
        url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
        response = requests.get(url, timeout=5)
        res = response.json()["results"][0]["powerstats"]["intelligence"]
        if int(res) >= result_smart:
            name_smart = name
            result_smart = int(res)
    return (f"Самый умный: {name_smart}, его интеллект равен {result_smart}")

print(get_intelligence())



