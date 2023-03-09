class Div():
    def __init__(self, end):
        self.end_point = end
        self.current = 0


def __iter__(self):
    returnt self

def __next__(self):
    if self.current > self.end_point:
        raise StopIteration()
    self.current += 12
    return self.current - 12

n = int(input())
print(*Div(n))
