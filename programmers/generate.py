def generatePermutation(arr, r, cur):
    if len(cur) == r:
        yield cur
        return
    for i in range(len(arr)):
        yield from generatePermutation(arr, r, cur + [arr[i]])


def generateCombination(arr, r, cur, start):
    if len(cur) == r:
        yield cur
        return
    for i in range(start, len(arr)):
        yield from generatePermutation(arr, r, cur + [arr[i]], i + 1)



parent = {}
rank = {}
def makeset(x):
    parent[x] = x
    rank[x] = 0
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x
def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        if rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            if rank[rx] == rank[ry]:
                rank[ry] += 1
            parent[rx] = ry


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

from collections import deque
d = deque([1, 2, 3, 4, 5])

# 오른쪽으로 2칸 회전
d.rotate(2)
print(d)  # deque([4, 5, 1, 2, 3])

# 왼쪽으로 2칸 회전 (음수값 사용)
d.rotate(-2)
print(d)  # deque([1, 2, 3, 4, 5]) (원래대로 복구됨)


