hex_string="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
import binascii 

temp_key=binascii.hexlify("crypto{".encode("utf-8"))
# print(temp_key)
hex_chunks=[temp_key[i:i+2] for i in range(0,len(temp_key),2)]

# print(hex_chunks)
# print(temp_key[0])
# for i in temp_key:
    # print(i)
hex_bytes=bytes.fromhex(hex_string)
# for i in hex_bytes:
#     print(i)

index=0
# print(chr(hex_bytes[1]^int(hex_chunks[1],16)))
string=""
for i in hex_bytes:
    string+=chr(i^int(hex_chunks[index],16))
    index=(index+1)%7

key=string[:7]+"y"

hex_key=binascii.hexlify(key.encode("utf-8"))
# print(temp_key)
hex_key_chunks=[hex_key[i:i+2] for i in range(0,len(hex_key),2)]
# print(hex_key_chunks)
ans=""
for i in hex_bytes:
    ans+=chr(i^int(hex_key_chunks[index],16))
    index=(index+1)%len(hex_key_chunks)

print(ans)




