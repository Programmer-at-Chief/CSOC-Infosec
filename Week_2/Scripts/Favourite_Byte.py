hex_string="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

given_hex=bytes.fromhex(hex_string)

for i in range(255):
    # key=bytes.fromhex(hex(i))
    ans=""
    for j in given_hex:
        ans+=chr(i^j)

    if (ans[0:6]=="crypto"):
        print(ans)
