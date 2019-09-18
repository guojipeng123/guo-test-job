import base64
import rsa


def rsa_decrypt_password(encrypted_password, private_key):
    return rsa.decrypt(base64.decodestring(encrypted_password), rsa.PrivateKey.load_pkcs1(private_key))
