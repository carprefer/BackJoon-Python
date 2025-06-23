import sys
input = sys.stdin.readline

n, a, b = [int(x) for x in input().split()]

big = max(a,b)
small = min(a,b)

count = 1
while True:
    if small % 2 == 1 and big == small + 1:
        break
    n //= 2
    small = small // 2 + (small%2)
    big = big // 2 + (big%2)
    count += 1

print(count)
        
            