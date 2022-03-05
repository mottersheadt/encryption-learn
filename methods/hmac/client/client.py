import zmq
import json
from Crypto.Hash import HMAC, SHA256

secret = input("What is the secret that the server is expecting???\n")
hmac_validator = HMAC.new(bytes(secret, "ASCII"), digestmod=SHA256)

context = zmq.Context()

# Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    print("Type your message!")
    msg = input()
    
    hmac_validator.update(bytes(msg, "UTF-8"))
    mac = hmac_validator.hexdigest()

    print("Message Mac: " + mac)

    tosend = bytes(json.dumps({
        "mac": mac,
        "data": msg
    }), "UTF-8")
    
    socket.send(tosend)

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (tosend, message))

