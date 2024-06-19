def mod(n,pow,base):
    ans=1
    while(pow!=0):
        if (pow&1):
            ans*=(n%base)
            pow-=1
        else:
            n*=n
            pow=pow//2
    return ans%base

# print(mod(3,5,17))
print(mod(273246787654,65536,65537))


