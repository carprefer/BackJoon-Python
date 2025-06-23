import sys
input = sys.stdin.readline

r, c = [int(x) for x in input().split()]
d = []
for _ in range(r):
    d.append([int(x) for x in list(input().strip())])

maxSize = 0
for i in range(r):
    for a in [j for j in range(c) if d[i][j] == 1]:
        if a >= maxSize:
            for j in range(maxSize, min(min(a+2, (r-i+1)//2+1),c-a+1)):
                stopFlag = False
                x = 0
                for k in range(1, j*2-1):
                    if k < j:
                        x += 1
                    else:
                        x -= 1
                    if d[i+k][a-x] != 1 or d[i+k][a+x] != 1:
                        stopFlag = True
                        break
                if not stopFlag:
                    maxSize = j

print(maxSize)
