a=26513
b=32321
# a=80
# b=55

def extended_gcd(a1,b1):
    if (b1==0):
        # return (0,1)
        return (1,0)
    else:
        tup=extended_gcd(b1,a1%b1)
        x1=tup[0]
        y1=tup[1]

        x=y1
        y=x1-(a1//b1)*y1
        return (x,y)

ans=extended_gcd(max(a,b),min(a,b))
print(min(ans[0],ans[1]))
