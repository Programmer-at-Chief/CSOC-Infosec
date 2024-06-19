from Crypto.PublicKey import RSA
import base64
import struct

with open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub","r") as file:
    data=file.read().split(' ')


# print(data[1])
byte_data=base64.b64decode(data[1])

# key=RSA.import_key(byte_data)
# print(key.n)

def read_ssh_string(data):
    str_len = struct.unpack('>I', data[:4])[0]
    return data[4:4+str_len], data[4+str_len:]

   
key_type, rest = read_ssh_string(byte_data)

exponent, rest = read_ssh_string(rest)
modulus, _ = read_ssh_string(rest)

# modulus=data[8:12]

modulus=int.from_bytes(modulus, byteorder='big')


print(modulus)
