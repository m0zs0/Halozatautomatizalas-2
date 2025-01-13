# REST API programozás

## A Request telepítéséhez egyszerűen futtasd a következő parancsot a terminálon

```python -m pip install requests```

Importáld a Requests modult

```import requests```

Próbáld ki az alábbi API hívások egyikét:

```
response = requests.get("https://httpbin.org/get")
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
response = requests.put('https://httpbin.org/put', data={'key': 'value'})
response = requests.delete('https://httpbin.org/delete')
```

Innentől minden benne lesz a `response` objektumban.

## Paraméterek átadása URL-ekben
```
httpbin.org/get?key=val
```
helyett:
```
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=payload)
```
ezt le is ellenőrízheted a `print(response.url)` paranccsal.

## API kérések programozása


```py
# 1. példa https://www.youtube.com/watch?v=hpc5jyVpUpw
import requests 

response = requests.get("https://randomfox.ca/floof")
print(response)
print(response.status_code)
print(response.text)
print(response.content)
print(response.ok)
print(response.headers)

if response.status_code==200:
    res=response.text
    print("response: ")
    print(res)
    print("json: ")
    json=response.json()
    print(json)
    print("for: ")
    for key in json:
        print(f"{key} : {json[key]}")
```

```py
# 2. példa https://www.youtube.com/watch?v=U7pSXyXt4Uw   ;  https://www.youtube.com/watch?v=Xi1F2ZMAZ7Q  ;   https://www.youtube.com/watch?v=qriL9Qe8pJc  ;
import requests

base_url = "https://httpbin.org"
headers = {"User-Agent": "mozso"}
payload = {"firstName": "John", "lastName": "Smith"}

res = requests.get(base_url+"/get?test=pro", params=payload)
print(res.text)
print()
print(res.url)
print()
print(res.content)
print()
json=res.json()
print(json)
print()
for key in json:
    print(f"{key} : {json[key]}")
```

```py
#3. példa
import requests
payload = {"firstName": "John", "lastName": "Smith"}
res = requests.post('https://httpbin.org/post', data=payload)
print(res.text)
print(res.content)
json=res.json()
print(json)
for key in json:
    print(f"{key} : {json[key]}")

```

```py
#4. példa
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
```

```py
#5. példa
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
```

források

https://requests.readthedocs.io/en/latest/

https://infojegyzet.hu/webszerkesztes/php/restapi/

https://requests.readthedocs.io/en/latest/

https://www.youtube.com/watch?v=eVFngZkjTlU&list=PLsYGHuNuBZcYtP1KTqyDtahvFBc0SLKQi&index=1

https://www.youtube.com/watch?v=GwSnAwsyhZY&list=PLHT5rv7PEE4N3ol8lBoxHBmzWvVW2UwmC&index=1

https://projekt.sulipy.hu/api/api_alapok
