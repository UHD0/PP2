def squares(current, end_point):
    while(current ** 2 <= end_point):
        yield current ** 2
        current += 1

cur = int(input())
end = int(input())
for i in squares(cur, end)
  print(i)