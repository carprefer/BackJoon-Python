import sys
input = sys.stdin.readline

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


n, m = [int(x) for x in input().split()]

tp = [int(x) for x in input().split()][1:]

graph = {}

pps = []

for _ in range(m):
    pp = [int(x) for x in input().split()][1:]
    pps.append(pp)

    for i in range(len(pp)-1):
        for j in range(i+1, len(pp)):
            if pp[i] in graph:
                graph[pp[i]].append(pp[j])
            else:
                graph[pp[i]] = [pp[j]]
            if pp[j] in graph:
                graph[pp[j]].append(pp[i])
            else:
                graph[pp[j]] = [pp[i]]
    if len(pp) == 1 and pp[0] not in graph:
        graph[pp[0]] = []


for x in range(1, n+1):
    makeset(x)

for t in tp:
    union(t, tp[0])


for k, vs in graph.items():
    for v in vs:
        union(k, v)

fp = []
for x in graph.keys():
    if len(tp) == 0 or find(x) != find(tp[0]):
        fp.append(x)
        
count = 0
for pp in pps:
    if all(p in fp for p in pp):
        count += 1

print(count)
