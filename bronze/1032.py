import sys
input = sys.stdin.readline


n = int(input())

result = list(input().strip())
for _ in range(n-1):
    s = input().strip()
    for i in range(len(s)):
        if result[i] != s[i]:
            result[i] = '?'

print(''.join(result))

