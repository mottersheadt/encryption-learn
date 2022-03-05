from Crypto.Hash import HMAC, SHA256

while True:
    secret = b'testo'
    h = HMAC.new(secret, digestmod=SHA256)
    print("Enter update value:")
    val = input()
    h.update(bytes(val, "UTF-8"))
    print(h.hexdigest())
