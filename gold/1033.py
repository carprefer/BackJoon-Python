import sys
input = sys.stdin.readline

n = int(input())

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def simplify(a):
    g = a[0]
    for i in range(1,len(a)):
        g = gcd(g, a[i])
    return [aa//g for aa in a]

mass = [0]*n
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, p, q = [int(x) for x in input().split()]
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))

visit = [False]*n
seq = []
def explore(x):
    visit[x] = True
    for y, p, q in graph[x]:
        if not visit[y]:
            seq.append((x,y,p,q))
            explore(y)

explore(0)

for a,b,p,q in seq:
    p, q = simplify([p, q])
    if mass[a] == 0 and mass[b] == 0:
        mass[a] = p
        mass[b] = q
    elif mass[a] == 0:
        mass[a] = p * mass[b]
        for i in range(n):
            if i != a:
                mass[i] *= q
    elif mass[b] == 0:
        mass[b] = q * mass[a]
        for i in range(n):
            if i != b:
                mass[i] *= p

if n == 1:
    mass = [1]

print(' '.join(str(m) for m in simplify(mass)))
    

