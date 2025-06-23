import sys
input = sys.stdin.readline

def bin2dec(bin):
    factor = 1
    sum = 0
    for b in reversed(bin):
        sum += factor * b
        factor *= 2
    return sum

n, k = [int(x) for x in input().split()]

bin = []

tn = n
while True:
    bin.append(tn%2)
    tn //= 2
    if tn == 0:
        break

bin.reverse()

all1 = bin.count(1)
front1 = bin.index(0) if 0 in bin else len(bin)

if all1 > k:
    if front1 >= k:
        print(2**(len(bin)) - n)
    else:
        second1 = bin.index(1, front1)
        count = front1
        for i in range(second1, len(bin)):
            if bin[i] == 1:
                count += 1
            else:
                second1 = i + 1
            if count == k:
                break
        bin[second1 - 1] = 1
        for i in range(second1, len(bin)):
            bin[i] = 0
        print(bin2dec(bin) - n)
else:
    print(0)


