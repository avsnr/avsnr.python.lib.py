import requests
import os
tsx = input("[-] Enter text to search :")
url = requests.get(f"https://www.flaticon.com/search?word={tsx}&order_by=4").content
s = BeautifulSoup(url,"lxml")
c = 0
for i in s.find_all("img"):
    c+=1
    sea = (i.get("data-src"))
    txt = f"{sea}"
    getx = (txt.replace("None",""))
    print(f"[{c}] - Url : {getx}")




    
