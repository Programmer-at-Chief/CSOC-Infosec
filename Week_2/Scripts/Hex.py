hex_flag="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# ans_string=""
# for i in range(0,len(hex_flag),2):
#     ans_string+=chr(int(hex_flag[i:i+2],16))
#

ans_string=bytes.fromhex(hex_flag)
print(ans_string)

