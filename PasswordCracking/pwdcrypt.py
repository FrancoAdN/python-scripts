import hashlib

def main():
    password = str(raw_input("Word: "))
    md5pass = hashlib.md5(password).hexdigest()
    print("MD5: " + md5pass)
    sha1 = hashlib.sha1(password).hexdigest()
    print("SHA1: " + sha1)
    sha224 = hashlib.sha224(password).hexdigest()
    print("SHA224: " + sha224)
    sha256 = hashlib.sha256(password).hexdigest()
    print("SHA256: " + sha256)
    sha384 = hashlib.sha384(password).hexdigest()
    print("SHA384: " + sha384)
    sha512 = hashlib.sha512(password).hexdigest()
    print("SHA512: " + sha512)




if __name__ == "__main__":
    main()