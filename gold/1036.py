import sys
input = sys.stdin.readline
output = []
def _36to10(ss):
    acc = 0
    for s in ss:
        if s.isdigit():
            n = int(s)
        else:
            n = 10 + (ord(s) - ord('A'))
        acc *= 10
        acc += n
    return n

n = int(input())

ss = []
for _ in range(n):
    ss.append(input())

k = int(input())

ca = [[0 for _ in range(50)] for _ in range(36)]

for i in range(n):
    for j, s in enumerate(ss[i][::-1]):
        ca[_36to10(s)][j] += 1

sa = [0 for _ in range(36)]
for i in range(36):
    sa[i] = [cfor j, c in enumerate(ca[i])
