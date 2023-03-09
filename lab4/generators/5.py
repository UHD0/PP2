def down(n):
    i = n
    while(i >= n):
        yield i 
        i -= 1

n = int(input())

for i in squares(n):
    print(i)