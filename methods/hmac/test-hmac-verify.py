from Crypto.Hash import HMAC, SHA256

# We have received a message 'msg' together
# with its MAC 'mac'


while True:
    secret = b'testo'
    h = HMAC.new(secret, digestmod=SHA256)
    print("Enter update value:")
    val = input()
    h.update(bytes(val, "UTF-8"))
    mac = h.hexdigest()
    print(mac)

    newH = HMAC.new(secret, digestmod=SHA256)
    newH.update(bytes(val, "UTF-8"))
    
    try:
        newH.hexverify(mac)
        h.hexverify(mac)
        print("The message '%s' is authentic" % val)
    except ValueError:
        print("The message or the key is wrong")
