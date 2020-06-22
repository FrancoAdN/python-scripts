import dns.resolver
from os import path

host =  'google.com'
words = 'brutesub.txt'

def main():
    if path.exists(words):
        wordlist = open(words, 'r')
        wordlist = wordlist.read().split('\n')
        subdom = []
        for w in wordlist:
            try:
                a = dns.resolver.query('{}.{}'.format(w, host), 'A')
                subdom.append('{}.{}'.format(w, host))
            except:
                pass
        
        print('{} subdomains found'.format(len(subdom)))
        if len(subdom) > 0:
            print('\n')
            for sub in subdom:
                print(sub)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit..")
        exit()