import requests
import json

url = "https://soccer-football-info.p.rapidapi.com/players/list/"

querystring = {"c":"all","p":"1"}
headers = {
	"X-RapidAPI-Host": "soccer-football-info.p.rapidapi.com",
	"X-RapidAPI-Key": "5c2e5f888bmsh3d7db9088d75be7p1dc742jsn40a7d7f31b37"
}

response = requests.request("GET", url, headers=headers, params=querystring)
dict = json.loads(response.text)
print(dict)