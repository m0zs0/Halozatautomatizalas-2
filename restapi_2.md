#Valutaváltás
**Kérj be egy Ft összeget, add meg az aktuális árfolyamon, hogy mennyi Euro-t ér.**

##Előkészületek:
1. Keressünk REST API-t hozzá:
pl: https://currencyapi.com/
2. próbáljuk ki a használatát:
-Get Free API Key
-monoki.zsolt@moriczref.hu
-XiMeFE7rGD96W@3
-email visszaigazolása után, megvan az apikey:

![currencyapi1.PNG](PICTURES/currencyapi1.PNG)

3. Listázzuk ki az alapértelemzett valuta (USD) váltási arányait:

https://api.currencyapi.com/v3/latest?apikey=cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx

4. Ezt próbáljuk meg Thunder Client-ben is:

![currencyapi2.PNG](PICTURES/currencyapi2.PNG)

5. Listázzuk ki a valuta nemeket:

https://api.currencyapi.com/v3/currencies?apikey=cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx

![currencyapi3.PNG](PICTURES/currencyapi3.PNG)

6. Próbáljuk ezt ki a Thunder Client-tel is:

![currencyapi4.PNG](PICTURES/currencyapi4.PNG)

7. Próbáljuk ki a felületen, hogy 1 EURO (base) hány forint:

https://api.currencyapi.com/v3/latest?apikey=cur_live_7w7VgNsyesqcZlWoa1Cdqm5yUvn7Br7eFCKvVFxx&currencies=HUF&base_currency=EUR

![currencyapi5.PNG](PICTURES/currencyapi5.PNG)

8. Próbáljuk ezt ki a Thunder Client-tel is:

![currencyapi6.PNG](PICTURES/currencyapi6.PNG)


