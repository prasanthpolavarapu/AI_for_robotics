#Write code that outputs p after multiplying each entry
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2
world=['G','R','R','G','G']
#Enter code here

for i in range(len(world)):
    if world[i]=='G':
        p[i]=p[i]*pMiss
    else:
        p[i]=p[i]*pHit
print(p)
#probability of all cells is 0.36
print(sum(p))