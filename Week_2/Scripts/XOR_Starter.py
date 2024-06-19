import pwn 
string="label"
new_string=""
for i in string:
    new_string += str(pwn.xor(13,i)).lstrip("b'").rstrip("'")
print(new_string)
