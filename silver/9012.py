import sys
input = sys.stdin.readline
output = []

t = int(input())


for _ in range(t):
    s = input().strip()
    open = 0
    for c in s:
        if c == '(':
            open += 1
        else:
            open -= 1
        if open < 0:
            break
    if open == 0:
        output.append('YES')
    else:
        output.append('NO')

sys.stdout.write('\n'.join(str(x) for x in output))