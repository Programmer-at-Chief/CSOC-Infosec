def extended_gcd(a,b):
    if (a==0):
        return b,0,1
    g,x,y=extended_gcd(b%a,a)
    return g,y-(b//a)*x,x

def mod_inverse(p,q,e):
    totient=(p-1)*(q-1)
    g,x,y=extended_gcd(e,totient)
    return x%totient 


p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

print(mod_inverse(p,q,e))
