def modulus(num,power,base):
    ans=1
    while(power!=0):
        if (power&1):
            ans*=num%base
            power-=1
        else:
            num*=num
            power=power//2

    return ans%base
print(modulus(101,17,22663))
