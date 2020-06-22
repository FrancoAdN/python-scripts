#!/usr/bin/env python
#_*_ coding: utf8 _*_
from Wappalyzer import WebPage, Wappalyzer

def main():
    wap = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url('http://maxpower-ar.com/')
        techs = wap.analyze(web)
        for t in techs:
            print('Technology {}'.format(t))
    except:
        print('An error has occurred')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit..")
        exit()