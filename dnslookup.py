import requests
from bs4 import BeautifulSoup

def main():
    host = 'wnpower.com'
    headers = {'User-Agent': 'Firefox'}
    req = requests.get('https://viewdns.info/reverseip/?host={}&t=1'.format(host), headers=headers)
    html = BeautifulSoup(req.text, 'html5lib')
    d = html.find(id="null").find(border="1")
    for l in d.find_all("tr"):
        print(l.td.string)
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()