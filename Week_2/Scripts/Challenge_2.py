import base64

flag_encoded="01000011 01010011 01001111 01000011 00110010 33 7b 6a 75 35 37 5f ZDFmZjNyM243XzNuYw== 60 144 61 156 66 65 137 154 60 154 175".split()
flag=""
for i in range(0,5):
    flag+=chr(int(flag_encoded[i],2))
# print(flag)
for i in range(5,12):
    flag+=chr(int(flag_encoded[i],16))
# print(flag)

decode_bytes = base64.b64decode(flag_encoded[12])

decoded_flag= decode_bytes.decode('utf-8')

flag+=decoded_flag
# print(flag)
# print(chr(int("61",8)))

for i in range(13,len(flag_encoded)):
    flag+=chr(int(flag_encoded[i],8))

print(flag)
