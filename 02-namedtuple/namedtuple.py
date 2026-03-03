from collection import namedtuple

n = input()
title = input().strip()
sc = namedtuple('sc', title)
total = 0
for i in range(int(n)):
    line = input().strip().split()
    s = sc(*line)

    total += int(s.MARKS)

print(total / int(n))