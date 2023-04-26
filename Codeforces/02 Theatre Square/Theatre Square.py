from math import ceil
m, n, a = map(int, input().split())
num_flagstones = ceil(n/a) * ceil(m/a)
print(num_flagstones)
