import sys
input = sys.stdin.readline
n = int(input())

if n < 10:
    result = n
else:
    n -= 9
    prev = [[i] for i in range(10)]
    current = [[i] for i in range(10)]

    result = 0
    endFlag = False
    for digit in range(1, 11):
        for i in range(10):
            current[i] = []
            for j in range(i):
                cand = [i * 10**digit + p for p in prev[j]]
                current[i] += cand
                if n - len(cand) > 0:
                    n -= len(cand)
                else:
                    result = cand[n-1]
                    endFlag = True
                    break
            
            if endFlag:
                break
        prev = current.copy()
        if endFlag:
            break
    if result == 0:
        result = -1


print(result)