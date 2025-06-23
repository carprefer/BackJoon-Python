import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

min6 = 10000
min1 = 10000

for _ in range(m):
    package, single = [int(x) for x in input().split()]

    min1 = min(min1, single)
    min6 = min(min6, min(package, 6*single))

print((n//6)*min6 + min((n%6)*min1, min6))