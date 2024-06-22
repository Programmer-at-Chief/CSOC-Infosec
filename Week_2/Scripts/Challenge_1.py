flag="43104f0c32017b48340179266203350636025f6b6e0a5f2730423f42"
new_flag=""
for i in range(0,len(flag),4):
    # new_flag+=(e[i:i+2])
    new_flag+=format(int(flag[i:i+2],16)^int(flag[i:i+4],16),'02x')
    # print(int(e[i:i+2],16)," ",int(e[i:i+4],16)," ",int(e[i:i+2],16)^int(e[i:i+4],16))

# print(new_flag)
convert_to_hex= bytes.fromhex(new_flag)

ascii_flag= convert_to_hex.decode()

print(ascii_flag)
