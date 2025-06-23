import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

arr = []

for _ in range(n):
    arr.append([int(x) for x in list(input().strip())])

maxWindow = -1
for i in range(n):
    for j in range(m):
        for k in range(maxWindow+1, min(n-i,m-j)):
            if arr[i][j] == arr[i+k][j] and arr[i][j] == arr[i][j+k] and arr[i][j] == arr[i+k][j+k]:
                maxWindow = k

print((maxWindow+1)**2)
        
            