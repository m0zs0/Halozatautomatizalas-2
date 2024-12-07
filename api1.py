import requests #https://www.youtube.com/watch?v=tb8gHvYlCFs&t=429s

# # 1. példa https://www.youtube.com/watch?v=hpc5jyVpUpw
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