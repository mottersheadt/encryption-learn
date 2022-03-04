from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import os
 
keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
pubKeyASCII = pubKeyPEM.decode('ascii')

with open('./client/rsa-key.pub', 'w') as f:
    f.write(pubKeyASCII)

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
privKeyASCII = privKeyPEM.decode('ascii')
 
with open('./server/rsa-key.priv', 'w') as f:
    f.write(privKeyASCII)
