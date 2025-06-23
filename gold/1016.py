import sys
input = sys.stdin.readline

minV, maxV = [int(x) for x in input().split()]

bound = int(maxV**0.5)
primes = list(range(bound+1))
for i in range(2, len(primes)):
    if primes[i] != -1:
        for j in range(i*i, len(primes), i):
            primes[j] = -1

primes = [p for p in primes if p != -1][2:]


d = list(range(maxV - minV +1))

for i in primes:
    start = minV // (i*i)
    end = maxV // (i*i)
    for j in range(start*i*i, (end+1)*i*i, i*i):
        idx = j - minV
        if idx >= 0 and idx <= maxV - minV:
            d[idx] = -1
    
count = 0
for x in d:
    if x != -1:
        count += 1

print(count)
