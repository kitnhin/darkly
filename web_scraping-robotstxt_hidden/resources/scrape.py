import requests
import sys
from bs4 import BeautifulSoup

base_url = "http://192.168.165.3/.hidden/"
found = False

def find_flag(url, depth=0):
    global found
    
    if depth > 5 or found:
        return
    
    try:
        print(f"Trying: {url}")
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        
        for link in soup.find_all('a'): #find all returns a 2D array containing all the <a> tags: [<a href="link1">link1</a>, <a href="link2" ...]
            if found:
                return
            
            href = link.get('href')
            if not href or href == '../':
                continue
            
            full_url = url + href
            
            #if dir, go deeper
            if href.endswith('/'):
                find_flag(full_url, depth + 1)
            
            #If its a README, check for "flag"
            elif href == 'README':
                content = requests.get(full_url, timeout=5).text
                
                if 'flag' in content.lower():
                    print(f"\n{'='*60}")
                    print(f"FOUND FLAG at: {full_url}")
                    print(f"{'='*60}")
                    print(content)
                    print(f"{'='*60}\n")
                    found = True
    except:
        pass


find_flag(base_url)