import time
import zmq
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

priv_key_file = open("rsa-private-key.pem")
priv_key_contents = priv_key_file.read()
priv_key_file.close()
private_key = RSA.import_key(priv_key_contents)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(message)

    print("Decrypted message: %s" % str(decrypted_message))

    #  Send reply back to client
    socket.send(decrypted_message)
