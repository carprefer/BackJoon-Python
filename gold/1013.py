import sys
input = sys.stdin.readline
output = []

t = int(input())


for _ in range(t):
    s = input()

    ## 0: start
    ## 1: 100로 시작
    ## 2: 100+1 중간 
    ## 3: dead
    state = 0
    i = 0
    while i < len(s) - 1:
        if state == 0:
            if s.find('100', i) == i:
                state = 1
                i += 3
            elif s.find('01',i) == i:
                state = 0
                i += 2
            else:
                state = 3
                break
        elif state == 1:
            j = s.find('1', i)
            if j >= i:
                state = 2
                i = j + 1
            else:
                state = 3
                break
        elif state == 2:
            j = s.find('0', i)
            k = s.find('01', i)
            l = s.find('100', i)
            if j == -1:
                break
            elif j == k and (l == -1 or k < l):
                state = 0
                i = k + 2
            elif l != -1 and l < j:
                state = 1
                i = l + 3
            else:
                state = 3
                break

    if state == 0 or state == 2:
        output.append('YES')
    else:
        output.append('NO')

sys.stdout.write('\n'.join(str(x) for x in output))