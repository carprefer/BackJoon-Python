import sys
input = sys.stdin.readline
output = []

t = int(input())


for _ in range(t):
    m, n, k = [int(x) for x in input().split()]

    map = [[0 for _ in range(m)] for _ in range(n)]
    parent = [[(i,j) for i in range(m)] for j in range(n)]
    def root(x,y):
        while parent[y][x] != (x,y):
            (x,y) = parent[y][x]
        return (x, y)
    for _ in range(k):
        x, y = [int(x) for x in input().split()]
        map[y][x] = 1
        flag = False
        if x-1 >= 0 and map[y][x-1] == 1:
            parent[y][x] = root(x-1,y)
            flag = True
        if x+1 < m and map[y][x+1] == 1:
            if flag:
                (rx, ry) = root(x+1, y)
                parent[ry][rx] = root(x,y)
            else:
                parent[y][x] = root(x+1,y)
                flag = True
        if y-1 >= 0 and map[y-1][x] == 1:
            if flag:
                (rx, ry) = root(x, y-1)
                parent[ry][rx] = root(x,y)
            else:
                parent[y][x] = root(x,y-1)
                flag = True
        if y+1 < n and map[y+1][x] == 1:
            if flag:
                (rx, ry) = root(x, y+1)
                parent[ry][rx] = root(x,y)
            else:
                parent[y][x] = root(x,y+1)
                flag = True
                
    count = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == 1 and parent[i][j] == (j, i):
                count += 1
    output.append(count)

sys.stdout.write('\n'.join(str(x) for x in output))