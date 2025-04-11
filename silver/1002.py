n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in input().split()]
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    bigR, smallR = (r1, r2) if r1 >= r2 else (r2, r1) 
    if d == 0 and bigR == smallR:
        print(-1)
    elif d > bigR:
        if smallR + bigR < d:
            print(0)
        elif smallR + bigR == d:
            print(1)
        elif smallR + bigR > d:
            print(2) 
    elif d == bigR:
        print(2)
    elif d < bigR:
        if d + smallR < bigR:
            print(0)
        elif d + smallR == bigR:
            print(1)
        elif d + smallR > bigR:
            print(2)