import sys
from shodan import Shodan

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    ip = '190.210.176.21'
    api = Shodan('WZqoK8tS9NZc8rjhwP6PD4XVEjTlU0Ey')
    h = api.host(ip)
    print('''
        Direction: {}
        City: {}
        ISP: {}
        Org: {}
        Ports: {}'''.format(h['ip_str'], h['city'], h['isp'], h['org'], h['ports']))
    
    file = open('scan-{}.txt'.format(ip), 'a+')
    
    for elem in h['data']:
        lst = elem.keys()
        for l in lst:
            file.write(str(elem[l]))

    file.close()




if __name__ == '__main__':
    main()
    
