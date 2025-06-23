import sys
input = sys.stdin.readline


n, m = [int(x) for x in input().split()]

pan = []

for _ in range(n):
    s = input()
    pan.append(s)

result = 64
for i in range(n-7):
    for j in range(m-7):
        togle = 'W'
        count = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if pan[y][x] == togle:  
                    count += 1
                togle = 'W' if togle == 'B' else 'B'
            togle = 'W' if togle == 'B' else 'B'
        result = min(result, min(count, 64-count))


print(result)