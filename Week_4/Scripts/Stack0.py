import random

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ"
ans=""
for i in range(77):
    ans+=random.choice(chars)
print(ans)
