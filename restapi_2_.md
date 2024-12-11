Programozás:
https://infojegyzet.hu/webszerkesztes/php/restapi/
https://requests.readthedocs.io/en/latest/
https://www.youtube.com/watch?v=eVFngZkjTlU&list=PLsYGHuNuBZcYtP1KTqyDtahvFBc0SLKQi&index=1
https://www.youtube.com/watch?v=GwSnAwsyhZY&list=PLHT5rv7PEE4N3ol8lBoxHBmzWvVW2UwmC&index=1
https://projekt.sulipy.hu/api/api_alapok

*********************************************************************************
REST API authentikáció:

1. API kulcs az url-ben
url = "https://api.example.com/data?apikey=a_te_api_kulcsod"
response = requests.get(url)


2. API kulcs a fejlécben:
headers = {
    "apikey": "a_te_api_kulcsod"
}
response = requests.get(url, headers=headers)

3. Felhasználónév és jelsző
from requests.auth import HTTPBasicAuth
response = requests.get(url, auth=HTTPBasicAuth('felhasználónév', 'jelszó'))


4. OAuth (Open Authorization)
OAuth egy nyílt szabvány az engedélyezéshez, amely lehetővé teszi, hogy egy alkalmazás hozzáférjen egy másik alkalmazás erőforrásaihoz a felhasználó nevében, anélkül, hogy megosztaná a felhasználó jelszavát. Az OAuth segítségével a felhasználók engedélyezhetik egy alkalmazás számára, hogy hozzáférjen bizonyos adatokhoz vagy funkciókhoz egy másik alkalmazásban.

Az OAuth folyamatában általában négy szereplő van:

Felhasználó: Az a személy, aki hozzáférést ad az adataihoz.
Kliens: Az az alkalmazás, amely hozzáférést kér a felhasználó adataihoz.
Engedélyező szerver: Az a szerver, amely hitelesíti a felhasználót és engedélyezi a hozzáférést.
Erőforrás szerver: Az a szerver, amely az adatokat tárolja és kiadja a kliensnek az engedélyezés után.

Példa az OAuth használatára:
Egy webalkalmazás (kliens) szeretne hozzáférni a felhasználó Google Drive fájljaihoz. A felhasználó bejelentkezik a Google fiókjába (engedélyező szerver), és engedélyezi az alkalmazás számára a hozzáférést. Az alkalmazás ezután hozzáférhet a fájlokhoz anélkül, hogy a felhasználó jelszavát ismerné.

https://api.github.com/user 

5. CORS (Cross-Origin Resource Sharing)
A CORS egy biztonsági mechanizmus, amely lehetővé teszi, hogy egy weboldal erőforrásokat kérjen le egy másik domainről. Alapértelmezés szerint a böngészők csak azonos domainről származó kéréseket engedélyeznek, de a CORS lehetővé teszi, hogy a szerver meghatározza, mely domain-ekről érkező kéréseket engedélyezi. Például, ha egy API támogatja a CORS-t, akkor egy másik domainről is lehet hozzá kéréseket küldeni.






**********************************************************************************
import requests #https://www.youtube.com/watch?v=tb8gHvYlCFs&t=429s

## 1. példa https://www.youtube.com/watch?v=hpc5jyVpUpw
# response = requests.get("https://randomfox.ca/floof")

# if response.status_code==200:
#     res=response.text
#     print("response: ")
#     print(res)
#     print("json: ")
#     json=response.json()
#     print(json)
#     print("for: ")
#     for key in json:
#         print(f"{key} : {json[key]}")

########################

#2. példa https://www.youtube.com/watch?v=U7pSXyXt4Uw   ;  https://www.youtube.com/watch?v=Xi1F2ZMAZ7Q  ;   https://www.youtube.com/watch?v=qriL9Qe8pJc  ;
payload = {"firstName": "John", "lastName": "Smith"}
res = requests.get('https://httpbin.org/get', params=payload)
print(res.text)
print()
print(res.content)
print()
json=res.json()
print(json)
print()
for key in json:
    print(f"{key} : {json[key]}")


###############################
# payload = {"firstName": "John", "lastName": "Smith"}
# res = requests.post('https://httpbin.org/post', data=payload)
# print(res.text)
# print(res.content)
# json=res.json()
# print(json)
# for key in json:
#     print(f"{key} : {json[key]}")

************************************************************************************

#https://www.youtube.com/watch?v=RDJkoUsdUmg

import requests
import colorama

parameters = {"limit": 1}
response = requests.get("https://fakestoreapi.com/products", params=parameters)


if response.status_code==200:
    res=response.text
    #print(res)
    json=response.json()
    
    #print(json)
    for dict in json:
        for key in dict:
            print(f"{key}: {dict[key]} ")


*************************************************************************************

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
