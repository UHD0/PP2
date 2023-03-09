def rev(x):
    x.reverse()
        
s = str(input())
x = s.split()
rev(x)
r = ' '.join(str(x) for x in x)
print(r)