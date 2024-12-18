# Valutaváltás
## Kérj be egy Ft összeget, add meg az aktuális árfolyamon, hogy mennyi Euro-t ér.

### Előkészületek:
1. Keressünk REST API-t hozzá:

  - pl: https://currencyapi.com/

  - Get Free API Key

  - regisztráljunk be

  - email visszaigazolása után, megvan az apikey.

2. Listázzuk ki az alapértelemzett valuta (USD) váltási arányait:
   
![currencyapi1.PNG](PICTURES/currencyapi1.PNG)

  https://api.currencyapi.com/v3/latest?apikey=cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx

3. Ezt próbáljuk meg Thunder Client-ben is:

![currencyapi2.PNG](PICTURES/currencyapi2.PNG)

4. Listázzuk ki a valuta nemeket (Dokumentációt kell megnyitni):

![currencyapi3.PNG](PICTURES/currencyapi3.PNG)

  https://api.currencyapi.com/v3/currencies?apikey=cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx

5. Próbáljuk ezt ki a Thunder Client-tel is:

![currencyapi4.PNG](PICTURES/currencyapi4.PNG)

6. Próbáljuk ki a felületen, hogy 1 EURO (base) hány forint:

![currencyapi5.PNG](PICTURES/currencyapi5.PNG)

  https://api.currencyapi.com/v3/latest?apikey=cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx&currencies=HUF&base_currency=EUR

7. Próbáljuk ezt ki a Thunder Client-tel is:

![currencyapi6.PNG](PICTURES/currencyapi6.PNG)

<details>
<summary>Megoldás</summary>

```py
import requests

be_huf = int(input("Kérem az átváltandó összeget Ft-ban: "))
endpoint = "https://api.currencyapi.com/v3/latest"
apikey="cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx"
currencies = "HUF"
base_currency = "EUR"

url = f"{endpoint}?apikey={apikey}&currencies={currencies}&base_currency={base_currency}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    exchange_rate = data['data']['HUF']['value']
    print(f"{be_huf} Ft = {be_huf / exchange_rate:.2f} Euro")
else:
    print("Nem sikerült az adatlekérés.")
```
</details>
