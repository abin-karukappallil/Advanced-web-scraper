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
        #print(d)
        if len(d)==0:
            print("No such element found")
        else:
            print(d)
            print("\n")
  except Exception as e:
    print(Fore.RED +"Error in scraping the data")

def scrape(url,_class,_id):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
        res = req.get(url, headers=headers, timeout=600)
        res.raise_for_status() 
        data = res.text
        soup = bs(data, 'html.parser')
       # print(soup.prettify())

        d = soup.find_all(class_=_class)
        #print(d)
        if len(d)==0:
            print("No such class found")
        else:
            for i in d:
                print(i.get_text(strip=True))
                if _id:
                 attribute_value = i.get(_id, "Attribute not found")
                 print(f"{_id}: {attribute_value}")
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
            print(i.get('href'))
    except Exception as e:
        print(Fore.RED +"Error in fetching the data",e)
def dork(url):
  try:
    dork = f'https://www.google.com/search?q=site:{url} ext:txt | ext:pdf | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:doc | ext:docx intext:“confidential” | intext:“Not for Public Release” | intext:”internal use only” | intext:“do not distribute”'
    res = req.get(dork)
    soup = bs(res.text, 'html.parser')
    #print(soup)
    d=soup.find_all('a')
    print(d)
    if url.startswith("https://"):
        url2 = url.replace("https://","")
    else:
        url2 = url.replace("http://","")
    for i in d:
      href=i.get('href')
      _dir = os.getcwd()
      file = f"{_dir}/Results/links.txt"
      if href.startswith(f"/url?q=https://{url2}") or href.startswith(f"/url?q=http://www.{url2}") or href.startswith(f"/url?q=https://www.{url2}") or href.startswith(f"/url?q=http://"):
          _fil_link = (href.replace("/url?q=","").split("&")[0]).replace("25","")
          os.makedirs(os.path.dirname(file), exist_ok=True)
          with open(file, "a") as f:
              f.write(f"{_fil_link}\n")
    print(Fore.YELLOW +"The links are saved in Results/links.txt"+Fore.WHITE)
  except Exception as e:
    print(Fore.RED +"Error in fetching the data",e)

styled_text=pyfiglet.figlet_format('WEB SCRAPPER',font= 'doom')
print(Fore.BLUE + styled_text)
print(Fore.LIGHTBLUE_EX + "https://github.com/abin-karukappallil/Advanced-web-scraper\n"+Fore.WHITE)
url = input("Enter the URL: ")
choice = input(Fore.BLUE + "\n1. Scrape with class name.\n2. Scrape with element.\n3. Scarpe with id.\n4. Scrape hidden links\n5. Scrape confidential documents\n Choose an option:")
if choice == '1':
    _class = input("Enter the class you want to scrape: ")
    _id = input("Enter the attribute you want to scrape else press 0: ")
    scrape(url,_class,_id)
elif choice == '2':
    element = input("Enter the element you want to scrape: ")
    srape(url,element)
elif choice == '3':
    id = input("Enter the element you want to scrape: ")
elif choice == '4':
    scrape_links(url)
elif choice == '5':
    dork(url)
