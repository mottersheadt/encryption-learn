from Crypto.Hash import HMAC, SHA256
import json
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

secret = input("What is the secret that we are expecting???\n")

hmac_validator = HMAC.new(bytes(secret, "ASCII"), digestmod=SHA256)

print("Waiting for messages....")
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    payload = json.loads(message.decode("utf-8"))
    try:
        hmac_validator.update(bytes(payload['data'], "UTF-8"))
        hmac_validator.hexverify(payload['mac'])
        print("The message '%s' is authentic" % payload['data'])
        socket.send(b"Great success. We have received and validated your message.")
    except ValueError:
        print("The message or the key is wrong")
        socket.send(b"Your message couldn't be validated!")
    
