import sys
input = sys.stdin.readline

r1, c1, r2, c2 = [int(x) for x in input().split()]

a = [[] for _ in range(r1, r2+1)]
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        b = max(abs(i),abs(j))
        if i >= j:
            if abs(i) == b and abs(i) != abs(j):
                a[i-r1].append((b*2+1)**2-i+j)    
            else:
                a[i-r1].append((b*2+1)**2-b*2+i+j)   
        else:
            if abs(i) == b and abs(i) != abs(j):
                a[i-r1].append((b*2+1)**2-b*4+i-j)   
            else:
                a[i-r1].append((b*2+1)**2-b*6-i-j)

maxV = max(max(aa) for aa in a)
maxL = len(str(maxV))

processedA = [[] for _ in range(r1, r2+1)]
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        s = ' ' * (maxL - len(str(a[i][j]))) + str(a[i][j])
        processedA[i].append(s)

print('\n'.join(' '.join(v for v in row) for row in processedA))