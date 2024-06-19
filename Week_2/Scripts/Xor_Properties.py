KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_1_3_2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1=(bytes.fromhex(KEY1))#.lstrip("b'").rstrip("'")
key2=(bytes.fromhex(KEY2_3))
key3=(bytes.fromhex(FLAG_1_3_2))

anskey=""
for i in range(len(key1)):
    anskey+= chr(key1[i]^key2[i]^key3[i])

print(anskey)


