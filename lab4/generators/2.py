class Even():
    def __init__(self, n):
        self.end = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.current <= self.end):
           x = self.current
           self.current += 2
           return x
        else:
            raise StopIteration()

def Even(end_point):
    current = 0
    while(current <= end_point)
    yield currentcurrent += 2

n = Even(int(input()))
print(*n, sep=', ')