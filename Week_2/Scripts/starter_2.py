def rsa_encrypt(e,p,q,m):
    base=p*q
    ans=1
    while (e!=0):
        if (e&1):
            ans*=m%base
            e-=1
        else:
            m*=m
            e=e//2

    return ans%base

print(rsa_encrypt(65537,17,23,12))

