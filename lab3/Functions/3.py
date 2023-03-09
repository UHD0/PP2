def solve(numheads,numlegs):
    ns ='No solutions!'
    for i in range(numheads+1):
        j = numheads-i
        if 2*i + 4*j == numlegs:
            return i,j
    return ns, ns

numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))