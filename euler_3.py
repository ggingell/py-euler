# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Function that determines if p is a factor of q
is_factor = lambda p,q: q % p == 0 and p or 0

a = list(range(2,10000))
for x in a:
    comp = []
    for y in a:
        comp.append(x*y)
    for z in comp:
        if z in a:
            a.remove(z)
print(a)
print '----------------------------------------'

target = 600851475143
for u in a:
    print(is_factor(u,target))
    