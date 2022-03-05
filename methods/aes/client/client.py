import zmq
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP

key_file = open('rsa-public-key.pem','r')
pubkey = RSA.import_key(key_file.read())
key_file.close()

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    print("Type your message!")
    msg = input()
    
    cipher_rsa = PKCS1_OAEP.new(pubkey)
    tosend = cipher_rsa.encrypt(bytes(msg, 'utf-8'))
    
    socket.send(tosend)

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (tosend, message))

