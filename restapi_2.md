REST API authentikáció:

1. API kulcs az url-ben
url = "https://api.example.com/data?apikey=a_te_api_kulcsod"
response = requests.get(url)


2. API kulcs a fejlécben:
headers = {
    "apikey": "a_te_api_kulcsod"
}
response = requests.get(url, headers=headers)

3. Felhasználónév és jelszó
from requests.auth import HTTPBasicAuth
response = requests.get(url, auth=HTTPBasicAuth('felhasználónév', 'jelszó'))


4. Személyes Hozzáférési Token (Personal Access Token - Bearer token)
A felhasználónév és jelszó helyett használható az API hívásokhoz. Biztonságosabb, mint a jelszó használata, mivel a tokenek korlátozott jogosultságokkal rendelkezhetnek.
Példa: A GitHub API esetében a token a Bearer fejlécben kerül elküldésre.

5. OAuth (Open Authorization)
OAuth egy nyílt szabvány az engedélyezéshez, amely lehetővé teszi, hogy egy alkalmazás hozzáférjen egy másik alkalmazás erőforrásaihoz a felhasználó nevében, anélkül, hogy megosztaná a felhasználó jelszavát. Az OAuth segítségével a felhasználók engedélyezhetik egy alkalmazás számára, hogy hozzáférjen bizonyos adatokhoz vagy funkciókhoz egy másik alkalmazásban.

Az OAuth folyamatában általában négy szereplő van:

Felhasználó: Az a személy, aki hozzáférést ad az adataihoz.
Kliens: Az az alkalmazás, amely hozzáférést kér a felhasználó adataihoz.
Engedélyező szerver: Az a szerver, amely hitelesíti a felhasználót és engedélyezi a hozzáférést.
Erőforrás szerver: Az a szerver, amely az adatokat tárolja és kiadja a kliensnek az engedélyezés után.

Példa az OAuth használatára:
Egy webalkalmazás (kliens) szeretne hozzáférni a felhasználó Google Drive fájljaihoz. A felhasználó bejelentkezik a Google fiókjába (engedélyező szerver), és engedélyezi az alkalmazás számára a hozzáférést. Az alkalmazás ezután hozzáférhet a fájlokhoz anélkül, hogy a felhasználó jelszavát ismerné.

6. CORS (Cross-Origin Resource Sharing)
A CORS egy biztonsági mechanizmus, amely lehetővé teszi, hogy egy weboldal erőforrásokat kérjen le egy másik domainről. Alapértelmezés szerint a böngészők csak azonos domainről származó kéréseket engedélyeznek, de a CORS lehetővé teszi, hogy a szerver meghatározza, mely domain-ekről érkező kéréseket engedélyezi. Például, ha egy API támogatja a CORS-t, akkor egy másik domainről is lehet hozzá kéréseket küldeni.



Példa:
"""
Github hozzáférés beállítása:

Lépj be a GitHub fiókodba: Nyisd meg a GitHub weboldalt, és jelentkezz be a fiókodba.

-Kattints a jobb felső sarokban lévő profilképedre.

-A legördülő menüben válaszd a "Settings" (Beállítások) lehetőséget.

-A bal oldali menü aljáig görgess le, a "Developer settings" (Fejlesztői beállítások) részhez, és kattints rá.

-Válaszd a "Personal access tokens" (Személyes hozzáférési tokenek) lehetőséget.

-Kattints a "Generate new token" (Új token létrehozása) gombra. Jó a classic.

-Adj nevet a tokennek a "Note" mezőben, hogy később is tudd, mire használod.

-Válaszd ki a szükséges jogosultságokat (repo, user)

-Görgess le az oldal aljára, és kattints a "Generate token" gombra.

-A generált token megjelenik az oldalon. Másold ki ezt a tokent, és tárold biztonságos helyen, mert később nem fogod tudni újra megtekinteni.


Tesztelés Thunder Client-ben:

-Kattints a "New Request" gombra.

-Válaszd ki a HTTP metódust (GET).

-Írd be az API URL-t (https://api.github.com/user).

-Kattints az "Auth" fülre.

-Válaszd ki a "Bearer Token" autentikációs típust.

-Másold be a személyes hozzáférési tokent a "Token" mezőbe.

-Kattints a "Send" gombra a kérés elküldéséhez.


Most pedig lássuk hozzá programot:


<details>
<summary>Megoldás</summary>


```py
import requests
import json
from requests.auth import HTTPBasicAuth

url = "https://api.github.com/user"

# Auth/Basic
# username = "m0zs0"
# password = "****"
# response = requests.get(url, auth=HTTPBasicAuth(username, password))


# Auth/Bearer token
bearer_token = "ghp_4ywgCcHs0S5EybqaBwX66fh7sjPBN448krFD"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

response = requests.get(url, headers=headers)

print(json.dumps(response.json(), indent=4))

```
</details>



Feladatok:

#Időjárás lekérdezése: Kérj be egy magyar városnevet, és add meg az aktuális időjárást. (Használhatod az OpenWeatherMap.org/Current Weather Data API-t.)

#Hírek lekérdezése: Kérj be egy kulcsszót, és add meg a legfrissebb magyar híreket ezzel kapcsolatban. (Használhatod a newsapi.org API-t.)

#Sporteredmények: Kérj be egy sportágat, és add meg a legfrissebb magyar sporteredményeket. (Használhatod a newsapi.org API-t.)

#Könyv keresés: Kérj be egy könyvcímet, és add meg a könyv szerzőjét és rövid leírását. (Használhatod a googleapis.com/books API-t.)

#Recept keresés: Kérj be egy alapanyagot, és add meg a hozzá kapcsolódó recepteket. (Használhatod a Spoonacular.com API-t.)

#Repülőút: Holnap szereték BUDapestről ISTambulba repülni. Javasolj egy járatot, mikor indul és mikor érkezik! (Használhatod a Google Flights API-t - SerpApi)



Haladó:

#Közlekedési információk: Kérj be egy útvonalat, és add meg az aktuális forgalmi helyzetet. (Használhatod a BKK OpenData API-t; https://opendata.bkk.hu/ api kulcsot innen tudsz szerezni)

#Térkép információk: Kérj be egy helyszínt, és add meg a környékbeli érdekes helyeket. (Használhatod a OpenStreetMap API-t.)

#Moziműsorok: Kérj be egy városnevet, és add meg az aktuális moziműsorokat. (Használhatod a Cinema City API-t.) Először telepítsd a pycin csomagot: pip install pycin

#Álláskeresés: Kérj be egy munkakört, és add meg a legfrissebb állásajánlatokat Magyarországon. (Használhatod a Profession.hu -t.)

