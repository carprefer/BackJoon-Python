import sys
input = sys.stdin.readline

t = int(input())
output = []

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    d = []
    a1 = a % 10
    c1 = a1
    for i in range(10):
        r = c1 if c1 != 0 else 10
        if r in d:
            break
        d.append(r)
        c1 = (c1 * a1) % 10
    output.append(d[(b-1)%len(d)])

sys.stdout.write('\n'.join([str(x) for x in output]))
    
