
import dns.resolver

query = ['A', 'NS','MD', 'MF', 'CNAME', 'SOA', 'MB', 'MG', 'MR']

def main():
    try:
        a = dns.resolver.query('maxpower-ar.com', 'ANY')
        for q in a:
            print(q)
    except:
        print('Error')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit..")
        exit()