def unique(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x
a = [int(x) for x in input().split()]
print(unique(a))