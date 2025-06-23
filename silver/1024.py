import sys
input = sys.stdin.readline
output = []

n, l = [int(x) for x in input().split()]

def findSeq(n, l):
    if (n//l + 1) * 2 < l or l > 100:
        return [-1]
    if l % 2 == 0:
        if n % l != 0 and n*2 % l == 0:
            mid = n//l
            return list(x for x in range(mid-l//2+1, mid+l//2+1))
        else:
            return findSeq(n, l+1)
    else:
        if n % l == 0:
            mid = n//l
            return list(x for x in range(mid-l//2, mid+l//2+1))
        else:
            return findSeq(n, l+1)

output = findSeq(n,l)
sys.stdout.write(' '.join(str(x) for x in output))