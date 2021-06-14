
def ext_euclid(a, b):
    old_s,s=1,0
    old_t,t=0,1
    old_r,r=a,b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q=old_r//r
            old_r,r=r,old_r-q*r
            old_s,s=s,old_s-q*s
            old_t,t=t,old_t-q*t
    return old_s, old_t, old_r


# Using the two primes p = 26513, q = 32321, find the integers u,v such that

#p * u + q * v = gcd(p,q)
p = 26513
q = 32321

print(ext_euclid(p,q))
