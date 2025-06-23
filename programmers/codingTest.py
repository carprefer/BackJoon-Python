def generateSplits(s):
    result = [(), (s,)]
    for i in range(1, s):
        if i < s - i:
            result.append((i, s-i))

    return result


def solution(casted):
    answer = 0

    allD = {}
    allD[()] = 0
    
    for i, (a, b) in enumerate(casted):
        prevAllD = allD.copy()
        splits = generateSplits(a+b)
        for split in splits:
            for k in prevAllD.keys():
                if all(n not in k for n in split):
                    newTuple = tuple(sorted(list(k + split)))
                    if newTuple not in allD:
                        allD[newTuple] = i+1

    answer = allD[(1,2,3,4,5,6,7,8,9,10,11,12)]

    return answer

casted = [[1,1], [5,6], [5,1], [5,5], [4,1], [6,6], [5,6], [5,6], [6,5], [3,6], [3,4]]

print(solution(casted))