"""
Codevita problem VVV IMP
"""
def isPrime(n):
    b = True
    for x in range(2,n-1):
        if(n%x==0):
            b = False
            break
    return b

totalHr , division = map(int,input().split())
peroid = int(totalHr /division)
counter = 0
for i in range(2,peroid):
    if isPrime(i):
        for j in range(1,division):
            if isPrime(peroid*j+i):
                if totalHr - (peroid*j+i) < peroid :
                    counter+=1
                    break
                continue
            else:
                break

print(counter,end="")


