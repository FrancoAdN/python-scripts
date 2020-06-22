#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://curso--python-0-pruebas1.000webhostapp.com/'
    headers = {'User-Agent': 'Firefox'}
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
            break
    
    print(version)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit..")
        exit()
