import sys
input = sys.stdin.readline
output = []

n = int(input())

a = [(int(x), i) for i, x in enumerate(input().split())]

a.sort(key=lambda x: x[0])

b = [x + (i,) for i, x in enumerate(a)]
b.sort(key=lambda x: x[1])



sys.stdout.write(' '.join(str(x[2]) for x in b))