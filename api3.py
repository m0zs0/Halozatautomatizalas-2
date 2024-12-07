######################
# Budapest időjárása #
###################### https://www.youtube.com/watch?v=qJPw_IVEyfc
#https://openweathermap.org/api

import requests

#1. geolokáció
url="http://api.openweathermap.org/geo/1.0/direct"
my_appid="2b9d8d7ce69ec344a1caac818c0e52c8"
payload = {"q": "Budapest", "limit": 5, "appid": my_appid}

response = requests.get(url, params=payload)
if response.status_code == 200:
    json=response.json()
    lat=json[0]['lat']
    lon=json[0]['lon']
    #print(f"lat: {lat}; lon: {lon}")


#2. időjárás megállapítása
url="https://api.openweathermap.org/data/2.5/weather"
payload={"lat": lat, "lon": lon, "units": "metric", "appid": my_appid}

response = requests.get(url, params=payload)
if response.status_code == 200:
    json=response.json()

    

    akt_homerseklet = json['main']['temp']
    min_homerseklet = json['main']['temp_min']
    max_homerseklet = json['main']['temp_max']
    wind_speed = json['wind']['speed']

    print(f"{min_homerseklet} <= {akt_homerseklet} <= {max_homerseklet} Celsius;\nSzél: {wind_speed}m/s")
