from selectorlib import Extractor
import json 
import requests 

eBay = Extractor.from_yaml_file('EBay.yml')

def scraper(url):  

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.ebay.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    print("Downloading product information from %s"%url)
    req = requests.get(url, headers=headers)
    if req.status_code > 500:
        print("Cannot get page. :(")
        return None
    print("Scraping complete for item. Results in result.jsonl")
    return eBay.extract(req.text)

with open("urls.txt",'r') as urls, open('result.jsonl','w') as outfile:
    for url in urls.read().splitlines():
        data = scraper(url) 
        if data:
            json.dump(data,outfile)
            outfile.write("\n")
                