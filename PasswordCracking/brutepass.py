import hashlib
from urllib import urlopen

def main():
    hashpass = str(raw_input("HASH: "))
    pwdlst = urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read()
    
    for p in pwdlst.split('\n'):
        z = hashlib.md5(p).hexdigest()
        if z == hashpass:
            print("Password: {}\nHash: {}".format(p, z))
            break
            

if __name__ == "__main__":
    main()

