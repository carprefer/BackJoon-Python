from collections import deque
import sys
input = sys.stdin.readline


t = int(input().strip())

for _ in range(t):
    p = input().strip()

    n = int(input().strip())

    X = [x for x in input().strip()[1:-1].split(',') if x != '']

    X = deque(X)

    error = False
    isForward = True
    for c in p:
        if c == 'R':
            isForward = not isForward
        elif c == 'D':
            if len(X) == 0:
                error = True
                break
            if isForward:
                X.popleft()
            else:
                X.pop()
    if error:
        print('error')
    else:
        if not isForward:
            X.reverse()

        print('[' + ','.join(X) + ']')
