import sys
input = sys.stdin.readline

n = int(input())


a = [int(x) for x in input().split()]

min1 = min(a)
min2 = sum(sorted(a)[-2:])
for i in range(6):
    for j in range(6):
        if j != i and j != 5-i:
            min2 = min(min2, a[i]+a[j])
min3 = sum(sorted(a)[-3:])
for i in range(6):
    for j in range(6):
        if j != i and j != 5-i:
            for k in range(6):
                if k != i and k != j and k != 5-i and k != 5-j:
                    min3 = min(min3, a[i]+a[j]+a[k])

min5 = sum(sorted(a)[:-1])

if n == 1:
    print(min5)
else:
    print(min3 * 4 + min2 * 4 * (2*n-3) + min1 * 5 * (n-2)**2 + min1 * 4 * (n-2))