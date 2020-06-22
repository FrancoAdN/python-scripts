import sys
from shodan import Shodan
import argparse

reload(sys)
sys.setdefaultencoding('utf8')

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', help='Query')
parser.add_argument('-a', '--api', help="Your Shodan api key")
parser = parser.parse_args()

def main():
    if parser.query and parser.api:
        api = Shodan(parser.api)
        try:
            b = api.search(parser.query)
            print('Total targets: {}'.format(b['total']))
            for i in b['matches']:
                print('Target found: {}'.format(i['ip_str']))
        except:
            print('An error has occurred')
            
    else:
        print('Both params (query and api) are required')
    


if __name__ == '__main__':
    main()
    