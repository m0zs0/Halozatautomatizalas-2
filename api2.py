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
