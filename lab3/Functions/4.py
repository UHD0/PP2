def filter_prime(a, y):
    for i in range(len(a)):
        if a[i] == 1:
            continue
        t = True
        for j in range(2, a[i]):
            if a[i] % j == 0:
                t = False
                break
        if t == True:
            y.append(a[i])
    

a = [int(x) for x in input().split()]
y=[]
print(a)
filter_prime(a, y)
print(y)