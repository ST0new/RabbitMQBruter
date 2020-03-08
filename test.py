import os
import hashlib
import struct
import sys
import base64


def rabbit_password_hashing_MD5(password, salt=None):
    # 1
    if salt is None:
        salt = os.urandom(4)
    # 2
    salt_pass = salt + password.encode('utf-8')
    # 3 这里使用的不是邮件例子中的 MD5，而是配置文件 hashing_algorithm 中指定的 SHA256
    pass_md5 = hashlib.md5(salt_pass).digest()
    # 4
    salted_hash = salt + pass_md5
    # 5
    pass_hash = base64.b64encode(salted_hash)
    return pass_hash.decode("utf-8")


def check_rabbit_password_hashing_sha256(password):
    # 这里写加密后的值
    target_hash = "31WzvIfGPVmFclmi7bU4sQSJBaM="
    salt = base64.b64decode(target_hash.encode('utf-8'))[:4]
    try_password = rabbit_password_hashing_MD5(password, salt)

    if target_hash == try_password:
        print('用户密码正确' + '-->', password)

if __name__ == "__main__":
    with open('123.txt', 'r') as zd:
        for ps in zd.readlines():
            ps = ps[:-1]
            check_rabbit_password_hashing_sha256(ps)
