from Crypto.PublicKey import ECC
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import binascii
import os
import base64

def encrypt(msg):
    #get the reciever's public key
    f = open("./client/ecc-public-key.pem", 'rt') # a.salama.pem
    recipient_key = ECC.import_key(f.read())
    f.close()

    # Encrypt the session key with the reciever's public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)

    return cipher_rsa.encrypt(msg)

keyPair = ECC.generate(curve='P-256')

pubKey = keyPair.public_key()
pubKeyPEM = pubKey.export_key(format="PEM")
print(f"Public key:  \n{pubKeyPEM}")

privKeyPEM = keyPair.export_key(format="PEM")
print(f"Private key:  \n{privKeyPEM}")

with open('./client/ecc-public-key.pem', 'w') as f:
    f.write(pubKeyPEM)

with open('./server/ecc-private-key.pem', 'w') as f:
    f.write(privKeyPEM)

data = get_random_bytes(16)
print(encrypt(data))
