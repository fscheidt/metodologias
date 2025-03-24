import hashlib
def encrypt_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    sha1_hash = hashlib.sha1(password_bytes)
    encrypted_password = sha1_hash.hexdigest()
    return encrypted_password

if __name__ == "__main__":
    res = encrypt_password("1234")
    print(res) # 7110eda4d09e062aa5e4a390b0a572ac0d2c0220
