from bs4 import BeautifulSoup as bs
import requests as req
from tabulate import tabulate
import os
from colorama import Fore
import pyfiglet 
def srape(url,element):
  try:
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"} 
    res = req.get(url, headers=headers, timeout=400)
    data = res.text
    soup = bs(data, 'html.parser')
    if element=='table':
        t = soup.find_all('table')
        for _tt in t:
            rows = _tt.find_all('tr')
            header = [th.text.strip() for th in rows[0].find_all('th')] 
            data = [[td.text.strip() for td in row.find_all('td')] for row in rows[1:]] 
            print(tabulate(data, headers=header, tablefmt="grid"))  
            print("\n")
    else:
        d=soup.find_all(element)
        if len(d)==0:
            print("No such element found")
        else:
            for i in d:
                print(i.get_text(strip=True))
  except Exception as e:
    print(Fore.RED +"Error in scraping the data")

def scrape(url,_class):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
        res = req.get(url, headers=headers, timeout=600)
        res.raise_for_status() 
        data = res.text
        soup = bs(data, 'html.parser')
        d = soup.find_all(class_=_class)
        if len(d)==0:
            print("No such class found")
        else:
            for i in d:
                print(i.get_text(strip=True))
    except Exception as e:
        print(Fore.RED +"Error in fetching the data",e)
            
def scrape_links(url):
    try:
         headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
         res = req.get(url, headers=headers, timeout=600)
         res.raise_for_status() 
         data = res.text
         soup = bs(data, 'html.parser')
         d=soup.find_all('a')
         for i in d:
            print(Fore.YELLOW+i.get('href'))
    except Exception as e:
        print(Fore.RED +"Error in fetching the data",e)
def dork(url):
    try:
        if url.startswith("https://"):
            url2 = url.replace("https://","")
        elif url.startswith("http://"):
            url2 = url.replace("http://","")
        else:
            url2=url
        url1 = f"https://web.archive.org/cdx/search/cdx?url={url2}&collapse=urlkey&matchType=prefix&filter=mimetype:application/pdf&collapse=digest&output=json"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
        res = req.get(url1, headers=headers)
        datas = res.json()
        _dir = os.getcwd()
        file = f"{_dir}/Results/links.txt"
        if datas:
         for i in datas:
            timestamp=i[1]
            links=i[2]
            timestamp=str(timestamp)+"if_"
            _fil_link = f"https://web.archive.org/web/{timestamp}/{links}"
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, "a") as f:
              f.write(f"{_fil_link}\n")
            print(Fore.YELLOW+_fil_link)
         print(Fore.WHITE +"The links are saved in Results/links.txt"+Fore.WHITE)
        else:
            print(Fore.RED+"No data found")
    except Exception as e:
        print(e)
def scrapeId(url,_id):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
        res = req.get(url, headers=headers, timeout=600)
        res.raise_for_status() 
        data = res.text
        soup = bs(data, 'html.parser')
        d = soup.find_all(id=_id)
        if len(d)==0:
            print("No such id found")
        else:
            for i in d:
                result = i.get_text(strip=True, separator=' | ')
                result = result.replace("|","\n")
                print(Fore.WHITE+result)
    except Exception as e:
        print(Fore.RED +"Error in fetching the data",e)
            
styled_text=pyfiglet.figlet_format('WEB SCRAPER',font= 'doom')
print(Fore.BLUE + styled_text)
print(Fore.LIGHTBLUE_EX + "https://github.com/abin-karukappallil/Advanced-web-scraper\n"+Fore.WHITE)
url = input("Enter the URL: ")
choice = input(Fore.BLUE + "\n1. Scrape with class name.\n2. Scrape with element.\n3. Scarpe with id.\n4. Scrape hidden links\n5. Scrape confidential documents\nChoose an option: "+Fore.WHITE)
if choice == '1':
    _class = input("Enter the class you want to scrape: ")
    scrape(url,_class)
elif choice == '2':
    element = input("Enter the element you want to scrape: ")
    srape(url,element)
elif choice == '3':
    id = input("Enter the element you want to scrape: ")
    scrapeId(url,id)
elif choice == '4':
    scrape_links(url)
elif choice == '5':
    dork(url)
