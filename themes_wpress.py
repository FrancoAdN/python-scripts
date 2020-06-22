#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://curso--python-0-pruebas1.000webhostapp.com/'
    headers = {'User-Agent': 'Firefox'}
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'html5lib')  
    for link in soup.find_all('link'):
        if '/wp-content/theme' in link.get('href'):
            th = link.get('href')
            th = th.split('/')
            if 'themes' in th:
                pos = th.index('themes')
                theme = th[pos + 1]
                print('Theme: {}'.format(theme))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit..")
        exit()