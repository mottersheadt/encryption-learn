from Crypto.PublicKey import ECC

def get_or_create_public_key(filename: str = "private_key.pem"):
""" Helper function to retrieve public key """
    private_key_file = os.path.join(settings.BASE_DIR, filename)
    if os.path.exists(private_key_file):
        file = open(private_key_file, "rt")
        private_key = ECC.import_key(file.read(), passphrase=settings.SECRET_KEY)
    else:
        private_key = ECC.generate(curve="P-256")
        file = open(private_key_file, "wt")
        file.write(
            private_key.export_key(
                format="PEM",
                use_pkcs8=True,
                passphrase=settings.SECRET_KEY,
                protection="PBKDF2WithHMAC-SHA1AndAES128-CBC",
            )
        )

    file.close()
    public_key = private_key.public_key()
    return public_key.export_key(format="PEM")
