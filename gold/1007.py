import sys
input = sys.stdin.readline
output = []

t = int(input())

for _ in range(t):


    n = int(input())

    xy = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]

        xy.append((x,y))

    xTot = sum(x for (x,y) in xy)
    yTot = sum(y for (x,y) in xy)

    def select(selected, depth, minD, xSum, ySum):
        if depth == n//2:
            xSum = xSum * 2 - xTot
            ySum = ySum * 2 - yTot
            d = (xSum**2 + ySum**2)**0.5
            return min(minD, d)
        if depth == 0:
            x = 0
        else:
            x = selected[-1]
        for i in range(x+1, n):
            minD = min(minD, select(selected + [i], depth+1, minD, xSum+xy[i][0], ySum+xy[i][1]))
        return minD
    
    result = select([],0,1000000, 0, 0)

    output.append(result)


sys.stdout.write('\n'.join(str(x) for x in output))
    