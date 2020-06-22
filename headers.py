#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

parser = argparse.ArgumentParser(description='Header detector')
parser.add_argument('-t', '--target', help='TARGET')
parser = parser.parse_args()


def main():
    if parser.target:
        url = requests.get(url=parser.target)
        headers = dict(url.headers)
        for x in headers:
            print('{}: {}'.format(x, headers[x]))
    else:
        print('No target selected')
if __name__ == '__main__':
    main()