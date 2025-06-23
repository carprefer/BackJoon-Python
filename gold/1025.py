import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

big, small = (n,m) if n > m else (m, n)

a = []
for _ in range(n):
    a.append(input())

b = [[-1 for _ in range(big)] for _ in range(small)]
for i in range(small):
    for j in range(big):
        if n > m:
            b[i][j] = a[j][i]
        else:
            b[i][j] = a[i][j]

s = [set() for _ in range(big + 1)]

for yGap in range(-small + 1, small):
    for xGap in range(-big + 1, big):
        for yStart in range(small):
            for xStart in range(big):
                if xGap == 0 and yGap == 0: 
                    s[1].add(int(b[yStart][xStart]))
                    continue
                ss = []
                i = yStart
                j = xStart
                while True:
                    ss.append(b[i][j])
                    if len(ss) > 0:
                        s[len(str(int(''.join(ss))))].add(int(''.join(ss)))
                    i += yGap
                    j += xGap
                    if i < 0 or i >= small or j < 0 or j >= big:
                        break
                

maxV = -1
for i in range(len(s)-1, -1, -1):
    for x in s[i]:
        if x**0.5 == int(x**0.5):
            maxV = max(maxV, x)
    if maxV != -1:
        break

print(maxV)

