import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

a = {}

for _ in range(n):
    x = input().strip()
    if x in a:
        a[x] += 1
    else:
        a[x] = 1

k = int(input())

maxV = 0

for key, value in a.items():
    zeroCount = key.count('0')
    if zeroCount <= k and (k-zeroCount)%2 == 0:
        maxV = max(maxV, value)

print(maxV)