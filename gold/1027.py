import sys
input = sys.stdin.readline
output = []

n = int(input())


h = [int(x) for x in input().split()]
maxV = 0

for i in range(len(h)):
    prevSlope = -1000000000
    count = 0
    for j in range(i+1, len(h)):
        slope = (h[j]-h[i])/(j-i)
        if slope > prevSlope:
            count += 1
            prevSlope = slope
    prevSlope = 1000000000
    for j in range(i-1, -1, -1):
        slope = (h[i]-h[j])/(i-j)
        if slope < prevSlope:
            count += 1
            prevSlope = slope

    maxV = max(maxV, count)


print(maxV)