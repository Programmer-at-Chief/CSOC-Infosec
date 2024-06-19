import hashlib

with open("private_0a1880d1fffce9403686130a1f932b10.key","r") as file:
    data=file.read().split()


N=int(data[2])
d_value=int(data[5])

message="crypto{Immut4ble_m3ssag1ng}"

encoded_message=message.encode()
sha256_hash = hashlib.sha256()
sha256_hash.update(encoded_message)
hex_data= sha256_hash.digest()

hashed_message=int.from_bytes(hex_data,'big')

print(pow(hashed_message,d_value,N))
