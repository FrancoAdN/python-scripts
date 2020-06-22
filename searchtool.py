#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search', help="Search something at Google")
parser = parser.parse_args()


def main():
    if parser.search:
        search = mechanize.Browser()
        search.set_handle_robots(False)
        search.set_handle_equiv(False)
        search.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]
        search.open('https://www.google.com')

        search.select_form(nr=0)
        search['q'] = parser.search
        search.submit()
        
        p = BeautifulSoup(search.response().read(), 'html5lib')
        for link in p.find_all('a'):
            u = link.get('href')
            u = u.replace('/url?q=', '')
            print(u) 
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit..")
