import zmq
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def encrypt(msg):
    msg = 'A message for encryption'
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(bytes(msg, 'UTF-8'))
    print("Encrypted:", binascii.hexlify(encrypted))

key_file = open('rsa-public-key.pem','r')
pubkey = RSA.import_key(key_file.read())
key_file.close()

# Encrypt the session key with the public RSA key

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
while True:
    print("Type your message!")
    msg = input()
    
    cipher_rsa = PKCS1_OAEP.new(pubkey)
    tosend = cipher_rsa.encrypt(bytes(msg, 'utf-8'))
    
    socket.send(tosend)

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (tosend, message))

