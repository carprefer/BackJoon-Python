import sys
input = sys.stdin.readline


n = int(input())

parents = [int(x) for x in input().split()]

delNum = int(input())

childs = {}

for i, p in enumerate(parents):
    if p in childs:
        childs[p].append(i)
    else:
        childs[p] = [i]

def countLeaf(root):
    if root not in childs:
        return 1
    nexts = childs[root]
    sum = 0
    if len(nexts) == 1 and nexts[0] == delNum:
        return 1
    for n in nexts:
        if n != delNum:
            sum += countLeaf(n)
    
    return sum

if childs[-1][0] == delNum:
    print(0)
else:
    print(countLeaf(-1))