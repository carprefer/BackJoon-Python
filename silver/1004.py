t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = [int(x) for x in input().split()]

        d1 = ((x1 - cx)**2 + (y1 - cy)**2)**0.5 
        d2 = ((x2 - cx)**2 + (y2 - cy)**2)**0.5

        if d1 < r and d2 > r or d1 > r and d2 < r:
            count += 1
    print(count)