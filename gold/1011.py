import sys
input = sys.stdin.readline
output = []

t = int(input())


for _ in range(t):
    x, y = [int(x) for x in input().split()]
    d = y - x
    k = int(d**0.5)
    if d < k*(k+1):
        k -= 1
    r = d - k*(k+1)

    if r == 0:
        count = 2*k
    elif r <= k+1:
        count = 2*k + 1
    elif r <= 2*k+1:
        count = 2*k + 2

    output.append(count)

sys.stdout.write('\n'.join(str(x) for x in output))