import sys
input = sys.stdin.readline


s, N, K, R1, R2, C1, C2 = [int(x) for x in input().split()]

def dc(t, n, k, r1, r2, c1, c2):
    if t == 0:
        return [[0]]
    if t == 1:
        a = [[1 if j >= (n-k)//2 and j < (n-k)//2 + k and i >= (n-k)//2 and i < (n-k)//2 + k else 0 for j in range(n)] for i in range(n)]
        return [ar[c1:c2+1] for ar in a][r1:r2+1]
    else:
        a = [[[] for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
        ax = 0
        ay = 0
        nn = n**(t-1)
        for i in range(n):
            yd = 0
            for j in range(n):
                rs = max(r1, i*nn) - i*nn
                cs = max(c1, j*nn) - j*nn
                re = min(r2, i*nn+nn-1) - i*nn
                ce = min(c2, j*nn+nn-1) - j*nn
                if rs > re or cs > ce:
                    continue
                if j >= (n-k)//2 and j < (n-k)//2 + k and i >= (n-k)//2 and i < (n-k)//2 + k:
                    ta = [[1]*(ce-cs+1)]*(re-rs+1)
                else:
                    ta = dc(t-1, n, k, rs, re, cs, ce)
                for ty in range(re-rs+1):
                    for tx in range(ce-cs+1):
                        a[ay+ty][ax+tx] = ta[ty][tx]

                ax += (ce-cs+1)
                yd = re-rs+1

            ax = 0
            ay += yd

        return a



output = dc(s, N, K, R1, R2, C1, C2)

for o in output:
    print(''.join(str(oo) for oo in o))