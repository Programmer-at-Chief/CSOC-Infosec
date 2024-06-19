def extended_gcd(a,b):
    if (a==0):
        return b,0,1
    g,x,y=extended_gcd(b%a,a)
    return g,y-(b//a)*x,x

def mod_inverse(p,q,e):
    totient=(p-1)*(q-1)
    g,x,y=extended_gcd(e,totient)
    return x%totient 

def cipher_decryption(c,d,n):
    ans=1
    while(d!=0):
        if (d&1):
            ans*=c%n
            d-=1
        else:
            c=(c*c)%n
            d=d//2

    return ans%n


p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

d=(mod_inverse(p,q,e))
N = 882564595536224140639625987659416029426239230804614613279163
c = 77578995801157823671636298847186723593814843845525223303932

print(cipher_decryption(c,d,N))
