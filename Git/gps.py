import requests
from json import dumps


start = input("Geef de startlocatie: ")
einde = input("Geef de eindlocatie: ")

url = f"https://www.mapquestapi.com/directions/v2/route?key=FGyArdui5tWcpKtygEg7nUmV2tQv2nfJ&from={start}&to={einde}&unit=k"
response = requests.get(url)
 
json = response.json()
statuscode = json["info"]["statuscode"]

if statuscode != 0:
    message = json["info"]["messages"][0] 
    print(statuscode, message)
else:
    print(json["route"]["distance"], "km")
    print(json["route"]["formattedTime"])
    maneuvers = json["route"]["legs"][0]["maneuvers"]
    for maneuver in maneuvers: 
        print(dumps(maneuver, indent=4)) 
        # print(maneuver["narrative"])