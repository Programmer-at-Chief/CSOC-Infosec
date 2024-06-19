# from cryptography import x509
# from cryptography.hazmat.backends import default_backend
# from asn1crypto import x509
from Crypto.PublicKey import RSA

with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der',"rb") as file:
    data=file.read()

key=RSA.import_key(data)
print(key.n)


# cert=x509.load_der_x509_certificate(data,default_backend())
# key=cert.subject
# modulus=key.public_numbers()
