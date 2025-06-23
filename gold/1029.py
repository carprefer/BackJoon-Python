import sys
input = sys.stdin.readline


n = int(input())

price = []

for _ in range(n):
    price.append([int(x) for x in list(input().strip())])

dp = [[[-1 for _ in range(2**15)] for _ in range(10)] for _ in range(n)]

def visit2int(visit):
    sum = 0
    for i in range(len(visit)):
        sum *= 2
        sum += visit[i]
    return sum

def rec(x, p, visit):
    vIdx = visit2int(visit)
    if dp[x][p][vIdx] != -1:
        return dp[x][p][vIdx]
    
    maxV = 0
    endFlag = True
    for i in range(n):
        if not visit[i] and price[x][i] >= p:
            visit[i] = True
            maxV = max(maxV, rec(i, price[x][i], visit))
            visit[i] = False
            endFlag = False
    if endFlag:
        return sum(visit)

    dp[x][p][vIdx] = maxV
    return maxV

visit = [False for _ in range(n)]
visit[0] = True
print(rec(0, 0, visit))



"""
def dfs():
    visit = [False for _ in range(n)]
    totalMax = 0
    def explore(i, p, depth):
        nonlocal totalMax
        print(totalMax)

        cCount = 0
        for c in [idx for idx, v in enumerate(visit) if not v and idx != i]:
            for r in range(n):
                if not visit[r] and price[r][c] >= p:
                    cCount += 1
                    break
        if cCount == 0:
            return 1
        if cCount + depth <= totalMax:
            return 0
        
        visit[i] = True

        eMax = 0
        for j in range(n):
            if not visit[j] and price[i][j] >= p:
                eMax = max(eMax, explore(j, price[i][j], depth+1))
            totalMax = max(totalMax, eMax + depth)

        visit[i] = False

        return eMax+1
    
    return explore(0, 0, 1)

print(dfs())"""


