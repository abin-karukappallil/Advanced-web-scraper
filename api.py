from bs4 import BeautifulSoup as bs
import requests as req
from tabulate import tabulate
import os
from fastapi import FastAPI,HTTPException,Query
from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re
import traceback

app = FastAPI()

# CORS configuration
origins = [
    "https://ws-ui-ten.vercel.app",
    "http://localhost:3000",  
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,  
    allow_methods=["*"], 
    allow_headers=["*"], 
)
def srape(url, element):
   try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        } 
        res = req.get(url, headers=headers, timeout=40)
        res.raise_for_status() 
        data = res.text
        soup = bs(data, 'html.parser')

        if element == 'table':
            tables = soup.find_all('table')
            results = []
            for i, table in enumerate(tables, start=1):
                rows = table.find_all('tr')
                header = [th.text.strip() for th in rows[0].find_all('th')] 
                data = [[td.text.strip() for td in row.find_all('td')] for row in rows[1:]]  
                results.append({"id": i, "data": {"header": header, "data": data}})
            return results  
        else:
            elements = soup.find_all(element)
            if not elements:
                return [{"id": "", "data": "No such element found"}]
            return [{"id": i + 1, "data": el.get_text(strip=True)} for i, el in enumerate(elements)]
   except Exception as e:
        return str(e)
def scrape(url,_class):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
        res = req.get(url, headers=headers, timeout=600)
        res.raise_for_status() 
        data = res.text
        soup = bs(data, 'html.parser')
       # print(soup.prettify())
        elements = soup.find_all(class_=_class)
        results = []
        if not elements:
            print("No elements found with the specified class.")
        else:
            for element in elements:
                text = element.get_text(separator=' | ', strip=True)
                split_items = text.split(" | ")
                results.extend(split_items)
        response = [{"id": i + 1, "data": item} for i, item in enumerate(results)]
        print("Formatted Output:\n")
        for item in response:
            print(f"id: {item['id']}, data: {item['data']}")
        return response
    except Exception as e:
        return "Error in scraping the data"
def idScrape(url,_id):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
        res = req.get(url, headers=headers, timeout=600)
        res.raise_for_status() 
        data = res.text
        soup = bs(data, 'html.parser')
       # print(soup.prettify())
        elements = soup.find(id=_id)
        results = []
        if not elements:
            return "No elements found with the specified class."
        else:
            for element in elements:
                text = element.get_text(separator=' | ', strip=True)
                split_items = text.split(" | ")
                results.extend(split_items)
        response = [{"id": i + 1, "data": item} for i, item in enumerate(results)]
        print("Formatted Output:\n")
        for item in response:
            print(f"id: {item['id']}, data: {item['data']}")
        return response
    except Exception as e:
       return "Error in scraping the data"
             
def scrape_links(url):
    try:
         headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
         res = req.get(url, headers=headers, timeout=600)
         res.raise_for_status() 
         data = res.text
         soup = bs(data, 'html.parser')
         d=soup.find_all('a')
         _dir = os.getcwd()
         file = f"{_dir}/Results/hiddenlinks.txt"
         for i in d:
             _fil_link = i.get('href')
             os.makedirs(os.path.dirname(file), exist_ok=True)
             with open(file, "a") as f:
                f.write(f"{_fil_link}\n")
    except Exception as e:
        return "Error in scraping the data"
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
            #print(i[2])
         #print(Fore.YELLOW +"The links are saved in Results/links.txt"+Fore.WHITE)
        else:
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, "a") as f:
              f.write("no documents found")
            return "No documents found"
    except Exception as e:
        return e
@app.get("/")
def read_root():
    return {"message": "Web Scraping API is running"}
@app.get("/scrape-element")
def scrape_element(url:str,element:str):
    try:
        result= srape(url,element)
        return result;
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@app.get("/scrape-hiddenlinks")
def scrape_lnk(url:str):
    try:
        _dir = os.getcwd()
        fileP = f"{_dir}/Results/hiddenlinks.txt"
        if os.path.exists(fileP):
            os.remove(fileP)
            open(fileP, 'w').close()
        scrape_links(url)
        return FileResponse(fileP, media_type="application/octet-stream", filename="hiddenlinks.txt")
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}, 500
        raise HTTPException(status_code=500,detail=str(e))
@app.get("/confi-doc")
def scrape_confidential(url:str):
    try:
        _dir = os.getcwd()
        fileP = f"{_dir}/Results/links.txt"
        if os.path.exists(fileP):
            os.remove(fileP)
            open(fileP, 'w').close()
        dork(url)
        response= FileResponse(fileP, media_type="application/octet-stream", filename="documentlinks.txt")
        return response
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@app.get("/scrape-class")
def scrape_element(url:str,_class:str):
    try:
        result= scrape(url,_class)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@app.get("/scrape-id")
def scrape_id(url:str,_id:str):
    try:
        result= idScrape(url,_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))