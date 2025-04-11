import sys
input = sys.stdin.readline

t = int(input())

output = []

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]       # weight
    edges = [[] for _ in range(n)]
    for _ in range(k):
        x, y = [int(x) for x in input().split()]
        edges[x-1].append(y-1)

    w = int(input())


    def dfs():
        visit = [False for _ in range(n)]
        topo = []
        stack = []
        for i in range(n):
            if not visit[i]:
                stack.append(i)
                while len(stack) > 0:
                    s = stack.pop()
                    if visit[s]:
                        topo.append(s) 
                        continue
                    visit[s] = True
                    stack.append(s)
                    for e in edges[s]:
                        if not visit[e]:
                            stack.append(e)
        return list(reversed(topo))

    topo = dfs()

    dijk = d.copy()

    for u in topo:
        for v in edges[u]:
            dijk[v] = max(dijk[v], dijk[u] + d[v])

    output.append(dijk[w-1])

sys.stdout.write('\n'.join([str(x) for x in output]))



