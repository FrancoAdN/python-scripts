import requests

def main():
    word = 'cloudfare'
    url = 'https://www.cloudflare.com/es-es/'
    req = requests.get(url)
    headers = dict(req.headers)
    verify = False
    for h in headers:
        if word in headers[h].lower():
            verify = True
            break

    if verify:
        print('Cloudfare detected')
    else:
        print('Not Cloudfare detected')




if __name__ == '__main__':
    main()
