import sys
from collections import deque
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

ps = [int(x)-1 for x in input().split()]

q = deque(range(n))

result = 0
for p in ps:
    a = q.index(p)
    b = len(q) - a
    if a <= b:
        result += a
        q.rotate(-a)
    else:
        result += b
        q.rotate(b)
    q.popleft()
print(result)