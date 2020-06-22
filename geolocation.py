import urllib
import json

def main():
    ip = '190.210.176.21'
    url = 'https://ipinfo.io/{}/json'.format(ip)
    v = urllib.urlopen(url)
    j = json.loads(v.read())
    for data in j:
        print('{}: {}'.format(data, j[data]))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()