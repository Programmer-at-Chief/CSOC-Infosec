def mod_inv(num,base):
    power=base-2
    ans=1
    while(power!=0):
        if (power&1):
            ans*=(num%base)
            power-=1
        else:
            num*=num
            power=power//2
    return ans%base
print(mod_inv(3,13))
        
