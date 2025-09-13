
# Don't run
# Don't run
# Don't run

import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=5g+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=5g+mobile%7CMobiles&requestId=74f10955-0e3e-434e-add2-2c8fbd4b0542&as-backfill=on"
i=2
z=0
while(i<303):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    divs = soup.find_all("div",class_ = "KzDlHZ")
    with open("Mobile_name.txt","a") as f:
        for div in divs:
            z=z+1
            r = div.get_text()
            s= f"{z} : {r}"
            f.write(f"{s}.\n")
    url = f"https://www.flipkart.com/search?q=5g+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=5g+mobile%7CMobiles&requestId=74f10955-0e3e-434e-add2-2c8fbd4b0542&as-backfill=on&page={i}"
    i=i+1